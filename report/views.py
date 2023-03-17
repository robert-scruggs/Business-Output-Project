import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .models import SearchLog
from .forms import BasicInformation, YearOne

# Create your views here.

def say_Hello(request):
    obj = SearchLog(url="www.google.com", iswp=True)
    obj.save()
    return HttpResponse("Hello")

#comes from forms.py 
def firstPage(request):
    form = BasicInformation()
    #somehow going from /templates/create.html to create.html makes this work
    return render(request, "create.html", {"form":form})

def yearOne(request):
    form = YearOne()

    return render(request, 'create.html', {"form" : form})
