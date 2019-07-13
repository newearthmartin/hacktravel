#!/usr/bin/env python

import django
django.setup()

from scanner.models import Org

org1 = Org(org_id='0x98Fa47CFA890b12465775c723C072376FC64eE1e')
org1.json_url = 'https://raw.githubusercontent.com/newearthmartin/hacktravel/master/files/hotel_01.json'
org1.json_text = '{"dataFormatVersion":"0.2.3","updatedAt":"2019-06-03T13:20:06.398Z","legalEntity":{"name":"Martin\'s hotel S.A.","address":{"road":"Av Cabildo","houseNumber":"1234","city":"Buenos Aires","countryCode":"AR"},"contact":{"email":"info@martin.com"}},"hotel":{"location":{"latitude":-34.5683865,"longitude":-58.4507712},"name":"Martin\'s Hotel","website":"https://hotel-martin.com","apis":[{"entrypoint":"https://api.hotel-martin.com","docs":"https://developers.hotel-martin.com","format":"ota","version":"2.0"}]}}'
org1.lif_balance = '77000000000000000000'
org1.save()