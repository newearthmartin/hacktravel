from .eth import entrypoint_getSegmentsLength

def scan():
    segments_count = entrypoint_getSegmentsLength()
    for i in range(0, segments_count):
        print(i)
