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
    proposed_loan_needs = models.CharField(max_length=200)
    list_of_report_outcomes = models.TextField(max_length=40000)
 
class OperatingYears(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.CharField(max_length=200)
    num_of_locations = models.CharField(max_length=200)
    total_sales = models.CharField(max_length=200)
    food_cost = models.CharField(max_length=200)
    labor_cost = models.CharField(max_length=200)
    admin_and_general = models.CharField(max_length=200)
    rands_marketing = models.CharField(max_length=200)
    facilities = models.CharField(max_length=200)
    total_other_operative_expenses = models.CharField(max_length=200)
    total_operative_expenses = models.CharField(max_length=200)
    income_before_fix_expense = models.CharField(max_length=200)
    property_tax = models.CharField(max_length=200)
    insurance = models.CharField(max_length=200)
    reserve = models.CharField(max_length=200)
    total_fix_expenses = models.CharField(max_length=200)
    net_income_before_interest_and_tax = models.CharField(max_length=200)
    percentages = models.CharField(max_length=200)


class PersonalFinancialStatement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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

class FinancialFlashReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    years_in_current_business = models.CharField(max_length=200)
    current_business_structure = models.CharField(max_length=200)
    
class TaxYears(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_of_statement = models.CharField(max_length=200)
    marketable_securities = models.CharField(max_length=200)
    cash_from_sales = models.CharField(max_length=200)
    gross_cash_income = models.CharField(max_length=200)
    cash_operating_expenses = models.CharField(max_length=200)
    other_income = models.CharField(max_length=200)
    net_cash_after_operations = models.CharField(max_length=200)
    m1_net_deductions = models.CharField(max_length=200)
    m2_net_deductions = models.CharField(max_length=200)
    ending_cash_position = models.CharField(max_length=200)
    depreciation = models.CharField(max_length=200)
    amortization = models.CharField(max_length=200)
    interest = models.CharField(max_length=200)
    nre = models.CharField(max_length=200)
    owners_management_fees = models.CharField(max_length=200)
    cash_flow = models.CharField(max_length=200)
    operational_cash = models.CharField(max_length=200)
    available_cash = models.CharField(max_length=200)
    new_debt_services = models.CharField(max_length=200)
    surplus = models.CharField(max_length=200)
    coverage_ratio = models.CharField(max_length=200)
    financial_footnotes = models.CharField(max_length=200)

class Uploads(models.Model):
    name = models.CharField(max_length=255)
    data = models.BinaryField()

    