<!-- add-breadcrumbs -->
# Adding Users

Users can be added by the System Manager or Administrator. To add users go to:
> Home > Users and Permissions > Users > User

There are two main types of users: Website Users and System Users. System Users are people using ERPNext in the company with access to modules, company data, etc. Web users are customers or suppliers who have access only to the portal.
  
Under User, a lot of info can be entered. For the sake of usability, the information entered for web users is minimal: First Name and Email.

An Email address is the unique key (ID) identifying the Users.

> Home > Users and Permissions > Users  > User

## 1. How to create a new User

1. Click on New.
1. Add an Email address and name of the user.
1. Save.

    <img class="screenshot" src="{{docs_base_url}}/assets/img/users-and-permissions/add-user-details.png" alt="Add User Details">

Details like Username and Language can also be changed.

## 2. Features

### 2.1 Setting Roles

After saving, you will see a list of roles and checkboxes next to them. Just check the roles you want the user to have and save the document. To click on what permissions translate into roles, click on the role
name. You can set [Role profiles](/docs/user/manual/en/setting-up/users-and-permissions/role-and-role-profile) to select multiple roles together.

<img class="screenshot" src="{{docs_base_url}}/assets/img/setup/users/user-2.png" alt="User Roles">

### 2.2 More Information

* Gender
* Phone
* Mobile No
* Birth Date
* Location
* Interests
* Bio
* Banner Image

Mute Sounds will mute sounds that play on interacting with documents. The user may need to do a Settings > Reload for the changes to take place.

### 2.3 Change Password

* **Set New Password**: Set a new password for the user.
* **Send Password Update Notification**: Send an email notification to the user that their password has been changed.
* **Logout from all devices while changing Password**: Logout the user from PC and any mobile device when changing the user's password.

### 2.4 Document Follow
With this option you can follow various documents in the system and get email notifications when they are updated. Know more [here](/docs/user/manual/en/setting-up/email/document-follow).

### 2.5 Email Settings

* **Send Notifications for Email threads**: The user will get a notification for Email threads in DocTypes like Opportunities.
* **Send Me A Copy of Outgoing Emails**: Send the user a copy of the Emails they send.
* **Allowed In Mentions**: Allow this user's name to appear in conversations so that they can be mentioned using '@'.
* **Email Signature**: Adding an email signature here will set it as default for all outgoing emails.

### 2.6 Email Inbox

Subscribe the user to different mailing lists of your company.

### 2.7 Allow Module Access

Users will have access to all modules for which they have role based access. If you want to block certain modules for certain users, un-check the module from the list.

<img class="screenshot" src="{{docs_base_url}}/assets/img/setup/users/user-3.png" alt="User Block Module">

### 2.8 Security Settings

* **Simultaneous Sessions**: Simultaneous login sessions the user is allowed.
* **User Type**: If the user has any role checked other than customer and supplier, they automatically become a System User.
* **Login After, Login Before**: If you wish to give the user access to the system only between office hours,
or during weekends, specify it here.
* **Restrict IP**: Restrict user login to the IPs specified here. Multiple IPs can be added separated by commas.

This section also shows other details like Last Login, Last IP, and Last Active for the user.

### 2.9 Third Party Authentication
This will allow users to use Facebook, Google, or GitHub to log in. Signup for a developer account with Facebook, Google, GitHub, etc. Create an app on their console, specify app name, originating URL and callback URL, copy the client ID and client secret info here. 

For more details, go to [this page](https://frappe.io/docs/user/en/guides/deployment/how-to-enable-social-logins).

### 2.10 API Access
You can generate API Secret keys from this section using the Generate Keys button.

### 3. Login Methods
Mobile No can also be used to log in if you check the Allow Login using Mobile No checkbox under the Security section in System Settings. While Mobile No will be unique, it will not be treated as a user id.

Login with Email:

<img class="screenshot" src="{{docs_base_url}}/assets/img/setup/users/user-login-email.png" alt="Email Login">

Login with Email or Mobile:

<img class="screenshot" src="{{docs_base_url}}/assets/img/setup/users/user-login-mobile.png" alt="Mobile No Login">

After adding these details, save the user.

### 4. Related Topics
1. [Role Based Permissions](/docs/user/manual/en/setting-up/users-and-permissions/role-based-permissions)
1. [User Permissions](/docs/user/manual/en/setting-up/users-and-permissions/user-permissions)
1. [Document Follow](/docs/user/manual/en/setting-up/email/document-follow)
