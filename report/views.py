from django.shortcuts import render, redirect

from report import financialStatements
from report import financialFlashReports
from .forms import BasicInformationForm, OperatingYearsForm1, OperatingYearsForm2, OperatingYearsForm3
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import * 
from django.core.files.base import ContentFile
import io
from django.http import JsonResponse
import json



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
            form.save()
            form.user = request.user.id
            #extra values that need to be saved
            total_cost_of_goods_sold_value = int(form.cleaned_data['food_cost']) + int(form.cleaned_data['labor_cost'])
            total_other_operative_expense_value = int(form.cleaned_data['admin_and_general']) + int(form.cleaned_data['rands_marketing']) + int(form.cleaned_data['facilities'])
            total_operative_expense_value = total_cost_of_goods_sold_value + total_other_operative_expense_value
            income_before_fix_expense_value = int(form.cleaned_data['total_sales']) - total_operative_expense_value
            total_fix_expense_value = int(form.cleaned_data['property_tax']) + int(form.cleaned_data['insurance']) + int(form.cleaned_data['reserve'])
            net_income_value = income_before_fix_expense_value - total_fix_expense_value
            #this is getting the first row of operating years for the specific user
            tcogsDB = OperatingYears.objects.filter(user_id = form.user).all()[0]
            tcogsDB.total_cost_of_goods_sold = total_cost_of_goods_sold_value
            tcogsDB.total_other_operative_expenses = total_other_operative_expense_value
            tcogsDB.total_operative_expenses = total_operative_expense_value
            tcogsDB.income_before_fix_expense = income_before_fix_expense_value
            tcogsDB.total_fix_expenses = total_fix_expense_value
            tcogsDB.net_income_before_interest_and_tax = net_income_value
            #saves extra data to database
            tcogsDB.save()
            print(total_cost_of_goods_sold_value, total_other_operative_expense_value, total_operative_expense_value, income_before_fix_expense_value,total_fix_expense_value,net_income_value)
            # idk = OperatingYears.objects.filter(user_id=form.user).all()[:3]
            # for data in idk:
            #     print(data.property_tax)
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
            #
            total_cost_of_goods_sold_value = int(form.cleaned_data['food_cost']) + int(form.cleaned_data['labor_cost'])
            total_other_operative_expense_value = int(form.cleaned_data['admin_and_general']) + int(form.cleaned_data['rands_marketing']) + int(form.cleaned_data['facilities'])
            total_operative_expense_value = total_cost_of_goods_sold_value + total_other_operative_expense_value
            income_before_fix_expense_value = int(form.cleaned_data['total_sales']) - total_operative_expense_value
            total_fix_expense_value = int(form.cleaned_data['property_tax']) + int(form.cleaned_data['insurance']) + int(form.cleaned_data['reserve'])
            net_income_value = income_before_fix_expense_value - total_fix_expense_value
            #this is getting the first row of operating years for the specific user
            tcogsDB = OperatingYears.objects.filter(user_id = form.user).all()[1]
            tcogsDB.total_cost_of_goods_sold = total_cost_of_goods_sold_value
            tcogsDB.total_other_operative_expenses = total_other_operative_expense_value
            tcogsDB.total_operative_expenses = total_operative_expense_value
            tcogsDB.income_before_fix_expense = income_before_fix_expense_value
            tcogsDB.total_fix_expenses = total_fix_expense_value
            tcogsDB.net_income_before_interest_and_tax = net_income_value
            #saves extra data to database
            tcogsDB.save()
            print(total_cost_of_goods_sold_value, total_other_operative_expense_value, total_operative_expense_value, income_before_fix_expense_value,total_fix_expense_value,net_income_value)
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
            total_cost_of_goods_sold_value = int(form.cleaned_data['food_cost']) + int(form.cleaned_data['labor_cost'])
            total_other_operative_expense_value = int(form.cleaned_data['admin_and_general']) + int(form.cleaned_data['rands_marketing']) + int(form.cleaned_data['facilities'])
            total_operative_expense_value = total_cost_of_goods_sold_value + total_other_operative_expense_value
            income_before_fix_expense_value = int(form.cleaned_data['total_sales']) - total_operative_expense_value
            total_fix_expense_value = int(form.cleaned_data['property_tax']) + int(form.cleaned_data['insurance']) + int(form.cleaned_data['reserve'])
            net_income_value = income_before_fix_expense_value - total_fix_expense_value
            #this is getting the first row of operating years for the specific user
            tcogsDB = OperatingYears.objects.filter(user_id = form.user).all()[2]
            tcogsDB.total_cost_of_goods_sold = total_cost_of_goods_sold_value
            tcogsDB.total_other_operative_expenses = total_other_operative_expense_value
            tcogsDB.total_operative_expenses = total_operative_expense_value
            tcogsDB.income_before_fix_expense = income_before_fix_expense_value
            tcogsDB.total_fix_expenses = total_fix_expense_value
            tcogsDB.net_income_before_interest_and_tax = net_income_value
            #saves extra data to database
            tcogsDB.save()
            print(total_cost_of_goods_sold_value, total_other_operative_expense_value, total_operative_expense_value, income_before_fix_expense_value,total_fix_expense_value,net_income_value)
        return redirect("/personalFinancialStatementFiles/")

    return render(request, 'fourthPage.html', {"form" : form})

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

