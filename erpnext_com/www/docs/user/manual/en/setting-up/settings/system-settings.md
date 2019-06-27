<!-- add-breadcrumbs -->
# System Settings

You can localize ERPNext to use particular timezone, date, number or currency format, and also set global session expiry via System Settings.

By checking the 'Allow Login using Mobile Number' checkbox, you can login to ERPNext using a valid mobile number set in your User account. 

To open System Settings, go to:

> Home > Settings > Core > System Settings

<img class="screenshot" alt="System Settings" src="{{docs_base_url}}/assets/img/setup/settings/system-settings.png">

## 1. Sections in System Settings

### 1.1 General

* Country
* Time Zone
* Language

### 1.2 Date and Number Format

* **Date Format**: Format in which dates will be displayed. Eg: dd.mm.yyyy or mm/dd/yyyy.
* **Number Format**: Format in which numbers will be formatted. Eg: 1,000 or 1000.00.
* **Float Precision**: The number of zeros displayed after the decimal point for quantities etc. Range is 2-9. Default is 3.
* **Currency Precision**: Number of zeros displayed after decimal point for currency values. If left blank, it will be based on the **Number Format**.

### 1.3 Backups

Number of Backups after which older ones will be deleted. The default is a standard, 3.

### 1.4 Permissions

If **Applying Strict User Permissions** checkbox is ticked and User Permission is defined for a DocType for a User, then all the documents where value of the link is blank, will not be shown to that User.

This is done from:
> Home > Users and Permissions > Permissions > User Permissions

For example: If you set User Permissions for Territory and set the value as India. If checkbox is unticked, all transactions (sales orders, quotations) with India and blank will be shown to the user.

If the checkbox is ticked, documents where Territory is blank will not be shown to the user.

### 1.5 Security

* **Session Expiry**: Number of hours after which you'll be logged out of a session. 0 means no limit.
* **Session Expiry Mobile**: Session expiry when logged in from a mobile phone.
* **Allow only one session per user**: Allow user login in via mobile phone for a User.
* **Allow Login using Mobile Number**: Allow user login in via mobile number.
* **Allow Login using User Name**: Allow user login via their username.
* **Show Full Error and Allow Reporting of Issues to the Developer**: This will display the whole error on the screen and allow reporting issues.

### 1.6 Password

* **Force User to Reset Password**: Number of days after which a password reset is mandatory. 0 means no limit.
* **Enable Password Policy**: Enables a password strength checker.
* **Minimum Password Score**: Score for the password strength checker, 2 is medium, 3 is strong, and 4 is very strong.

### 1.7 Brute Force Security

* **Allow Consecutive Login Attempts**: Consecutive logins after which you'll be locked out of the account for a specific time period.
* **Allow Login After Fail**: Seconds after which a login attempt will be allowed after consecutive unsuccessful attempts.

### 1.8 Two Factor Authentication
Settings for Two Factor Authentication can be configured here.

On ticking 'Enable Two Factor Auth', the following two options will be seen.

* **Bypass Two Factor Auth for users who login from restricted IP Address**: Users who login from restricted IP addresses will not be asked for Two Factor Authentication. You can restrict IPs from User master under the Restrict IP field.
* **Bypass restricted IP Address check If Two Factor Auth Enabled**: If checked, all users can login with Two Factor Authentication.

* **Two Factor Authentication method**: Select the authentication method to be used.
* **Expiry time of QR Code Image Page**: Expiry time for QRCode image if "OTP App" is selected in method.
* OTP Issuer Name of the One Time Password.

### 1.9 Email

* **Email Footer Address**: Organization name, address, and other details can be added here.
* **Disable Standard Email Footer**: If ticked, the standard email footer will be disabled.
* **Hide footer in auto email reports**: If ticked, footers will be hidden in 'Auto Email reports'.

### 1.10 Chat

* **Enable Chat**: Enable in app chat to communicate with other system users.
* **Use socketio to upload file**: If ticked, Socket.IO will be used to upload files.

    <img class="screenshot" alt="Two Factor Auth" src="{{docs_base_url}}/assets/img/setup/settings/twofactor-settings.png">


{next}
