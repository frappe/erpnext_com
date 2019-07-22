<!--add breadcrumbs-->

# Personal Data Download

As a part of GDPR compliance, ERPNext has Personal Data Download.

Personal data download tool enables a user to automatically download all the personal data they have generated while using ERPNext. This includes personally identifiable data of your account and data from lead, contact, communication, emails, and so on.

## 1. How to request user data download

1. To begin downloading data, the user has to **logged in** and visit [host-name]/request-data (e.g. erpnext.com/request-data) in the URL field.

    <img class="screenshot" alt="Request Data" src="{{docs_base_url}}/assets/img/setup/personal-data-download-request/request-data-webform.png">

2. After submitting your request, you will receive a success response.
    <img class="screenshot" alt="Request Data" src="{{docs_base_url}}/assets/img/setup/personal-data-download-request/download-request-succes.png">

3. This will sent a mail with a download link of the data to the email address associated with the user.
    <img class="screenshot" alt="Download Data Email" src="{{docs_base_url}}/assets/img/setup/personal-data-download-request/download-data-email.png">

The file available for download will be in the JSON format.

## 2. Personal Data Download Request DocType

The request is also recorded in the DocType "Personal Data Download Request", the file-link that is sent to the user via email is also attached to the doc. Serach for Personal Data Download Request from the search bar.

<img class="screenshot" alt="Personal Data Download Request Doctype" src="{{docs_base_url}}/assets/img/setup/personal-data-download-request/personal-data-download-request-doctype.png">

### 3. Related Topics
1. [Personal Data Deletion](/docs/user/manual/en/setting-up/personal-data-deletion)
