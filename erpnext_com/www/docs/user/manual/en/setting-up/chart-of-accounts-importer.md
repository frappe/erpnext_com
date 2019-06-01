<!--add breadcrumbs-->

# Chart Of Accounts Importer

Chart Of Accounts Importer is avaiable in ERPNext from v12 onwards.

To start importing charts of accounts navigate to

> Getting Started > Data Import and Settings > Chart of Accounts Importer

1\. Select the Company for which you want to import chart of accounts. Make sure the company you are selecting doesn't have an pre existing transactions otherwise you'll receive a validation error.

2\. Click on `Download Template` button on the top right corner to download the template. The template you have downloaded will look as follows.

<img class="screenshot" alt="POS Setting" src="{{docs_base_url}}/assets/img/setup/coa-template-download.png">

<img class="screenshot" alt="POS Setting" src="{{docs_base_url}}/assets/img/setup/coa-template.png">

3\. Once you download the template fill in the template as shown in the screenshot below. Please make sure to make accounts for account type "Cost of Goods Sold", "Depreciation", "Fixed Asset", "Payable", "Receivable", "Stock Adjustment". Root type for these accounts must be one of Asset, Liability, Income, Expense and Equity

<img class="screenshot" alt="POS Setting" src="{{docs_base_url}}/assets/img/setup/coa-template-1.png">

4\. Click on ```Attach``` to upload the template

<img class="screenshot" alt="POS Setting" src="{{docs_base_url}}/assets/img/setup/coa-attach.png">

5\. Once you upload the template you'll be able to see the preview of the charts of accounts in the preview section

<img class="screenshot" alt="POS Setting" src="{{docs_base_url}}/assets/img/setup/coa-preview.png">

6\. If everything seems correct in the preview then click on ```Start Import``` in the top right corner and the accounts will be created.

<img class="screenshot" alt="POS Setting" src="{{docs_base_url}}/assets/img/setup/coa-start-import.png">

7\. To verify the created accounts you can go to chart of accounts and see the newly created accounts for that company.

<img class="screenshot" alt="POS Setting" src="{{docs_base_url}}/assets/img/setup/coa-import.png">





