## Email Template

Every email sent is different but certain emails can be standardized, usually known as Email Template or Standard Reply.

To create a new Email Template, navigate through:
> Email Template > New Email Template

**Name:** The name for this Email Template.

**DocType Associated:** (optional) The DocType associated with this template.

**Subject:** The Subject of this Email Template.

**Response:** The standard content of the email that will be a part of this template

<img class="screenshot" alt="Email Template" src="{{docs_base_url}}/assets/img/setup/email/new-email-template.png">

<img class="screenshot" alt="Email Template" src="{{docs_base_url}}/assets/img/setup/email/email-template-example.png">

## How to use Email Template
You can use this Email Template in the Emails that are sent from ERPNext in the "CC, BCC & Email Template" field of the email section of the document. ERPNext will fetch the subject and response as per the template selected.

##How to get fieldnames
The fieldnames you can use in your email template are the fields in the document from which you are sending the email. You can find out the fields of any documents via Setup > Customize Form View and selecting the document type (e.g. Sales Order)

##Templating
Templates are compiled using the Jinja Templating Langauge. To learn more about Jinja, read this documentation.