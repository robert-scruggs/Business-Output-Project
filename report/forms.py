from django import forms

#class is inheriting from forms.Form
class BasicInformation(forms.Form):
    financeReview = forms.CharField(label="Proposed Project for Financing Review", max_length=200)
    operatingCompany = forms.CharField(label="Operating Company", max_length=200)
    parentComapny = forms.CharField(label="Parent Company", max_length=200)
    businessOwners = forms.CharField(label="Business Owners", max_length=200)
    primaryBusinessAddress = forms.CharField(label="Primary Business Address", max_length=200)
    listOfReportOutcomes = forms.CharField(label="Package will include", max_length=200)
    

class YearOne(forms.Form):
    area = forms.CharField(label="What state does your business operate out of", max_length=200)
    numOfLocations = forms.CharField(label="Please type number of locations for year 1", max_length=200)
    totalSales = forms.CharField(label="Total sales for year 1", max_length=200)
    foodCost = forms.CharField(label="Food Cost", max_length=200)
    laborCost = forms.CharField(label="Labor Cost", max_length=200)
    adminAndGeneral = forms.CharField(label="Administrative & General Costs", max_length=200)
    randsMarketing = forms.CharField(label="Royalty/Sales Marketing Costs", max_length=200)
    incomeBeforeFixExpense = forms.CharField(label="Income Before Fix Expense", max_length=200)
    propertyTax = forms.CharField(label="Property Tax", max_length=200)
    insurance = forms.CharField(label="Insurance", max_length=200)
    reserve = forms.CharField(label="Reserve", max_length=200)

