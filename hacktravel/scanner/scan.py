import logging
from .eth import *
import requests
logger = logging.getLogger(__name__)


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

    for segment_name, segment_address in segments:
        scan_segment(segment_name, segment_address)

def scan_segment(segment_name, segment_address):
    logger.info('Segment %s: %s' % (segment_name, segment_address))
    contract = wt_segment(segment_address)
    orgs = contract.functions.getOrganizations().call()
    orgs = [org for org in orgs if int(org,0) != 0]
    logger.info('found %d organizations in segment %s' % (len(orgs), segment_name))
    return [get_org(org_address) for org_address in orgs]

def get_org(org_address):
    contract = wt_organization(org_address)
    json_url = contract.functions.getOrgJsonUri().call()
    owner = contract.functions.owner().call()
    logger.info('organization %s - %s' % (org_address, json_url))
    response = requests.get(json_url)
    json_text = response.text if response.status_code == 200 else None
    return {
        'json_url': json_url,
        'json_text': json_text,
        'owner': owner
    }

