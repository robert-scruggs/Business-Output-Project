from django.db import models

#populate models with data from the forms.py you fucking dumb idiot
# Create your models here.

#class BasicInformatio(models.Model):
    #financeReview = forms.CharField(label="Proposed Project for Financing Review", max_length=200)
    #operatingCompany = forms.CharField(label="Operating Company", max_length=200)
    #parentComapny = forms.CharField(label="Parent Company", max_length=200)
    #businessOwners = forms.CharField(label="Business Owners", max_length=200)
    #primaryBusinessAddress = forms.CharField(label="Primary Business Address", max_length=200)
    #listOfReportOutcomes = forms.CharField(label="Package will include", max_length=200)

class BasicInformation(models.Model):
    financeReview = models.CharField(max_length=200)
    operatingCompany = models.CharField(max_length=200)
    parentCompany = models.CharField( max_length=200)
    businessOwners = models.CharField(max_length=200)
    primaryBusinessAddress = models.CharField(max_length=200)
    listOfReportOutcomes = models.CharField(max_length=200)
 
class TaxYears(models.Model):
    state = models.CharField(max_length=200)
    numOfLocations = models.CharField(max_length=200)
    totalSales = models.CharField(max_length=200)
    foodCost = models.CharField(max_length=200)
    laborCost = models.CharField(max_length=200)
    adminAndGeneral = models.CharField(max_length=200)
    randsMarketing = models.CharField(max_length=200)
    incomeBeforeFixExpense = models.CharField(max_length=200)
    propertyTax = models.CharField(max_length=200)
    insurance = models.CharField(max_length=200)
    reserve = models.CharField(max_length=200)