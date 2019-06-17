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
- In your connect API under "Create popup feature" and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`
- After that add a Passthru applet under "After Call Conversation ends" and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_end_call`
and Check "Make Passthru Async"
- Lastly, add a Passthru applet under "If nobody answers..." section and paste following URL:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_missed_call`
and Check "Make Passthru Async"
- Save the flow.
- Now assign this newly created app to your ExoPhone from which you receive your business calls.

### 2. Setup in ERPNext

- From Awesome Bar, go to 'Exotel Settings'.
- Set your "Exotel SID" and "Exotel Token". (Link to find Exotel API credentials)
- Go to Communication Medium.
- Add your ExoPhone and schedule that number. Based on this schedule employees will receive the popup.
