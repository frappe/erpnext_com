# Process Deferred Accounting

**Process Deferred Accounting is a log which is created on every deferred revenue or expense processing**

Process Deferred Accounting record is automatically created on deferred revenue or expense booking through a background job and the user can also create a record for manual deferred expense or revenue booking.

To access the Process Deferred Accounting list, go to:
> Home > Accounting > General Ledger > Process Deferred Accounting 

## 1. Prerequisites
Before creating and using a Process Deferred Accounting, it is advised to understand the following first:

* [Deferred Revenue](/docs/user/manual/en/accounts/deferred-revenue)
* [Deferred Income](/docs/user/manual/en/accounts/deferred-expense)


## 2. How to create a Process Deferred Accounting
1. Go to Process Deferred Accounting list, click on New.
1. Enter Company.
1. Select the type of deferred accounting process. Select 'Income' for booking deferred revenue or select 'Expense' for booking deferred expense
1. Expand the posting date.
1. Enter service start date and service end date. 
1. Save and Submit.

<img class="screenshot" alt="Process Deferred Revenue" src="{{docs_base_url}}/assets/img/accounts/process-deferred-accounting.png">

## 3. Features

### 3.1 On Submitting

On submitting a Process Deferred Accounting document GL Entries for deferred revenue or expense booking will be created for all the invoices falling between the service start and service end date.

Enter account if deferred revenue or expense has to be booked only for specific deferred income or expense account

### 3.2 Enabling automatic deferred accounting

To enable automatic deferred accounting enable the checkbox 'Automatically Process Deferred Account Entry' checkbox by navigating to Accounts Settings 

To access Accounts Settings go to
> Accounting > Accounting Masters > Accounts Settings

<img class="screenshot" alt="Process Deferred Revenue" src="{{docs_base_url}}/assets/img/accounts/process-deferred-accounting-settings.png">




