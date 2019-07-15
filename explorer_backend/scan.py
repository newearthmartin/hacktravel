#!/usr/bin/env python
import django
django.setup()

from scanner.scan import scan

scan()
