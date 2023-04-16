from django.shortcuts import render, redirect
from .forms import BasicInformationForm, OperatingYearsForm1, OperatingYearsForm2, OperatingYearsForm3, TaxYearsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
#basically methods that link up to the forms.py module and return instances of the html created
#in forms

#think of these mfs as people who prepare the rooms
#like a specific maid to tend to a room 
#that maid knows how to do specific things that i have already taught them

#comes from forms.py 
@login_required
def basicInformation(request):
    form = BasicInformationForm()
    
    if request.method == "POST":
        form = BasicInformationForm(request.POST)
        if form.is_valid():
            #this will be the signed in users id
            my_object = form.save(commit=False)
            my_object.user = request.user
            my_object.save()
            form.save()
        return redirect("/yearOne/")
    
    return render(request, "firstPage.html", {"form":form})

@login_required
def yearOne(request):
    form = OperatingYearsForm1()
    if request.method == "POST":
        form = OperatingYearsForm1(request.POST)
        if form.is_valid():
            my_object = form.save(commit=False)
            my_object.user = request.user
            my_object.save()
            form.user = request.user.id
            form.save()
        return redirect("/yearTwo/")
    

    return render(request, 'secondPage.html', {"form" : form})

@login_required
def yearTwo(request):
    form = OperatingYearsForm2()

    if request.method == "POST":
        form = OperatingYearsForm2(request.POST)
        if form.is_valid():
            my_object = form.save(commit=False)
            my_object.user = request.user
            my_object.save()
            form.user = request.user.id
            form.save()
        return redirect("/yearThree/")

    return render(request, 'thirdPage.html', {"form" : form})

@login_required
def yearThree(request):
    form = OperatingYearsForm3()

    
    if request.method == "POST":
        form = OperatingYearsForm3(request.POST)
        if form.is_valid():
            my_object = form.save(commit=False)
            my_object.user = request.user
            my_object.save()
            form.user = request.user.id
            form.save()
        return redirect("/files/")

    return render(request, 'fourthPage.html', {"form" : form})

@login_required
def taxYears(request):
    form = TaxYearsForm()

    
    if request.method == "POST":
        form = TaxYearsForm(request.POST)
        if form.is_valid():
            my_object = form.save(commit=False)
            my_object.user = request.user
            my_object.save()
            form.user = request.user.id
            form.save()
        return redirect("/success/")

    return render(request, 'fourthPage.html', {"form" : form})

@login_required
def success(request):
    return render(request,'success.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/basicInformation/")
        else:
            print("wrong information")
            
    # context = {'form':form}
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    
    form = UserCreationForm()
    context = {'form':form}
    return render(request, "register.html", context)
    
def logoutUser(request):
    logout(request)
    return redirect("/login")

filesList = []
def files(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        filesList.append(uploaded_file)
        print(filesList)
        
        #return render(request, 'success.html')
    return render(request, 'files.html')

