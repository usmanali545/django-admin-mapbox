from django.shortcuts import render
from . models import Poi
# Create your views here.
def home(request):
    poi = Poi.objects.filter(is_active=True)
    print(poi)
    return render(request, 'map.html', context= {'poi': poi})