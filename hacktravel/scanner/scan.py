import json
import logging
import requests
import threading
import time
import traceback
from cache_utils.decorators import cached
from django.conf import settings
from .eth import *
from .models import Org


logger = logging.getLogger(__name__)


def start_scan_thread():
    logger.info('Starting scan thread')
    def loop():
        while True:
            try:
                scan()
            except:
                traceback.print_exc()
            logger.info('sleeping %d minutes' % settings.SCAN_THREAD_SLEEP)
            time.sleep(settings.SCAN_THREAD_SLEEP * 60)
    threading.Thread(target=loop).start()


def scan():
    logger.info('Starting scan loop')
    segments = get_segments()
    orgs = []
    for segment_name, segment_address in segments:
        orgs += scan_segment(segment_name, segment_address)
    logger.info('Total %d organizations in all segments' % len(orgs))
    delete_non_present(orgs)

@cached(settings.CACHE_TIMEOUT_SEGMENTS * 60)
def get_segments():
    logger.info('Getting segments')
    segments_count = wt_entrypoint.functions.getSegmentsLength().call()
    segments = []
    for i in range(0, segments_count):
        segment_name = wt_entrypoint.functions.getSegmentName(i).call()
        if not segment_name: continue
        segment = wt_entrypoint.functions.getSegment(segment_name).call()
        segments.append((segment_name,segment))
    logger.info('Found %d segments' % len(segments))
    return segments


def scan_segment(segment_name, segment_address):
    orgs = get_orgs_in_segment(segment_name, segment_address)
    stored_orgs = []
    for org_address in orgs:
        org_data = get_org(org_address, segment_name)
        db_org = save_org(org_data)
        stored_orgs.append(db_org)
    return stored_orgs

@cached(settings.CACHE_TIMEOUT_SEGMENT_ORGS * 60)
def get_orgs_in_segment(segment_name, segment_address):
    logger.info('Retrieving orgs in segment %s' % segment_name)
    contract = wt_segment(segment_address)
    orgs = contract.functions.getOrganizations().call()
    orgs = [org for org in orgs if int(org,0) != 0]
    logger.info("Found %d organizations in '%s' segment. Retrieving..." % (len(orgs), segment_name))
    return orgs


def get_org(org_address, segment):
    org = get_basic_org(org_address)
    json_url = org['json_url']
    logger.debug('organization %s - %s' % (org_address, json_url))
    json_text, _ = get_json(org['json_url'], org_address)
    lif_balance = get_lif_balance(org_address)
    org.update({
        'segment': segment,
        'lif_balance': lif_balance,
        'json_text': json_text
    })
    return org


@cached(settings.CACHE_TIMEOUT_ORG * 60)
def get_basic_org(org_address):
    contract = wt_organization(org_address)
    json_url = contract.functions.getOrgJsonUri().call()
    owner = contract.functions.owner().call()
    return {
        'org_id': org_address,
        'json_url': json_url,
        'owner': owner,
    }


def get_json(json_url, org_address):
    json_text = get_url(json_url)
    json_parsed = None
    if json_text:
        try:
            json_parsed = json.loads(json_text)
        except ValueError:
            logger.debug('invalid JSON for org %s - %s' % (org_address, json_url))
            json_text = None
    return json_text, json_parsed


@cached(settings.CACHE_TIMEOUT_URLS * 60)
def get_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.ConnectionError as e:
        logger.warning('Connection error for ' + url)
    except:
        traceback.print_exc()
    return None



@cached(settings.CACHE_TIMEOUT_LIF_BALANCE * 60)
def get_lif_balance(org_address):
    lif_contract = wt_liftokentest('0xB6e225194a1C892770c43D4B529841C99b3DA1d7')
    return str(lif_contract.functions.balanceOf(org_address).call())


def save_org(org):
    org_id = org['org_id']
    db_org = Org.objects.filter(org_id=org_id)
    if db_org.exists():
        db_org = db_org.first()
    else:
        logger.info('NEW org! %s' % org_id)
        db_org = Org(org_id=org_id)
    db_org.owner = org['owner']
    db_org.segment = org['segment']
    db_org.json_url = org['json_url']
    db_org.json_text = org['json_text']
    db_org.lif_balance = org['lif_balance']
    # db_org.trust_clues = org['trust_clues']
    db_org.save()
    return db_org


def delete_non_present(orgs):
    present_ids = [org.org_id for org in orgs]
    for db_org in Org.objects.all():
        if db_org.org_id not in present_ids:
            logger.info('Org %s no longer present, deleting' % db_org.org_id)
            db_org.delete()

