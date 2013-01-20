# Create your views here.
from django.http import HttpResponse
from GearSwap.models import GearItem
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext

def index(request):
    return render_to_response('GearSwap/index.html', {'title': 'Gear Surf'}, context_instance=RequestContext(request))

#def list_all_gear(request):


