from django.db import models
from django.contrib.auth.models import User


#populate models with data from the forms.py you fucking dumb idiot
# Create your models here.

class BasicInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    finance_review = models.CharField(max_length=200)
    operating_company = models.CharField(max_length=200)
    parent_company = models.CharField( max_length=200)
    business_owners = models.CharField(max_length=200)
    primary_business_address = models.CharField(max_length=200)
    proposed_loan_needs = models.IntegerField()
    list_of_report_outcomes = models.TextField(max_length=40000)
 
class OperatingYears(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.CharField(max_length=200)
    num_of_locations = models.IntegerField()
    total_sales = models.IntegerField()
    food_cost = models.IntegerField()
    labor_cost = models.IntegerField()
    total_cost_of_goods_sold = models.IntegerField(default=0)
    admin_and_general = models.IntegerField()
    rands_marketing = models.IntegerField()
    facilities = models.IntegerField()
    total_other_operative_expenses = models.IntegerField(default=0)
    total_operative_expenses = models.IntegerField(default=0)
    income_before_fix_expense = models.IntegerField(default=0)
    property_tax = models.IntegerField()
    insurance = models.IntegerField()
    reserve = models.IntegerField()
    total_fix_expenses = models.IntegerField(default=0)
    net_income_before_interest_and_tax = models.IntegerField(default=0)
    percentages = models.IntegerField(default=0)


class PersonalFinancialStatement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cash = models.IntegerField()
    marketable_securities = models.IntegerField()
    total_liquid_assets = models.IntegerField()
    real_estate = models.IntegerField()
    primary_residence = models.IntegerField()
    total_real_estate = models.IntegerField()
    ira_401k = models.IntegerField()
    life_insurance = models.IntegerField()
    notes_receivable = models.IntegerField()
    business_values = models.IntegerField()
    automobiles = models.IntegerField()
    personal_property = models.IntegerField()
    total_other_assets = models.IntegerField()
    total_assets = models.IntegerField()
    primary_residence_re_mortgage = models.IntegerField()
    total_re_mortgage = models.IntegerField()
    notes_payable = models.IntegerField()
    installment_accounts = models.IntegerField()
    total_liabilities = models.IntegerField()
    net_worth = models.IntegerField()
    grand_total = models.IntegerField()

class FinancialFlashReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    years_in_current_business = models.IntegerField()
    current_business_structure = models.CharField(max_length=200)
    
class TaxYears(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_of_statement = models.CharField(max_length=200)
    marketable_securities = models.IntegerField()
    cash_from_sales = models.IntegerField()
    gross_cash_income = models.IntegerField()
    cash_operating_expenses = models.IntegerField()
    other_income = models.IntegerField()
    net_cash_after_operations = models.IntegerField()
    m1_net_deductions = models.IntegerField()
    m2_net_deductions = models.IntegerField()
    ending_cash_position = models.IntegerField()
    depreciation = models.IntegerField()
    amortization = models.IntegerField()
    interest = models.IntegerField()
    nre = models.IntegerField()
    owners_management_fees = models.IntegerField()
    cash_flow = models.IntegerField()
    operational_cash = models.IntegerField()
    available_cash = models.IntegerField()
    new_debt_services = models.IntegerField()
    surplus = models.IntegerField()
    coverage_ratio = models.IntegerField()
    financial_footnotes = models.IntegerField()

class Uploads(models.Model):
    name = models.CharField(max_length=255)
    data = models.BinaryField()

    