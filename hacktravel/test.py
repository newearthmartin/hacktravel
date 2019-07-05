#!/usr/bin/env python
import django
django.setup()

from scanner.scan import *
#scan_segment('hotels','0x8ea119A7Ef0Ac4c1a83a3BB6D1aa1a3afcAfDE8b')
scan()

#print(get_org('0x98Fa47CFA890b12465775c723C072376FC64eE1e','hotels'))