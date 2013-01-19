# Create your views here.
from django.http import HttpResponse
from gearswap.models import GearItem

def index(request):
    gear_list = GearItem.objects.all()
    return render_to_response('it works')
    'return HttpResponse("It works")

