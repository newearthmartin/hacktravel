import logging
from .eth import *
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
    organizations = contract.functions.getOrganizations().call()
    print(organizations)


