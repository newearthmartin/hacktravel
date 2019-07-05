import json
import logging
from .eth import *
from .models import Org
import requests
import threading

logger = logging.getLogger(__name__)

def start_scan_thread():
    logger.info('Starting scan loop!')
    def loop():
        while True: scan()
    threading.Thread(target=loop).start()

def scan():
    logger.info('Getting segments')
    segments_count = wt_entrypoint.functions.getSegmentsLength().call()

    segments = []
    for i in range(0, segments_count):
        segment_name = wt_entrypoint.functions.getSegmentName(i).call()
        if not segment_name: continue
        segment = wt_entrypoint.functions.getSegment(segment_name).call()
        segments.append((segment_name,segment))

    logger.info('Found %d segments' % len(segments))

    orgs = []
    for segment_name, segment_address in segments:
        orgs += scan_segment(segment_name, segment_address)
    logger.info('Total %d organizations in all segments' % len(orgs))
    store_orgs(orgs)

def scan_segment(segment_name, segment_address):
    logger.info('Segment %s: %s' % (segment_name, segment_address))
    contract = wt_segment(segment_address)
    orgs = contract.functions.getOrganizations().call()
    orgs = [org for org in orgs if int(org,0) != 0]
    logger.info("Found %d organizations in '%s' segment. Retrieving..." % (len(orgs), segment_name))
    orgs = [get_org(org_address) for org_address in orgs]
    for org in orgs:
        org['segment'] = segment_name
    return orgs

def get_org(org_address):
    contract = wt_organization(org_address)
    json_url = contract.functions.getOrgJsonUri().call()
    owner = contract.functions.owner().call()
    logger.debug('organization %s - %s' % (org_address, json_url))
    response = requests.get(json_url)
    json_text = None

    if response.status_code == 200:
        try:
            json.loads(json_text)
        except:
            logger.info('invalid JSON for org %s' % org_address)
            json_text = None
    return {
        'org_id': org_address,
        'json_url': json_url,
        'json_text': json_text,
        'owner': owner
    }

def store_orgs(orgs):
    logger.info('Storing %d orgs' % len(orgs))
    added_orgs = []
    for org in orgs:
        org_id = org['org_id']
        db_org = Org.objects.filter(org_id=org_id)
        if db_org.exists():
            db_org = org.all()[0]
        else:
            logger.info('NEW org! %s' % org_id)
            db_org = Org(org_id=org_id)
        db_org.owner =  org['owner']
        db_org.json_url = org['json_url']
        db_org.json_text = org['json_text']
        #db_org.lif_balance = org['lif_balance']
        #db_org.trust_clues = org['trust_clues']
        db_org.save()
        added_orgs.append(org_id)
    for db_org in Org.objects.all():
        if db_org.org_id not in added_orgs:
            logger.info('Org %s no longer present, deleting' % db_org.org_id)
            db_org.delete()
