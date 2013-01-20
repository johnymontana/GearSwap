# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from GearSwap.models import GearItem
from GearSwap.forms import (DocumentForm, RentForm)
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext

def index(request):
    return render_to_response('GearSwap/index.html', {'title': 'Gear Surf', 'subtitle':'Rent your gear', 'top_text':'How does it work', 'second_text':'We facilitate peer to peer gear rentals. Want gear? Rent it. Have gear? Rent it!'}, context_instance=RequestContext(request))

def list_all_gear(request):
    gear_list = GearItem.objects.filter(is_available=True)
    cat_list = []

    for gear in gear_list:
        cat_list.append(gear.type)


    return render_to_response('GearSwap/search_list.html', {'title': 'Gear Surf', 'subtitle': 'Rent your gear', 'gear_list': gear_list, 'sidebar_title': 'See our gear', 'sidebar_text': 'Some more info about our gear here', 'main_title':'All Available Gear', 'main_subtitle':'All Available gear is listed below', 'cat_list': cat_list}, context_instance=RequestContext(request))

def post_gear(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = GearItem(name = form.cleaned_data['name'],
                              type=form.cleaned_data['type'],
                              description=form.cleaned_data['description'],
                              dayRentalPrice=form.cleaned_data['dayRentalPrice'],
                              docfile = form.cleaned_data['docfile'],
                              user=form.cleaned_data['user'],
                              userEmail=form.cleaned_data['userEmail'],
                              is_available=True)
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('GearSwap.views.list_all_gear'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = GearItem.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'GearSwap/post_gear.html',
        {'documents': documents, 'form': form, 'title': 'Gear Surf', 'subtitle': 'Rent your gear', 'main_subtitle':'Post your gear for rent:'},
        context_instance=RequestContext(request)
    )

def gear_detail(request, gear_id):
    gear_item = GearItem.objects.get(id=gear_id)

    return render_to_response('GearSwap/gear_detail.html', {'title': gear_item.name, 'gear_item': gear_item, 'sidebar_title': 'Sidebar title text here', 'sidebar_text': 'Sidebar text here'}, context_instance=RequestContext(request))

def confirm_rent(request, gear_id):
    gear_to_rent = GearItem.objects.get(id=gear_id)
    form = RentForm() # A empty, unbound form

    # Load documents for the list page
    documents = GearItem.objects.all()

    return render_to_response(
        'GearSwap/confirm_rent.html',
        {'documents': documents, 'form': form, 'title': 'Confirm Rent', 'subtitle': 'Rent your gear', 'gear_to_rent': gear_to_rent},
        context_instance=RequestContext(request)
    )

def rented(request):
    if request.method == 'POST':
        form = RentForm(request.POST, request.FILES)
        if form.is_valid():
            # currently discard the note :(
            gear_id = form.cleaned_data['gear_id']
            gear_to_rent = GearItem.objects.get(id=gear_id)
            gear_to_rent.is_available = False
            gear_to_rent.save()
    else:
        return HttpResponseRedirect(reverse('GearSwap.views.list_all_gear'))


def search_categories(request, cat):
    gear_list = GearItem.objects.filter(type=cat)

    return render_to_response('GearSwap/search_list.html', {'title': 'Gear Surf', 'subtitle':'Get your gear on!', 'sidebar_title': 'Sidebar title here', 'sidebar_text': 'Sidebar text here', 'gear_list': gear_list}, context_instance=RequestContext(request))
