import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BasicInformationForm, OperatingYearsForm1, OperatingYearsForm2, OperatingYearsForm3, TaxYearsForm, YearThree
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
            f = form.cleaned_data["finance_review"]
            oc = form.cleaned_data['operating_company']
            pc = form.cleaned_data['parent_company']
            bo = form.cleaned_data['business_owners']
            pba = form.cleaned_data['primary_business_address']
            lro = form.cleaned_data['list_of_report_outcomes']
            form.save()
            print(f,oc,pc,bo,pba,lro)
            
        return redirect("/yearOne/")
    
    
    return render(request, "firstPage.html", {"form":form})

def yearOne(request):
    form = OperatingYearsForm1()
    if request.method == "POST":
        form = OperatingYearsForm1(request.POST)
        if form.is_valid():
            a = form.cleaned_data["state"]
            nol = form.cleaned_data['num_of_locations']
            fc = form.cleaned_data['food_cost']
            lc = form.cleaned_data['labor_cost']
            ag = form.cleaned_data['admin_and_general']
            rs = form.cleaned_data['rands_marketing']
            pt = form.cleaned_data['property_tax']
            insurance = form.cleaned_data['insurance']
            reserve = form.cleaned_data['reserve']
            form.save()
            print(a,nol,fc,lc,ag,rs,pt,insurance,reserve)
        return redirect("/yearTwo/")
    

    return render(request, 'secondPage.html', {"form" : form})

def yearTwo(request):
    form = OperatingYearsForm2()

    if request.method == "POST":
        form = OperatingYearsForm2(request.POST)
        if form.is_valid():
            a = form.cleaned_data["state"]
            nol = form.cleaned_data['num_of_locations']
            fc = form.cleaned_data['food_cost']
            lc = form.cleaned_data['labor_cost']
            ag = form.cleaned_data['admin_and_general']
            rs = form.cleaned_data['rands_marketing']
            pt = form.cleaned_data['property_tax']
            insurance = form.cleaned_data['insurance']
            reserve = form.cleaned_data['reserve']
            form.save()
            print(a,nol,fc,lc,ag,rs,pt,insurance,reserve)
        return redirect("/yearThree/")

    return render(request, 'thirdPage.html', {"form" : form})

def yearThree(request):
    form = OperatingYearsForm3()

    if request.method == "POST":
        form = OperatingYearsForm3(request.POST)
        if form.is_valid():
            a = form.cleaned_data["state"]
            nol = form.cleaned_data['num_of_locations']
            fc = form.cleaned_data['food_cost']
            lc = form.cleaned_data['labor_cost']
            ag = form.cleaned_data['admin_and_general']
            rs = form.cleaned_data['rands_marketing']
            pt = form.cleaned_data['property_tax']
            insurance = form.cleaned_data['insurance']
            reserve = form.cleaned_data['reserve']
            form.save()
            print(a,nol,fc,lc,ag,rs,pt,insurance,reserve)
        return redirect("/success/")

    return render(request, 'fourthPage.html', {"form" : form})

def taxYears(request):

    form = TaxYearsForm()

    if request.method == "POST":
        form = TaxYearsForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["state"]
            nol = form.cleaned_data['num_of_locations']
            fc = form.cleaned_data['food_cost']
            lc = form.cleaned_data['labor_cost']
            ag = form.cleaned_data['admin_and_general']
            rs = form.cleaned_data['rands_marketing']
            pt = form.cleaned_data['property_tax']
            insurance = form.cleaned_data['insurance']
            reserve = form.cleaned_data['reserve']
            form.save()
            print(a,nol,fc,lc,ag,rs,pt,insurance,reserve)
        return redirect("/success/")

    return render(request, 'fourthPage.html', {"form" : form})



def success(request):
    return render(request,'success.html')

