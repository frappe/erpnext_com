<!-- add-breadcrumbs -->
# Setting up LDAP

Lightweight Directory Access Protocol is a centralised access control system used by many small and medium scale organisations.

By settings up LDAP service, you able to login to ERPNext account by using LDAP credentials.

#### Setup LDAP

##### Prerequisites
To use LDAP, you will first need to install the ldap3 python module.  To do this, open a terminal session on your server that hosts the ERPNext instance. Go to the frappe-bench directory.
run the command: `./env/pip install ldap3`

After completing the step above, you are now ready to enable the LDAP servrice in ERPNext.

To setup LDAP, go to
`Explore > Integrations > LDAP Settings`

There are a number of parameters that are mandatory to allow ERPNext to connect to LDAP
These are:
  * ##### LDAP Server URL
    This is the url to your LDAP server. Must be in the form of `ldap://yourserver:port` or `ldaps://yourserver:port`

  * ##### Base Distinguished Name (DN)
    This is the distinguised name of the user that has permissions to look up user details on your LDAP server.  This should be a user that only has read-only permissions on your LDAP Server.

  * ##### Password for Base DN
    This is the password for the user above, that is used to look up user details on your LDAP server.
  
  * ##### Organization Unit of Users
    This is the DN of the Organizational Unit that all users in your LDAP Server must be part of to be able to log into ERPNext.

  * ##### Default Role on Creation
    When the user is created in ERPNext, they will be assigned with this default role, the first time they log in.

  * ##### LDAP Search String
    This field allows ERPNext to match the user/email entered in the ERPNext login screen, with the LDAP Server.  For example you could use email address, or username depending on your preference.
    
    It must be entered in the format : `LDAPFIELD={0}`  

    Active Directory username example: `sAMAccountName={0}`

    Open LDAP username example: `uid={0}`

  * ##### LDAP Email Field
    Specifies the LDAP field that contains the email address of the user.

    Active Directory and Open LDAP example: `mail`

  * ##### LDAP Username Field
    Specifies the LDAP field that contains the username of the user.  

    Active Directory example : `sAMAccountName`
    
    Open LDAP example: `uid`

  * ##### LDAP First Name Field
    Specifies the LDAP field that contains the first name of the user.  

    Active Directory example: `givenName`

    Open LDAP example: `sn`

There are a number of other non mandatory fields that you can use to map your LDAP user fields to the ERPNext user fields.  They are:
  * Middle Name
  * Phone
  * Mobile

<img class="screenshot" alt="LDAP Settings" src="{{docs_base_url}}/assets/img/setup/integrations/ldap_settings.png">

Once your settings are correct, you can click the `Enabled` checkbox at the top.  When attempting to enable LDAP, ERPNext will try and connect to the LDAP Server to ensure the settings are correct.  If it fails, you will not be able to enable LDAP, and will receive an error message.

The error message will indicate the issue that needs to be resolved to continue.

After setting enabling LDAP, on the login screen, the system enables **Login Via LDAP** option.

<img class="screenshot" alt="LOGIN via LDAP" src="{{docs_base_url}}/assets/img/setup/integrations/login_via_ldap.png">

#### LDAP Security

In the LDAP Security section, You have a number of options to connect securely to your LDAP server.

  * ##### SSL/TLS Mode
    Specifies whether you want to start a TLS session on initial connection to the LDAP server.

  * ##### Require Trusted Certificate
    Specifies if you require a trusted certificate to connect to the LDAP server


  If you are specifying a trusted certificate, you will need to specify the paths to your certificate files.  These files are to be placed on your ERPNext server, and the fields below should be an absolute path to the files on your server.
    The certificate fields are:

  * Path to private Key File
    
  * Path to Server Certificate
    
  * Path to CA Certs File


#### LDAP Group Mappings
ERPNext also allows you to automatically map multiple LDAP groups to the appropriate ERPNext roles.  
For example you may want all of your Accounting employees, to automatically have the Accounts User Role.

Ensure that you fill out the LDAP Group Field to allow this.  This is the LDAP field that is found on a user object in LDAP, that has all of the groups the user is a member of.

For Active Directory and Open LDAP this field should be set to `memberOf`

Open LDAP may need this field to be enabled on your LDAP server.  Please see examples on the internet for more details.

> Note that all ERPNext roles will be checked each time a user logs on, and will be removed or added to the users permissions.

<img class="screenshot" alt="LDAP Group Mappings" src="{{docs_base_url}}/assets/img/setup/integrations/ldap_group_mappings.png">
