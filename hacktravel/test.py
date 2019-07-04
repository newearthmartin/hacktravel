#!/usr/bin/env python

import requests

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("San Francisco")

#print(location.address)
#print((location.latitude, location.longitude))
#print(location.raw)

WT_URL = 'http://localhost:3000'
path = '/hotels?location=%s,%s' % (location.latitude,location.longitude)

print(path)

r = requests.get(WT_URL +  path)
print(r.text)