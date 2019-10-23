<!-- add-breadcrumbs -->
# Employee Tax Exemption Declaration

**Tax exemption is the monetary exemption of income, property or transactions from taxes that would otherwise be levied on an Employee.**

At the beginning of a Payroll Period, employees can declare the amount of exemption they will be claiming from their taxable salary. ERPNext allows you to specify tax exemption category/sub-category, tax exemption amount and other related information in the Employee Tax Exemption Declaration form.
 

To access Employee Tax Exemption Declaration, go to:

> Home > Human resources > Employee Tax and Benefits > Employee Tax Exemption Declaration 

## 1. How to create Employee Tax Exemption Declaration

To create a new Employee Tax Exemption Declaration:

1. Go to: Employee Tax Exemption Declaration > New.
1. Select the Exemption Sub Category and Exemption Category.
1. Enter the Maximum Exemption Amount and Declared Amount.
1. Save and Submit.

<img class="screenshot" alt="Employee Tax Exemption Declaration" src="{{docs_base_url}}/assets/img/human-resources/employee-tax-exemption-declaration.png">

The Total Exemption Amount will be exempted from annual taxable earnings of the employee while calculating the tax deductions in Payroll.

> Note: Employees can only submit one Employee Tax Exemption Declaration for a Payroll Period.

## 2. Features

### 2.1 HRA Exemption (Regional - India)

For the current fiscal year, in India, House Rent Allowance (HRA) exemption from taxable earnings is the minimum of:

* The actual amount allotted by the employer as the HRA.
* Actual rent paid less 10% of the basic salary.
* 50% of the basic salary, if the employee is staying in a metro city (40% for a non-metro city).

As part of the Employee Tax Exemption Declaration, employees can also fill out the HRA Exemption. ERPNext calculates the exemption eligible for HRA and exempts it while calculating the taxable earnings. 

Enter the Monthly House Rent and check the 'Rented in Metro City' checkbox if applicable and submit the form. The Annual and Monthly HRA Exemption will be automatically calculated.

Once the declaration is submitted, you can submit the proof of your tax exemption by clicking on the _Submit Proof_ button.


<img class="screenshot" alt="Employee Tax Exemption Declaration" src="{{docs_base_url}}/assets/img/human-resources/hra-exemption.png">

> Note: HRA component needs to be configured in Company master under HRS Settings sections for the HRA exemption to work.


## 3. Related Topics

1. [Employee Tax Exemption Proof Submission](/docs/user/manual/en/human-resources/employee-tax-exemption-proof-submission)
1. [Employee Benefit Application](/docs/user/manual/en/human-resources/employee-benefit-application)
1. [Employee Benefit Claim](/docs/user/manual/en/human-resources/employee-benefit-claim)

{next}
