from django import forms
from django.forms import ModelForm
from .models import BasicInformation, TaxYears


#this is basically your html
#this is what your maids will use to decorate the rooms

#class is inheriting from forms.Form
#class BasicInformation(forms.Form):
#    financeReview = forms.CharField(label="Proposed Project for Financing Review", max_length=200)
#    operatingCompany = forms.CharField(label="Operating Company", max_length=200)
#    parentComapny = forms.CharField(label="Parent Company", max_length=200)
#    businessOwners = forms.CharField(label="Business Owners", max_length=200)
#    primaryBusinessAddress = forms.CharField(label="Primary Business Address", max_length=200)
#    listOfReportOutcomes = forms.CharField(label="Package will include", max_length=200)

class BasicInformationForm(ModelForm):
    finance_review = forms.CharField(max_length=255, label="What is the name of the proposed project for financing review?")
    operating_company = forms.CharField(max_length=255, label="Operating Company")
    parent_company = forms.CharField(max_length=255, label="Parent Company")
    business_owners = forms.CharField(max_length=255, label="Business Owners", help_text="(Separate business owners with commas)")
    primary_business_address = forms.CharField(max_length=255, label="Primary Business Address")
    list_of_report_outcomes = forms.CharField(max_length=255, label="List of Report Outcomes")
    class Meta:
        model = BasicInformation
        fields = ['finance_review','operating_company', 'parent_company', 'business_owners', 'primary_business_address','list_of_report_outcomes']
        


class TaxYearsForm(ModelForm):
    state = forms.TextInput()
    num_of_locations = forms.TextInput()
    total_sales = forms.TextInput()
    food_cost = forms.TextInput()
    labor_cost = forms.TextInput()
    admin_and_general = forms.TextInput()
    rands_marketing = forms.TextInput()
    income_before_fix_expense = forms.TextInput()
    property_tax = forms.TextInput()
    insurance = forms.TextInput()
    reserve = forms.TextInput()
    class Meta:
        model = TaxYears
        fields = ['state','num_of_locations', 'total_sales', 'food_cost', 'labor_cost','admin_and_general', 'rands_marketing', 'income_before_fix_expense', 'property_tax','insurance','reserve']    

class YearTwo(forms.Form):
    area = forms.CharField(label="What state does your business operate out of", max_length=200)
    numOfLocations = forms.CharField(label="Please type number of locations for year 2", max_length=200)
    totalSales = forms.CharField(label="Total sales for year 2", max_length=200)
    foodCost = forms.CharField(label="Food Cost", max_length=200)
    laborCost = forms.CharField(label="Labor Cost", max_length=200)
    adminAndGeneral = forms.CharField(label="Administrative & General Costs", max_length=200)
    randsMarketing = forms.CharField(label="Royalty/Sales Marketing Costs", max_length=200)
    incomeBeforeFixExpense = forms.CharField(label="Income Before Fix Expense", max_length=200)
    propertyTax = forms.CharField(label="Property Tax", max_length=200)
    insurance = forms.CharField(label="Insurance", max_length=200)
    reserve = forms.CharField(label="Reserve", max_length=200)
    


class YearThree(forms.Form):
    area = forms.CharField(label="What state does your business operate out of", max_length=200)
    numOfLocations = forms.CharField(label="Please type number of locations for year 3", max_length=200)
    totalSales = forms.CharField(label="Total sales for year 3", max_length=200)
    foodCost = forms.CharField(label="Food Cost", max_length=200)
    laborCost = forms.CharField(label="Labor Cost", max_length=200)
    adminAndGeneral = forms.CharField(label="Administrative & General Costs", max_length=200)
    randsMarketing = forms.CharField(label="Royalty/Sales Marketing Costs", max_length=200)
    incomeBeforeFixExpense = forms.CharField(label="Income Before Fix Expense", max_length=200)
    propertyTax = forms.CharField(label="Property Tax", max_length=200)
    insurance = forms.CharField(label="Insurance", max_length=200)
    reserve = forms.CharField(label="Reserve", max_length=200)


