# Create your views here.
from django.http import HttpResponse
from GearSwap.models import GearItem
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext

def index(request):
    return render_to_response('gearswap/index.html', {'title': 'Gear Surf', 'subtitle':'Rent your gear', 'top_text':'How does it work', 'second_text':'We facilitate peer to peer gear rentals. Want gear? Rent it. Have gear? Rent it!'}, context_instance=RequestContext(request))

def list_all_gear(request):
    gear_list = GearItem.objects.filter(is_available=True)

    return render_to_response('gearswap/search_list.html', {'title': 'Gear Surf', 'subtitle': 'Rent your gear', 'gear_list': gear_list, 'sidebar_title': 'See our gear', 'sidebar_text': 'Some more info about our gear here', 'main_title':'All Available Gear', 'main_subtitle':'All Available gear is listed below'}, context_instance=RequestContext(request))

def gear_detail(request, gear_id):
    gear_item = GearItem.objects.get(id=gear_id)

    return render_to_response('gearswap/gear_detail.html', {'title': gear_item.name, 'gear_item': gear_item, 'sidebar_title': 'Sidebar title text here', 'sidebar_text': 'Sidebar text here'}, context_instance=RequestContext(request))

def rented(request, gear_id):
    gear_to_rent = GearItem.objects.get(id=gear_id)
    gear_to_rent.is_available = False
    gear_to_rent.save()

    return render_to_response('gearswap/rented.html', {'title': 'Rented', 'gear_to_rent': gear_to_rent, 'sidebar_title': 'Sidebar title texthere', 'sidebar_text':'Sidebar text here'}, context_instance=RequestContext(request) )
