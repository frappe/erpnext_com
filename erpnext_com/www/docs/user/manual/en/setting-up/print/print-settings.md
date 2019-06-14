<!-- add-breadcrumbs -->
# Print Settings

In Print Settings you can set your printing preferences like Paper Size, default text size, whether you want to output as PDF or HTML etc. To edit print settings, go to: **Settings > Printing > Print Settings**.

<img class="screenshot" alt="Print Settings" src="{{docs_base_url}}/assets/img/setup/print/print-settings.png">


There is various other configuration available in the Print Settings. Let's learn about each below.

### 1. PDF Settings

#### 1.1 PDF or HTML

When you email any document (like order or invoice) from ERPNext, it is sent in the PDF or HTML format. The file is sent in the PDF by default. If you wish to send a document in the HTML format, just uncheck field "Send Print as PDF".

#### 1.2 Repeat Header and Footer in PDF

The letterhead is a master where you can define the standard Header and Footer which is appended to the document's Print Format. If this Property is enabled, then Header and Footer are added to each page. If you don't want header and footer repeat on each page, just disbale this setting.

### 2. Page Settings

#### 2.1 Print With Letterhead

Enabling this property will automatically update Letterhead in each of your print formats.

#### 2.2 Compact Item Print

The transactions like orders and invoices have table detailing item's bought or sold. It has multiple columns like Item Name, Description, UoM, Rate Amount etc. If there are many columns in the Item table, then print format looks bit cluttered. You can improve the view of the table by enabling Compact Item Print. 

As per this setting, there will be only four column in the Print Format, namely:

> Description, Qty, Rate and Amount

The value of other columns (like name, description, image, serial nos. etc.) is concatenated in the Description column. Here is the sneak preview of Compact Print Format.

<img class="screenshot" alt="Compact Print Format Settings" src="{{docs_base_url}}/assets/img/setup/print/compact-print.png">

#### 2.3 Allow Print for Draft

The documents (mostly transactions) has two stage of authentication, Save and Submit. The saved documents are a first draft and mostly un-authenticate. Hence printing is restricted for the documents at this stage. However, if you wish to permit users to print documents at the Draft stage as well, enabling this setting will help.

#### 2.4 Send document web view link in the email

ERPNext has a portal view available from where parties like Customer and Suppliers can signup and view their order history.

When you email a transaction to your party, you can also send a web link to view the same document on the portal of your ERPNext account.

#### 2.5 Always add "Draft" Heading for printing draft documents

Enabling this setting also print Draft in the Print Format as well, thus indicating that document shared is not completely authenticated as yet.

#### 2.6 Allow Page Break Inside Table

If you have item's details which capture more than usual space of a page, then enabling this setting will split item's details to the next page. Hence, a page break will be inserted between the Item Description, and the rest of the details will be pushed to the next page.

#### 2.7 Allow Print for Cancelled

Canceled transactions are the ones which don't have any impact on the reports. If you wish to allow printing for the canceled transactions, then enable this setting.

#### 2.8 Print Taxes with Zero Amount

In the sales and purchase transactions, you can add apply multiple taxes on the item. Bydefault, in the print format, only taxes which has some amount calculated are visible in the Print Format. If you wish to also print the tax which was not applied to any item and has zero tax amount, just enable this setting.

#### 3. Network Printer

You can enable print server by fill the print server IP and port then chose default printer

Before enabling this feature you have to install pycups library.

You may need first to install cups library if is not already on your system

For Debian OS Family:

`sudo apt-get install libcups2-dev`

For Redhat OS Family:

`sudo yum install cups-libs`

After that, install pycups in the env using the command

`./env/bin/pip install pycups`

executed from the `frappe-bench` directory.

#### 4. Raw Printing

You can enable raw printing and print to many supported thermal printers. [Click here to know more about Raw Printing.](/docs/user/manual/en/setting-up/print/raw-printing)

{next}
