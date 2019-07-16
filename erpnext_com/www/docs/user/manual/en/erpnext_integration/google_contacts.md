<!-- add-breadcrumbs -->
# Google Contacts Integration

ERPNext provides an integration with Google Contacts in order for all users to synchronize their Google Contacts with ERPNext.


## Setup

In order to allow a synchronization with Google Contacts, you need to authorize ERPNext to get Contacts data from Google. Google Contacts Integration is set up with the following steps:

1. Create a new project on Google Cloud Platform and generate new OAuth 2.0 credentials.
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_project_creation.gif">
2. Add `https://{yoursite}` to Authorized JavaScript origins.
3. Add `https://{yoursite}?cmd=frappe.integrations.doctype.google_contacts.google_contacts.google_callback` as an authorized redirect URI.
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_oauth.gif">
4. Add your Client ID and Client Secret in the Google Settings in **Home > Integrations > Google Services > Google Settings**
5. In the Google Contacts list, click on New. Enter the Google Account Email you want to sync and then save it. Now click on `Authorize Contacts Access` to authorize ERPNext to get Contacts data from Google.
6. Once Authorized, you can manually sync Google Contacts or let ERPNext sync Google Contacts daily.
<img class="screenshot" src="/docs/assets/img/erpnext_integrations/google_contacts_sync.gif">


## Features

1. Creation of a Contacts in ERPNext from Google Contacts
	- All the Contacts present in Google Contacts will be synchronised in ERPNext Framework.
	- If any of the Google Contact have multiple Email Ids associated with them, new Contact will be created in ERPNext for each Email Id.
