import jinja2
import pdfkit

template = """
<html>
<head>
    <title>BUSINESS FINANCING REVIEW</title>
</head>
<body>
  <h1>{{ title }}</h1>
  <p> Proposed Project for financing reivew: <strong>{{project}}</strong> </p>
  <p> Operating Company: <strong>{{operating_company}}</strong></p>
  <p> Parent Company: <strong>{{parent_company}}</strong></p>
  <p> Business Owners: <strong>{{business_owners}}</strong></p>
  <p> Primary Business Address: <strong>{{primary_business_address}}</strong></p>
  <p> Locations: <strong>{{locations}}</strong></p>
  <p> Business Financing Needs Summary: <strong>{{business_financing_needs_summary}}</strong></p>
  <p> Proposed Loan Needs: <strong>{{proposed_loan_needs}}</strong></p>
  <p> Package Includes: <strong>{{package_includes}}</strong></p>
</body>
</html>
"""

data = {
    'title': 'BUSINESS FINANCING REVIEW',
    'project': 'project',
    'operating_company': 'operating company',
    'parent_company': 'operating company',
    'business_owners': 'operating company',
    'primary_business_address': 'operating company',
    'locations': 'operating company',
    'business_financing_needs_summary': 'operating company',
    'proposed_loan_needs': 'operating company',
    'package_includes': 'operating company',

}

rendered_template = jinja2.Template(template).render(data)


pdfkit.from_string(rendered_template, 'report.pdf')
