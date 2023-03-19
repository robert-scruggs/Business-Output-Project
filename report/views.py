import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SearchLog
from .forms import BasicInformation, YearOne, YearTwo, YearThree

# Create your views here.
#basically methods that link up to the forms.py module and return instances of the html created
#in forms

#comes from forms.py 
def firstPage(request):
    form = BasicInformation()

    if request.method == "POST":
        return redirect("/yearOne/")
    #somehow going from /templates/create.html to create.html makes this work
    return render(request, "firstPage.html", {"form":form})

def yearOne(request):
    form = YearOne()

    if request.method == "POST":
        return redirect("/yearTwo/")

    return render(request, 'secondPage.html', {"form" : form})

def yearTwo(request):
    form = YearTwo()

    if request.method == "POST":
        return redirect("/yearThree/")

    return render(request, 'thirdPage.html', {"form" : form})

def yearThree(request):
    form = YearThree()

    if request.method == "POST":
        return redirect("/success/")

    return render(request, 'fourthPage.html', {"form" : form})

def success(request):
    return render(request,'success.html')

