<!-- add-breadcrumbs -->
# Email Accounts

**You can add your email account to be used with ERPNext account.**

You can manage multiple incoming and outgoing Email Accounts in ERPNext. There has to be at least one default outgoing account and one default incoming account. If you are on the ERPNext cloud, the default outgoing email is set by us.

To access Email Accounts, go to:
> Home > Setting > Email > Email Account

## 1. How to create an Email Account
1. Click on New.
1. Enter the email address with the domain. [Domains](/docs/user/manual/en/setting-up/email/email-domain) need to be created in order to create an email account.
1. Enter its password.
1. Save.

### 1.1 Additional options when creating an Email Account
1. **Use Different Email Login ID**: To use an alternative email login and password to access this account.
1. **Awaiting password**: If you're creating this account on behalf of someone and the password is unknown, tick this checkbox.
1. **Use ASCII encoding for password**: Ticking this will use ASCII encoding for the password.

## 2. Configuration of the Email Account
### 2.1 Default Email Accounts

ERPNext will create templates for a bunch of email accounts by default. Not all of them are enabled. To enable them, you must set your account details.

There are two types of email accounts, outgoing and incoming. Outgoing email accounts use an SMTP service to send emails and emails are retrieved from your inbox using an IMAP or POP. Most email providers such as Gmail, Outlook, or Yahoo provide these services.

<img class="screenshot" alt="Defining Criteria" src="{{docs_base_url}}/assets/img/setup/email/email-account-list.png">

### 2.2 Incoming Email Accounts

To set up an incoming Email Account, check on **Enable Incoming** and set your POP3 settings, if you are using a popular email service, these will be preset for you.

<img class="screenshot" alt="Incoming EMail" src="{{docs_base_url}}/assets/img/setup/email/email-account-incoming.png">

The following options are available for incoming emails:

* Use IMAP
* Use SSL
* Attachment Limit
* **Append To**: Add emails in this account to a DocType in the Communication section.
* **Default Incoming**: If ticked, all replies to your company (eg: replies@yourcomany.com) will come to this account.
* **Email Sync Option**: Whether to sync all or only unseen emails.
* **Initial Sync Count**: Number of emails to sync the first time.

Enable Automatic Linking in Documents will link emails to documents, to know more [click here](/docs/user/manual/en/setting-up/email/linking-emails-to-document).

### 2.3 Notification for unreplied messages

If you would like ERPNext to notify you if an email is unreplied for a certain amount of time, then you can set **Notify if Unreplied**. Here you can set the number of minutes to wait before notifications are sent and whom the notifications must go to.

<img class="screenshot" alt="Incoming EMail" src="{{docs_base_url}}/assets/img/setup/email/email-account-unreplied.png">

#### Setting Import Conditions for Email Import

Email Accounts allows you to set conditions according to the data of the incoming emails. The email will be imported to ERPNext only if all conditions are true. For example, if you want to import an email if the subject is "Some important email", you put doc.subject == "Some important email" in the conditions textbox. You can also set more complex conditions by combining them, as shown on the following screenshot.

<img class="screenshot" alt="Incoming EMail Conditions" src="{{docs_base_url}}/assets/img/setup/email/email-account-incoming-conditions.png">

### 2.4 Outgoing Email Accounts

All emails sent from the system, either by the user to a contact or via notifications or via transaction emails, will be sent from an Outgoing Email Account.

To set up an outgoing Email Account, check on **Enable Outgoing** and set your SMTP server settings, if you are using a popular email service, these will be preset for you.

<img class="screenshot" alt="Outgoing EMail" src="{{docs_base_url}}/assets/img/setup/email/email-account-sending.png">

The following options are available for outgoing emails:
* Use TLS
* Port
* Disable SMTP server authentication
* Add Signature

* **Default Outgoing**: Notifications and bulk emails will be sent from this outgoing server.
* **Always use Account's Email Address as Sender**: The email address of this account will be mentioned as the sender for outgoing emails.
* **Send unsubscribe message in email**: Send a link to unsubscribe from emails sent from this account.
* **Track Email Status**: Track if your email has been opened by the recipient. Note that, if you're sending to multiple recipients, even if one recipient reads the email, it'll be considered "Opened".
* **Enable Auto Reply**: If enabled, enter an auto reply message.

### 3. How ERPNext handles replies

In ERPNext when you send an email to a contact like a customer, the sender will be the user who sent the email. In the **Reply-To** property, the Email Address will be of the default incoming account (like `replies@yourcompany.com`). ERPNext will automatically extract these emails from the incoming account and tag it to the relevant communication.

> **Note for self implementers:** For outgoing emails, you should set up your own SMTP server or sign up with an SMTP relay service like mandrill.com or sendgrid.com that allows a larger number of transactional emails to be sent. Regular email services like Gmail will restrict you to a limited number of emails per day.

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/ChsFbIuG06g?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

### 4. Related Topics
1. [Email Inbox](/docs/user/manual/en/setting-up/email/email-inbox)
1. [Email Digest](/docs/user/manual/en/setting-up/email/email-digest)
1. [Auto Email Reports](/docs/user/manual/en/setting-up/email/auto-email-reports)
1. [Sending Email](/docs/user/manual/en/setting-up/email/sending-email)
1. [Email Domain](/docs/user/manual/en/setting-up/email/email-domain)
