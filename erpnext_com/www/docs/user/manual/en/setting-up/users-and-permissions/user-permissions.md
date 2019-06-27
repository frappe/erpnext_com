<!-- add-breadcrumbs -->
# User Permissions

Along with Role based permissions, you can also set user level permissions that are based on rules that are evaluated against the data contained in the document being accessed. This is particularly useful when you want to restrict based on:

1. Allow user to access data belonging to one Company
2. Allow user to access data related to a specific Customer or Territory

### Creating User Permissions

To create a User Permission, go to Setup > Permission > User Permissions

When you create a new record you will have to specify

1. The user for which the rule has to be applied
2. The type of document which will be allowed (for example "Company")
3. The specific item that you want to allow (the name of the "Company)
4. If you check "Is Default", the default value will be set in the transaction for fields of this type (example "Company")

    <img src="{{docs_base_url}}/assets/img/users-and-permissions/user-perms/new-user-permission.png" class="screenshot" alt="Creating a new user permission">

    >Note: Only a single user permission can be set as default for a particular doctype for a specific user.

### Advanced control

You can optionally apply user permission only for specific Document Type by setting the Document Type in the Applicable For field under Advanced Control.
Setting **Applicable For** option will make the current user permission applicable only under the selected Document Type master.

<img src="{{docs_base_url}}/assets/img/users-and-permissions/user-perms/advanced-control.png" class="screenshot" alt="Advance control">
In the above User Permission, user michael.corleone@gadgets.com will be able to access blog posts created by blogger Michael Corleone.

**Note:** If **Applicable For** is not set, User Permission will applicable across all related Document Types.

### Ignoring User Permissions on Certain Fields

Another way of allowing documents to be seen that have been restricted by User Permissions is to check "Ignore User Permissions" on a particular field by going to **Customize Form**

For example you don't want Assets to be restricted for any user, then select **Asset** in **Customize Form** and in the Company field, check on "Ignore User Permissions"


<img src="{{docs_base_url}}/assets/img/users-and-permissions/user-perms/ignore-user-permissions.png" class="screenshot" alt="Ignore User Permissions on specific properties">


### Strict Permissions

Since User Permissions are applied via Roles, there may be many users belonging to a particular Role. Suppose you have three users belonging to Role "Accounts User" and you have applied **User Permissions** to only one user, then the permissions will only be restricted to that user.

You can change this setting incase you want the user permissions to be assigned to all users, even if they are not assigned any user permissions by going to **System Settings** and checking "Apply Strict User Permissions"

### Checking How User Permissions are Applied

Finally once you have created your air-tight permission model, and you want to check how it applies to various users, you can see it via the **Permitted Documents for User** report. Using this report, you can select the **User** and document type and check how user permissions get applied.

<img src="{{docs_base_url}}/assets/img/users-and-permissions/user-perms/permitted-documents.png" class="screenshot" alt="Permitted Documents for User report">

{next}