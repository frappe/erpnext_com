<!-- add-breadcrumbs -->
# Issue

**Issue is an incoming query from your Customer, usually via email or
from the “Contact” section of your website. (To fully integrate the Support
Ticket to email, see the Email Settings section).**

> Tip: A dedicated support Email Address is a good way to integrate incoming
queries via email. For example, you can send support queries to ERPNext at
support@erpnext.com and it will automatically create a Issue at our end.


To Create a New Issue:
> Home > Support > Issue > New Issue

<img class="screenshot" alt="Issue" src="{{docs_base_url}}/assets/img/support/issue.png">

## 1. Prerequisites
Before creating and using Issue, it is advised that you create the following first:

* [Customer](docs/user/manual/en/CRM/customer)

## 2. How to Create Issue
If you'd like to create an Issue manually, follow these steps:

1. Go to the Issue list, click on New.


### 2.1 Additional Options when Creating an Issue
* **Status**: When a new Issue is created, its status will be “Open”, when it is
replied, its status becomes “Replied”.
If the sender replies back its status again becomes “Open”.
User can “Close” the Issue manually by selecting the “Close”.
* **Priority**: Issue Priority can selected based on requirement. Priority can be set as per the requirements.
* **Issue Type**: This is the master from user can select the Issue Type to classify the issue.
* **Raised By(Email account)**: User need to enter the email account, while creating the issue.

## 3. Features

### 3.1 Details
* **Description**: This is a text field. User can enter a details about the issue. Also, user can upload the image, enter or create a table.

### 3.2 Service Level Agreement
It is a contract between a service provider and the end user that defines the level of service expected from the service provider.

User can select the "[Service Level Agreement](/docs/user/manual/en/support/service-level-agreement)" (SLA) from the list.

* Every Issue will have a Time to Response and Time to Resolve within which you have to Respond and Resolve the Issue.
* You can change Priority in order to escalate the priority of the Issue. The priorities need to be specified in the Service Level Agreement.
* If by any chance you feel like resetting Service Level Agreement, you can do so by clicking on the 'Reset Service Level Agreement' button in Issues shown as follows:

<img class="screenshot" alt="Issue" src="{{docs_base_url}}/assets/img/support/iss.gif">

### 3.3 Response
* **First Response on**: When the user reply on the issue, first response date and time will get updated.

### 3.4 Reference
User can filter the issues based on these fields:

* **Lead**: User can create or link a Lead to the Issue. 
* **Contact**: User can create or link a Contact from the Contact master. 
* **Email Account**: User can give the reference by defining the email group account. This is an email master.
* **Project**: User can create or link a project from the project master.
* **Company**: This field the auto selected. User can select the company from the company list. The issue has been raised or created against the company will be selected in this field.

### 3.5 Resolution
* **Opening Date**: When the issue is created or logged date will automatically get update.

* **Opening Time**: When the issue is created or logged time will automatically get update.

* **Resolution Date**: When the user resolved the issue, Date and Time will get updated in this field.

* **Resolution Details**: User can enter the details of the issue, once it is resolved. This is a text field. Also, user can upload the image, enter or create a table.

## 4. After Saving
### 4.1 Discussion Thread

* When a new email is fetched from your mailbox, a new Issue record is created and an automatic reply is sent to the sender indicating the Support Ticket Number.
* The sender can send additional information to this email.
* All subsequent emails containing this Issue number in the subject will be added to this Issue thread.
* The sender can also add attachments to the email.

* Issue maintains all the emails which are sent back and forth against this issue in the system so that you can track what transpired between the sender and the person responding.

### 4.2 Add Comments
Once the Issue is registered, user can add a comments for the issue. This field is editable.

### 4.3 New Email
User can compose an email to the person has raised the issue. All the mails (received as well as sent) will be recorded against the issue.

### 4.4 Allocation

* You can allocate the Issue by using the “Assign To” feature in the left sidebar. This will add a new To Do to the user and also send a message indicating that this Issue is allocated.

### 4.5 Closing

* You can either “Close” the Issue manually by clicking on “Close Ticket” in the toolbar or if its status is “Waiting For Reply”.
* If the sender does not reply in 7 days, then the Issue closes automatically.


{next}