from django.shortcuts import render, redirect

from report import financialStatements
from .forms import BasicInformationForm, OperatingYearsForm1, OperatingYearsForm2, OperatingYearsForm3
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import * 
from django.core.files.base import ContentFile
import io
import time



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

# @login_required
# def taxYears(request):
#     form = TaxYearsForm()

    
#     if request.method == "POST":
#         form = TaxYearsForm(request.POST)
#         if form.is_valid():
#             my_object = form.save(commit=False)
#             my_object.user = request.user
#             my_object.save()
#             form.user = request.user.id
#             form.save()
#         return redirect("/success/")

#     return render(request, 'fourthPage.html', {"form" : form})

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

incomeTaxReturnFilesList = []
def incomeTaxReturnFiles(request):
    if request.method == 'POST':
        uploaded_file = request.FILES["file"]
        name = request.POST.get('name')
        incomeTaxReturnFilesList.append(uploaded_file)
        for file in incomeTaxReturnFilesList:
            print(file)
        
        file_contents = io.BytesIO(uploaded_file.read())
        user = request.user
        new_file = financial_flash_report_pdfs(user=user)
        new_file.file.save(file.name, ContentFile(file_contents.getvalue()))
        new_file.save()
        
    return render(request, 'uploadIncomeTaxReturns.html')

personalFinancialStatementFilesList = []
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

def report(request):

    context = {'title': 'Business Financing Review',
               'project' : 'Corner Bakery Cafe Franchise Locations (3)',
               'operating_company': 'Cutter Highlands Ranch LLC',
               'parent_company': 'Something IDK',
               'business_owners': 'Gerald and Whitney',
               'primary_business_address': 'ya mama lane',
               'locations': 'some locations around the world',
               'business_financing_needs_summary': '$50000000',
               'proposed_loan_needs': '$63435415413',
               'package_includes': 'something about what is inside the package',
               'year_one_locations': '1',
               'year_two_locations': '2',
               'year_three_locations': '3',
               'state': 'Colorado',
                'year_one_sales': '2281',
                'year_two_sales': '4813',
                'year_three_sales': '5053',
                'year_one_food_costs': '570',
                'year_two_food_costs': '1203',
                'year_three_food_costs': '1263',
                'year_one_labor_costs': '593',
                'year_two_labor_costs': '1251',
                'year_three_labor_costs': '1314',
                'year_one_total_costs': '1163',
                'year_two_total_costs': '2455',
                'year_three_total_costs': '2577',
                'year_one_ag_costs': '80',
                'year_two_ag_costs': '168',
                'year_three_ag_costs': '177',
                'year_one_rsm_costs': '114',
                'year_two_rsm_costs': '241',
                'year_three_rsm_costs': '253',
                'year_one_facilities_costs': '342',
                'year_two_facilities_costs': '722',
                'year_three_facilities_costs': '758',
                'year_one_total_other_operative_exp': '536',
                'year_two_total_other_operative_exp': '1131',
                'year_three_total_other_operative_exp': '1188',
                'year_one_total_operative_exp': '1699',
                'year_two_total_operative_exp': '3586',
                'year_three_total_operative_exp': '3765',
                'year_one_income_before_fix_expense': '582',
                'year_two_income_before_fix_expense': '1227',
                'year_three_income_before_fix_expense': '1289',
                'year_one_property_tax': '16',
                'year_two_property_tax': '26',
                'year_three_property_tax': '27',
                'year_one_insurance': '11',
                'year_two_insurance': '24',
                'year_three_insurance': '25',
                'year_one_reserve': '342',
                'year_two_reserve': '722',
                'year_three_reserve': '810',
                'year_one_net_income_before_interest_tax': '212',
                'year_two_net_income_before_interest_tax': '455',
                'year_three_net_income_before_interest_tax': '478',
                'owner': 'John Cutter',
                'cash': '25,000',
                'marketable_securities': '2,100,000',
                'total_liquid_assets': '2,125,000',
                'real_estate': '0',
                'primary_residence1': '900,000',
                'total_real_estate': '900,000',
                'other_assets': '0',
                'ira_401k': '0',
                'life_insurance': '0',
                'notes_receivable': '0',
                'business_values': '3,500,000',
                'automobiles': '50,000',
                'personal_property': '60,000',
                'total_other_assets': '3,610,000',
                'total_assets': '6,635,000',
                'primary_residence2': '339,000',
                'total_re_mortgage': '339,000',
                'accounts_payable': '0',
                'notes_payable': '0',
                'installment_accounts': '94,000',
                'total_liabilites': '433.000',
                'net_worth': '6,202,000',
                'overall_total': '6,635,000',

                

                }
    
    
    
    return render(request, 'report.html', context)

def finalReport(request):
    bi = BasicInformation.objects.all()
    oy1 = OperatingYears.objects.all()
    pfs = PersonalFinancialStatement.objects.all()
    ffr = FinancialFlashReport.objects.all()

    context = {
        'bi': bi,
        'oy1': oy1,
        'pfs': pfs,
        'ffr': ffr,
        'state': oy1[0].state
    }
    
    return render(request, 'practiceReport.html', context)
