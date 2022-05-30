from threading import local
from django.shortcuts import render
from django.http import HttpResponse
from .models import Voiture
# Create your views here.
def index(request):
    automobiles = Voiture.objects.all()
    return render(request, 'index.html', {'automobiles': automobiles})



def page(request, id):
    automobiles = Voiture.objects.get(id=id)
    context = {'automobiles':automobiles}
    return render(request, 'page.html', context)

def pages(request):
    return render(request, 'page.html', local())


