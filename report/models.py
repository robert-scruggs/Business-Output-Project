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
    finance_review = models.CharField(max_length=200)
    operating_company = models.CharField(max_length=200)
    parent_company = models.CharField( max_length=200)
    business_owners = models.CharField(max_length=200)
    primary_business_address = models.CharField(max_length=200)
    list_of_report_outcomes = models.CharField(max_length=200)
 
class TaxYears(models.Model):
    state = models.CharField(max_length=200)
    num_of_locations = models.CharField(max_length=200)
    total_sales = models.CharField(max_length=200)
    food_cost = models.CharField(max_length=200)
    labor_cost = models.CharField(max_length=200)
    admin_and_general = models.CharField(max_length=200)
    rands_marketing = models.CharField(max_length=200)
    income_before_fix_expense = models.CharField(max_length=200)
    property_tax = models.CharField(max_length=200)
    insurance = models.CharField(max_length=200)
    reserve = models.CharField(max_length=200)

class PersonalFinancialStatement(models.Model):
    cash = models.CharField(max_length=200)
    marketable_securities = models.CharField(max_length=200)
    total_liquid_assets = models.CharField(max_length=200)
    real_estate = models.CharField(max_length=200)
    primary_residence = models.CharField(max_length=200)
    total_real_estate = models.CharField(max_length=200)
    ira_401k = models.CharField(max_length=200)
    life_insurance = models.CharField(max_length=200)
    notes_receivable = models.CharField(max_length=200)
    business_values = models.CharField(max_length=200)
    automobiles = models.CharField(max_length=200)
    personal_property = models.CharField(max_length=200)
    total_other_assets = models.CharField(max_length=200)
    total_assets = models.CharField(max_length=200)
    primary_residence_re_mortgage = models.CharField(max_length=200)
    total_re_mortgage = models.CharField(max_length=200)
    notes_payable = models.CharField(max_length=200)
    installment_accounts = models.CharField(max_length=200)
    total_liabilities = models.CharField(max_length=200)
    net_worth = models.CharField(max_length=200)
    grand_total = models.CharField(max_length=200)

#class FinancialFlashReport(models.Model):
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    years_in_current_business = models.CharField(max_length=200)
    current_business_structure = models.CharField(max_length=200)
    