<!-- add-breadcrumbs -->
# Loan
> Introduced in Version 13

**Loan record is the loan account which contains all the information regarding a loan.**

Loan record acts as a loan account which contains all the applicant details, repayment schedule and repayment info. All the loan related documents like [Loan Disbursement](/docs/user/manual/en/loan-management/loan-disbursement), [Loan Repayment](/docs/user/manual/en/loan-management/loan-repayment), etc are linked to a Loan.

To access the Loan List list, go to:
> Home > Loan Management > Loan > Loan


<img class="screenshot" alt="Loan" src="{{docs_base_url}}/assets/img/loan-management/loan.png">

## 1. Prerequisites
Before creating and using a Loan , it is advised that you create the following first:

* [Loan Security Type](/docs/user/manual/en/loan-management/loan-security-type)
* [Loan Security](/docs/user/manual/en/loan-management/loan-security)
* [Loan Type](/docs/user/manual/en/loan-management/loan-type)
* [Loan Application](/docs/user/manual/en/loan-management/loan-application)
* [Loan Security Pledge](/docs/user/manual/en/loan-management/loan-security-pledge)

## 2. How to Create a Loan
* Go to Loan List, click on New.
* Select applicant type.
* Select the applicant.
* Select loan application if loan application is created against that applicant. All the details in loan application will be automatically fetched in the loan.
* Select Company
* Enter posting date
* If applicant type is Employee then check "Repay from Salary" if loan will be repaid from salary

<img class="screenshot" alt="Make Loan" src="{{docs_base_url}}/assets/img/loan-management/loan-details.png">

* Enter Loan Type. All the loan accounts, mode of payment and other loan details like whether the loan is a term loan or demand loan will be automatically fetched from the loan type master. If loan is a term loan repayment schedule will be auto generated on saving the loan document.

<img class="screenshot" alt="Make Loan" src="{{docs_base_url}}/assets/img/loan-management/loan-accounts.png">

<img class="screenshot" alt="Make Loan" src="{{docs_base_url}}/assets/img/loan-management/loan-repayment-schedule.png">


* Check is secured loan if the loan is a secured loan. Also select Loan Security Pledge if the loan is a secured loan
* Click "Save" to save the draft of the Loan.
* Click "Submit" to submit the Loan Security Pledge.
* Once the Loan is submitted the loan amount is ready to be disbursed



### 2.1. Other ways to create a Loan
1. You can also create a Loan from a approved Loan Application via the Create button on the top right

<img class="screenshot" alt="Loan Application" src="{{docs_base_url}}/assets/img/loan-management/create-loan.png">

## 3. Features

### 3.1 Creation Of Disbursement Entry
After submitting the Loan document, if the status is "Sanctioned" and "Repay from Salary" is unchecked, you can create [Loan Disbursement](/docs/user/manual/en/loan-management/loan-disbursement) from the loan document via Create button on top right.

<img class="screenshot" alt="Create Loan Disbursement" src="{{docs_base_url}}/assets/img/loan-management/create-loan-disbursement.png">

### 3.2 Creation Of Repayment Entry
If the loan is fully or partially disbursed and "Repay from Salary" is unchecked, you can create a [Loan Repayment](/docs/user/manual/en/loan-management/loan-repayment) from the loan document via Create button on top right.

<img class="screenshot" alt="Create Loan Repayment" src="{{docs_base_url}}/assets/img/loan-management/create-loan-repayment.png">

### 3.3 Loan Repayment Deduction from salary
To auto deduct the Loan repayment from Salary, check "Repay from Salary" in Loan. It will appear as Loan Repayment in Salary Slip and a [Loan Repayment](/docs/user/manual/en/loan-management/loan-repayment) record will also be automatically created for the same .

<img class="screenshot" alt="Salary Slip Loan" src="{{docs_base_url}}/assets/img/loan-management/salary-slip-loan.png">

{next}




