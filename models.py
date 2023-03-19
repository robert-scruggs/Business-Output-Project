# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BasicInformation(models.Model):
    idfirst_page = models.AutoField(primary_key=True)
    operating_compnay = models.CharField(max_length=45, blank=True, null=True)
    parent_company = models.CharField(max_length=45, blank=True, null=True)
    business_owners = models.CharField(max_length=45, blank=True, null=True)
    primary_business_address = models.CharField(max_length=45, blank=True, null=True)
    locations = models.CharField(max_length=45, blank=True, null=True)
    business_financing_needs_summary = models.CharField(max_length=45, blank=True, null=True)
    proposed_loan_needs = models.CharField(max_length=45, blank=True, null=True)
    package_includes = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basic_information'


class FinancialFlashReport(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    owner_name = models.CharField(max_length=45, blank=True, null=True)
    years_in_current_business = models.CharField(max_length=45, blank=True, null=True)
    current_business_structure = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financial_flash_report'


class OperatingYears(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    field_of_locations = models.CharField(db_column='#_of_locations', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    area_state = models.CharField(max_length=45, blank=True, null=True)
    operating_yearscol = models.CharField(max_length=45, blank=True, null=True)
    sales = models.CharField(max_length=45, blank=True, null=True)
    food_costs = models.CharField(max_length=45, blank=True, null=True)
    labor_costs = models.CharField(max_length=45, blank=True, null=True)
    total_cost_of_goods_sold = models.CharField(max_length=45, blank=True, null=True)
    admin_and_general = models.CharField(max_length=45, blank=True, null=True)
    royalty_and_sales = models.CharField(max_length=45, blank=True, null=True)
    facilities = models.CharField(max_length=45, blank=True, null=True)
    total_other_operative_exp = models.CharField(max_length=45, blank=True, null=True)
    total_operative_exp = models.CharField(max_length=45, blank=True, null=True)
    incomes_before_fix_expense = models.CharField(max_length=45, blank=True, null=True)
    property_tax = models.CharField(max_length=45, blank=True, null=True)
    insurance = models.CharField(max_length=45, blank=True, null=True)
    reserve = models.CharField(max_length=45, blank=True, null=True)
    total_fix_expense = models.CharField(max_length=45, blank=True, null=True)
    net_income_before_interest_and_tax = models.CharField(max_length=45, blank=True, null=True)
    percentages = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operating_years'


class PersonalFinancialStatement(models.Model):
    id = models.AutoField(primary_key=True)
    cash = models.CharField(max_length=45, blank=True, null=True)
    marketable_securities = models.CharField(max_length=45, blank=True, null=True)
    total_liquid_assets = models.CharField(max_length=45, blank=True, null=True)
    real_estate = models.CharField(max_length=45, blank=True, null=True)
    primary_residence = models.CharField(max_length=45, blank=True, null=True)
    total_real_estate = models.CharField(max_length=45, blank=True, null=True)
    ira_401k = models.CharField(max_length=45, blank=True, null=True)
    life_insurance = models.CharField(max_length=45, blank=True, null=True)
    notes_receivable = models.CharField(max_length=45, blank=True, null=True)
    business_values = models.CharField(max_length=45, blank=True, null=True)
    automobiles = models.CharField(max_length=45, blank=True, null=True)
    personal_property = models.CharField(max_length=45, blank=True, null=True)
    total_other_assets = models.CharField(max_length=45, blank=True, null=True)
    total_assets = models.CharField(max_length=45, blank=True, null=True)
    primary_residence_re_mortgage = models.CharField(max_length=45, blank=True, null=True)
    total_re_mortgage = models.CharField(max_length=45, blank=True, null=True)
    notes_payable = models.CharField(max_length=45, blank=True, null=True)
    installment_accounts = models.CharField(max_length=45, blank=True, null=True)
    total_liabilites = models.CharField(max_length=45, blank=True, null=True)
    net_worth = models.CharField(max_length=45, blank=True, null=True)
    grand_total = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_financial_statement'


class TaxYears(models.Model):
    id = models.AutoField(primary_key=True)
    date_of_statement = models.CharField(max_length=45, blank=True, null=True)
    cash_from_sales = models.CharField(max_length=45, blank=True, null=True)
    gross_cash_income = models.CharField(max_length=45, blank=True, null=True)
    cash_operating_expenses = models.CharField(max_length=45, blank=True, null=True)
    other_income = models.CharField(max_length=45, blank=True, null=True)
    net_cash_after_operations = models.CharField(max_length=45, blank=True, null=True)
    m1_net_deductions = models.CharField(max_length=45, blank=True, null=True)
    m2_net_deductions = models.CharField(max_length=45, blank=True, null=True)
    ending_cash_position = models.CharField(max_length=45, blank=True, null=True)
    depreciation = models.CharField(max_length=45, blank=True, null=True)
    amortization = models.CharField(max_length=45, blank=True, null=True)
    interest = models.CharField(max_length=45, blank=True, null=True)
    nre = models.CharField(max_length=45, blank=True, null=True)
    owners_management_fees = models.CharField(max_length=45, blank=True, null=True)
    cash_flow = models.CharField(max_length=45, blank=True, null=True)
    operational_cash = models.CharField(max_length=45, blank=True, null=True)
    available_cash = models.CharField(max_length=45, blank=True, null=True)
    new_debt_service = models.CharField(max_length=45, blank=True, null=True)
    surplus = models.CharField(max_length=45, blank=True, null=True)
    coverage_ratio = models.CharField(max_length=45, blank=True, null=True)
    financial_footnotes = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_years'


class Uploads(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    files = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploads'
