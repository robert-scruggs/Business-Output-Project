import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BasicInformationForm, TaxYearsForm, YearTwo, YearThree
from django.forms import ModelForm


# Create your views here.
#basically methods that link up to the forms.py module and return instances of the html created
#in forms

#think of these mfs as people who prepare the rooms
#like a specific maid to tend to a room 
#that maid knows how to do specific things that i have already taught them

#comes from forms.py 
def firstPage(request):
    form = BasicInformationForm()

    if request.method == "POST":
        form = BasicInformationForm(request.POST)

        if form.is_valid():
            f = form.cleaned_data["financeReview"]
            oc = form.cleaned_data['operatingCompany']
            pc = form.cleaned_data['parentCompany']
            bo = form.cleaned_data['businessOwners']
            pba = form.cleaned_data['primaryBusinessAddress']
            lro = form.cleaned_data['listOfReportOutcomes']
            form.save()
            print(f,oc,pc,bo,pba,lro)
            
        return redirect("/yearOne/")
    
    
    return render(request, "firstPage.html", {"form":form})

def yearOne(request):
    form = TaxYearsForm()

    if request.method == "POST":
        form = TaxYearsForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["state"]
            nol = form.cleaned_data['numOfLocations']
            ts = form.cleaned_data['totalSales']
            fc = form.cleaned_data['foodCost']
            lc = form.cleaned_data['laborCost']
            ag = form.cleaned_data['adminAndGeneral']
            rs = form.cleaned_data['randsMarketing']
            ibfe = form.cleaned_data['incomeBeforeFixExpense']
            pt = form.cleaned_data['propertyTax']
            insurance = form.cleaned_data['insurance']
            reserve = form.cleaned_data['reserve']
            form.save()
            print(a,nol,ts,fc,lc,ag,rs,ibfe,pt,insurance,reserve)
        return redirect("/yearTwo/")
    

    return render(request, 'secondPage.html', {"form" : form})

def yearTwo(request):
    form = YearTwo()

    if request.method == "POST":
        form = YearTwo(request.POST)
        if form.is_valid():
            f = form.cleaned_data["area"]
            print(f)
        return redirect("/yearThree/")

    return render(request, 'thirdPage.html', {"form" : form})

def yearThree(request):
    form = YearThree()

    if request.method == "POST":
        form = YearThree(request.POST)
        if form.is_valid():
            f = form.cleaned_data["area"]
            print(f)
        return redirect("/success/")

    return render(request, 'fourthPage.html', {"form" : form})

def success(request):
    return render(request,'success.html')

