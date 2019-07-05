import json
from django.http import HttpResponse
from .models import Org

import sys
import threading
from .scan import start_scan_thread

if 'runserver' in sys.argv: # HACK!
    start_scan_thread()

def home(request):
    return HttpResponse('Access list of orgs at /orgs')

def orgs_view(request):
    orgs = Org.objects.all()
    orgs = [{
        'org_id': org.org_id,
        'json_url': org.json_url,
        'json_text': org.json_text, # maybe too much!
        'lif_balance': org.lif_balance,
        'trust_clues': org.trust_clues,
    } for org in orgs]
    return HttpResponse(json.dumps(orgs))
