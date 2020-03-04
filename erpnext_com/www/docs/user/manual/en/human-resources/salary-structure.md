<!-- add-breadcrumbs -->
# Salary Structure

**Salary Structure is the details of the salary being offered to an Employee, in terms of the breakup of the different components constituting the compensation.**

Any changes to the Salary Structure i.e. among the components can have a major impact on what the Employee does, such as the kind of tax exemptions claimed.

ERPNext allows you to define the Earning and Deductions of a Salary Structure, Payroll frequency and Payment Mode among other features.

To access Salary Structure, go to:
> Home > Human Resources > Payroll > Salary Structure

## 1. How to create a Salary Structure

To create a new Salary Structure:

1. Go to Salary Structure, click on New.
2. Enter the Salary Structure Name.
3. Select the Company Name and Payroll Frequency.
3. Save and Submit.


## 2. Features

Apart from the mandatory fields, the other important fields of a Salary Structure are Earnings and Deductions which form the basis of the Salary Structure among others. They are explained below:

### 2.1 Earning and Deduction

Earnings specify the Salary Components that are earned by an Employee. These components typically include basic, allowances, bonuses and incentives that are added to the employee's Total Salary. On the other hand, Deductions specify the Salary Components that are deducted from the employee's Total Salary. These typically include the taxes.


To create Earnings and Deductions, select the Salary Component in the Component column. Enter the Formula/Condition if not previously specified while creating the [Salary Component](/docs/user/manual/en/human-resources/salary-component). Additionally, you can also enter a pre-defined amount in the Amount column.



<img class="screenshot" alt="Salary Structure" src="{{docs_base_url}}/assets/img/human-resources/salary-structure.png">


> Note: Make sure to click on the downward arrow and enable the 'Amount based on formula' checkbox in case the Salary Component is calculated using a formula.


### 2.2 Account

In this section, the Mode of Payment and the Payment Account that is used to pay the salary can be specified.

### 2.3 Salary Structure for Salary based on Timesheets

In ERPNext you can also define the Salary Structure for Salary Slip based on Timesheet, which allows the Company to pay there Employee as per working hours.

Steps for creating such Salary Structure:

1. Go to Salary Structure List, click on New.
1. Select checkbox **Salary Slip based on Timesheet**.
1. Fill Salary Component, this component is for Timesheet based payroll.
1. Fill Hour Rate, the amount for Working hours will be calculated accordingly.
1. Save and Submit.

<img class="screenshot" alt="Create Salary Slip based on Timesheets" src="{{docs_base_url}}/assets/img/human-resources/salary-structure-for-salary-based-on-timesheets.png">

### 2.4 Additional Features

Some of the additional features provided in the Salary Structure doctype are:

* Leave Encashment Amount Per Day
* Max Benefits (Amount)

Once all the information is saved and submitted, you can assign the Salary Structure to an Employee either through the **Assign Salary Structure** button or by creating a new [Salary Structure Assignment](/docs/user/manual/en/human-resources/salary-structure-assignment) through the dashboard.

You can also assign the created Salary Structure to several employees based on the Employee Grade, Department, Designation, etc. through the 'Assign to Employees' button.
Additionally, Salary Slip can also be directly created through the dashboard.

## 3. Related Topics

1. [Salary Component](/docs/user/manual/en/human-resources/salary-component)
1. [Salary Structure Assignment](/docs/user/manual/en/human-resources/salary-structure-assignment)
1. [Employee Grade](/docs/user/manual/en/human-resources/employee-grade)
1. [Payroll Entry](/docs/user/manual/en/human-resources/payroll-entry)
