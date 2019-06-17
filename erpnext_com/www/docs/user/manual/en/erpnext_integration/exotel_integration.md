<!-- add-breadcrumbs -->

# Exotel Integration

This integration enables you to integrate Exotel with your ERPNext system, if you are using Exotel for business to capture the leads with their phone number directly in your ERPNext account.

## Features

1. Track incoming calls in your ERPNext account.
2. Shows lead/customer information pop-up to employees when an incoming call is received.

## How to setup

### 1. Setup in your Exotel account for call popup

- Login to your Exotel account and go to App Bazar
- Create a new App for a new flow.
- Setup the flow as you wish it to be.
- In your connect API under "Create popup..." and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

<img class="screenshot" alt="Connect Applet" src="{{docs_base_url}}/assets/img/erpnext_integrations/exotel_integration/connect_applet.png">

<img class="screenshot" alt="Call Popup Section" src="{{docs_base_url}}/assets/img/erpnext_integrations/exotel_integration/create_popup_section.png">

> **Note:** Replace `<your-site>` in URL with your site name. For example, if the site name is **frappe.erpnext.com** then the URL will be: `https://frappe.erpnext.com/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

- After that add a Passthru applet under "After Call Conversation ends" and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_end_call`

<img class="screenshot" alt="After Conversation Ends Section" src="{{docs_base_url}}/assets/img/erpnext_integrations/exotel_integration/after_conversation_ends_section.png">

<img class="screenshot" alt="After call ends section" src="{{docs_base_url}}/assets/img/erpnext_integrations/exotel_integration/passthru_end_call.png">

> **Note:** Make sure to check "Make Passthru Async"

- Similary, add a Passthru applet under "If nobody answers..." section and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_missed_call`

<img class="screenshot" alt="No Response Section" src="{{docs_base_url}}/assets/img/erpnext_integrations/exotel_integration/no_response.png">

<img class="screenshot" alt="After call ends section" src="{{docs_base_url}}/assets/img/erpnext_integrations/exotel_integration/passthru_missed_call.png">

> **Note:** Make sure to check "Make Passthru Async"

- Save the flow.
- Now assign this newly created app to your ExoPhone from which you receive your business calls.

### 2. Setup in ERPNext

- From Awesome Bar, go to 'Exotel Settings'.
- Set your "Exotel SID" and "Exotel Token". You can find your Exotel API key and token on your [Exotel Dashboard](https://my.exotel.com/apisettings/site#api-credentials)
- Go to Communication Medium.
- Add your ExoPhone and schedule that number. Based on this schedule employees will receive the popup.