@login_required    
def logoutUser(request):
    logout(request)
    return redirect("/login")

incomeTaxReturnFilesList = []
businessID = [0]
@login_required
def incomeTaxReturnFiles(request):
    user = request.user
    ffr = FinancialFlashReport.objects.filter(user_id=user)
    # max_id = ffr.latest('business_id').business_id

    if request.method == 'POST':
        # data = json.loads(request.body)
        uploaded_files = request.FILES.getlist("files")
        # nre_list = data.get('nreList')
        # management_fees_list = data.get('managementFeesList')

        # for x in nre_list:
        #     print(x)
        # for x in management_fees_list:
        #     print
            

        businessName = request.POST.get('businessName')
        address = request.POST.get('address')
        owners = request.POST.get('owners')
        yearsInBusiness = request.POST.get('yearsInBusiness')
        
        for file in uploaded_files:
            incomeTaxReturnFilesList.append(file)
            file_contents = io.BytesIO(file.read())
            new_file = FinancialFlashReport(user=user,business_id=businessID[0])
            new_file.file.save(file.name, ContentFile(file_contents.getvalue()))
            new_file.save()
            print(file)
        
        businessID[0] = businessID[0] + 1
    
        # for id in range(max_id + 1):
        #     files = ffr.filter(business_id=id)

        #     for currUser in files:
        #         currFile = currUser.file
        #         currUser.company_name = businessName
        #         currUser.address = address
        #         currUser.owner_name = owners
        #         currUser.years_in_current_business = yearsInBusiness
        
        
    context = {
        'ffr':ffr
    }

    return render(request, 'uploadIncomeTaxReturns.html',context)

