# Create your views here.
from django.http import HttpResponse
from GearSwap.models import GearItem
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext

def index(request):
    return render_to_response('gearswap/index.html', {'title': 'Gear Surf', 'subtitle':'Rent your gear', 'top_text':'How does it work', 'second_text':'We facilitate peer to peer gear rentals. Want gear? Rent it. Have gear? Rent it!'}, context_instance=RequestContext(request))

#def list_all_gear(request):


