<!-- add-breadcrumbs -->
# Company

**A company is a legal entity made up of an association of people for carrying on a commercial or industrial enterprise.**

In ERPNext, the first Company is created on completion of account creation. For each Company, you can set a domain as manufacturing, retail, or services depending on the nature of your business activity.

If you have more than one company, you can add them from:

> Home > Accounting > Company

## 1. How to create a new Company
1. Click on New.
1. Enter the name, abbreviation, and default currency for the company.
1. Save.

You can also attach a company logo and add a description for the company.

![Company Master](/docs/assets/img/setup/company-master.png)

### 1.1 Other Options when creating a company

* **Domain**: The domain of work the company is into. Eg: manufacturing, services, etc. Choose one when setting up your account.
* **Is Group**: If checked, this becomes a parent company.
* **Parent Company**: If this is a child company, set the parent from this field. If a parent company is set, the chart of accounts for new company will be created on basis of parent company.

### 1.2  Tree View
The tree view displays the overall structure of your companies.

<img class="screenshot" alt="Company Tree" src="{{docs_base_url}}/assets/img/accounts/company-tree.png">

Once you build a company tree, ERPNext will validate if the accounts of the child companies match the accounts in the parent company. All the accounts can be combined in a consolidated chart of accounts statement.

### 1.3 Chart of Accounts
On each Company, the master for Chart of Accounts is maintained separately. This allows you to maintain separate accounting for each company as per the legal requirements.

<img class="screenshot" alt="Company Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/company-coa.png">

ERPNext has localized Chart of Accounts readily available for some countries. When creating new Company, you can choose to setup Chart of Account for it from one of the following options.

* Standard Chart of Accounts
* Based on Existing Company's Chart of Account

<img class="screenshot" alt="Company Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/company-coa-2.png">

### 1.4 Defaults:
Within the Company master, you can set many of default values for masters and accounts. These default accounts will help you in the quick posting of accounting transactions, where the value for the account will be fetched from the Company master if provided. As soon as the company is created, a default Chart Of Accounts and Cost Center is automatically created.

The following defaults can be set for a company:

* Default Finance Book
* Default Letter Head
* Default Holiday List
* Standard Working Hours
* Default Terms and Conditions
* Country
* Tax ID
* Date of Establishment

## 2. Features
### 2.1 Monthly Sales Target
Numerical value in the currency you've set. Total monthly sales will be visible once transactions are made. Know more [here](/docs/user/manual/en/setting-up/setting-company-sales-goal).

### 2.2 Account Settings
Some of the following accounts will be set by default, others can be created. The accounts can be seen in the [Chart of Accounts](/docs/user/manual/en/accounts/chart-of-accounts).

* Default Bank Account
* Default Cash Account
* Default Receivable Account
* Round Off Account
* Round Off Cost Center
* Write Off Account
* Discount Allowed Account
* Discount Received Account
* Exchange Gain / Loss Account
* Unrealized Exchange Gain/Loss Account
* Default Payable Account
* Default Employee Advance Account
* Default Cost of Goods Sold Account
* Default Income Account
* Default Deferred Revenue Account
* Default Deferred Expense Account
* Default Payroll Payable Account
* Default Expense Claim Payable Account
* Default Cost Center
* Credit Limit
* Default Payment Terms Template

### 2.3 Stock Settings
Enable Perpetual Inventory - a method for managing inventory, know more [here](/docs/user/manual/en/stock/perpetual-inventory).

* Default Inventory Account
* Stock Adjustment Account
* Stock Received But Not Billed
* Expenses Included In Valuation

    ![Stock Settings in Company](/docs/assets/img/setup/company-stock-settings.png)

### 2.2 Fixed Asset Depreciation Settings
For managing fixed assets in a company, the following accounts are needed. Most of them will be created by default. They can be seen in the [Chart of Accounts](/docs/user/manual/en/accounts/chart-of-accounts).

* Accumulated Depreciation Account
* Depreciation Expense Account
* Series for Asset Depreciation Entry (Journal Entry)
* Expenses Included In Asset Valuation
* Gain/Loss Account on Asset Disposal
* Asset Depreciation Cost Center
* Capital Work In Progress Account
* Asset Received But Not Billed

    ![Fixed Asset Depreciation](/docs/assets/img/setup/company-asset-depreciation.png)

### 2.3 HRA Settings
House Rent Allowance settings for your company can be set here:

* Basic Component
* HRA Component
* Arrear Component

### 2.4 Bank Remittance Settings
For transferring money abroad, you can set the following details of your company:

* Client Code
* Product Code

### 2.5 Budget
Exception Budget Approver Role: The role selected here can bypass the set budget to approve expenses.

### 2.6 Company Info
For reference, the following details of your company can be saved in ERPNext:

* Date of Incorporation
* Phone No
* Fax
* Email
* Website
* Address
* Registration Details

> Note: When setting the address here, it is important to tick the 'Is Your Company Address' checkbox.

**For India**, different addresses can be added with different GSTIN numbers if the company has multiple locations. For example, if your company has an offices in Mumbai, Delhi, and Bangalore, you'll have to add different addresses with different GSTIN numbers.

On saving a company, the following details/actions will be visible in the dasboard:
![Company after Save](/docs/assets/img/setup/company-after-save.png)

{next}