personalFinancialStatementFilesList = []
@login_required
def personalFinancialStatementFiles(request):
    user = request.user
    pfs = PersonalFinancialStatement.objects.filter(user_id=user) 
    
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')
        for file in uploaded_files:
            personalFinancialStatementFilesList.append(file)
            file_contents = io.BytesIO(file.read())
            new_file = PersonalFinancialStatement(user=user)
            new_file.file.save(file.name, ContentFile(file_contents.getvalue()))
            new_file.save()

        for person in pfs:
            file = person.file
            person.cash_on_hand = financialStatements.getCashOnHand(file)
            person.savings_account = financialStatements.getSavingsAccount(file)
            person.cash = financialStatements.getCash(file)
            person.marketable_securities = financialStatements.getMarketableSecurities(file)
            person.total_liquid_assets = financialStatements.getTotalLiquidAssets(file)
            person.primary_residence = financialStatements.getPrimaryResidence(file)
            person.ira_401k = financialStatements.getIRA(file)
            person.life_insurance = financialStatements.getLifeInsurance(file)
            person.notes_receivable = financialStatements.getNotesReceivable(file)
            person.business_values = financialStatements.getBusinessValues(file)
            person.automobiles = financialStatements.getAutomobiles(file)
            person.personal_property = financialStatements.getPersonalProperty(file)
            person.total_other_assets = financialStatements.getTotalOtherAssets(file)
            person.total_assets = financialStatements.getTotalAssets(file)
            person.total_re_mortgage = financialStatements.getTotalREMortgage(file)
            person.accounts_payable = financialStatements.getAccountsPayable(file)
            person.notes_payable = financialStatements.getNotesPayable(file)
            person.installment_accounts_auto = financialStatements.getInstallmentAccountsAuto(file)
            person.installment_accounts_other = financialStatements.getInstallmentAccountsOther(file)
            person.installment_accounts = financialStatements.getInstallmentAccounts(file)
            person.total_liabilities = financialStatements.getTotalLiabilities(file)
            person.net_worth = financialStatements.getNetWorth(file)
            person.grand_total = financialStatements.getAbsoluteTotal(file)
            person.save()
    context = {
        'pfs':pfs
    }
    return render(request, 'uploadFinancialStatements.html', context)
 

@login_required
def finalReport(request):
    #resets businessID back to zero since it will be used globally, yes i know its bad code but i must continue i fear
    businessID[0] = 0
    user = request.user
    ffr = FinancialFlashReport.objects.filter(user_id=user)
    max_id = ffr.latest('business_id').business_id

    #these names are confusing as hell but keep up please
    # for id in range(max_id + 1):
    #     files = ffr.filter(business_id=id)

    #     for currUser in files:
    #         currFile = currUser.file
    #         currUser.cash_from_sales = financialFlashReports.getCashFromSales(currFile)
    #         currUser.gross_cash_income = financialFlashReports.getGrossCashIncome(currFile)
    #         currUser.cash_operating_expenses = financialFlashReports.getCashOperatingExpenses(currFile)
    #         currUser.other_income = financialFlashReports.getOtherIncomeExpenses(currFile)
    #         currUser.net_cash_after_operations = financialFlashReports.getNetCashAfterOperations(currFile)
    #         currUser.m1_net_deductions = financialFlashReports.getM1Deductions(currFile)
    #         currUser.m2_net_deductions = financialFlashReports.getM2Deductions(currFile)
    #         currUser.ending_cash_position = financialFlashReports.getEndingCashPosition(currFile)
    #         currUser.depreciation = financialFlashReports.getDepreciation(currFile)
    #         currUser.amortization = financialFlashReports.getAmortization(currFile)
    #         currUser.interest = financialFlashReports.getInterest(currFile)
    #         currUser.nre = 0
    #         currUser.owners_management_fees = 0
    #         currUser.cash_flow = financialFlashReports.getCashFlow(currFile)
    #         currUser.operational_cash = financialFlashReports.getCashFlow(currFile)
    #         currUser.available_cash = financialFlashReports.getCashFlow(currFile)
    #         currUser.new_debt_services = 0
    #         currUser.surplus = financialFlashReports.getCashFlow(currFile)
    #         currUser.coverage_ratio = 0
    #         currUser.financial_footnotes = "empty"
    #         currUser.save()

    bi = BasicInformation.objects.all()
    oy1 = OperatingYears.objects.all()
    pfs = PersonalFinancialStatement.objects.all()
    ffr = FinancialFlashReport.objects.all()

    context = {
        'bi': bi,
        'oy1': oy1,
        'pfs': pfs,
        'ffr': ffr,
        'state': oy1[0].state,
    }
    
    return render(request, 'practiceReport.html', context)
