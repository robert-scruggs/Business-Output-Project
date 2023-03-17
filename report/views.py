import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from .models import SearchLog
from .forms import BasicInformation, YearOne, YearTwo, YearThree

# Create your views here.
#basically methods that link up to the forms.py module and return instances of the html created
#in forms

def say_Hello(request):
    obj = SearchLog(url="www.google.com", iswp=True)
    obj.save()
    return HttpResponse("Hello")

#comes from forms.py 
def firstPage(request):
    form = BasicInformation()

    if request.method == "POST":
        return redirect("/yearOne/")
    #somehow going from /templates/create.html to create.html makes this work
    return render(request, "create.html", {"form":form})

def yearOne(request):
    form = YearOne()

    return render(request, 'create.html', {"form" : form})

def yearTwo(request):
    form = YearTwo()

    return render(request, 'create.html', {"form" : form})

def yearThree(request):
    form = YearThree()

    return render(request, 'create.html', {"form" : form})