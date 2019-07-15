---
title: Version 12 Features
add_breadcrumbs: 0

metatags:
 image: /assets/frappe/img/page-cover.jpg
 description: Create custom dashboards for everything you want to measure. Monitor and visualise your growth.
 tags: [dashbaords, erpnext dashbaords, erpnext version-12, erp, erp dashboards]
---

# Features and Enhancements

## Auto Fetch Serialized Items
Serial numbers can be automatically fetch based on FIFO. It will ignore any items for which transactions like sales is created.

<img alt="Auto Fetch" src="/assets/erpnext_com/img/version-12/auto-fetch.gif" style="width:70%" class="screenshot">

## Link Preview
Hovering on links in list view and other link fields will show a small popup with information about the document. You can view information of items, quotations and other doctypes without opening the form.

![Link Preview](/assets/erpnext_com/img/version-12/link-preview.png)

## New Upload Dialog
We have refactored the upload feature, the new dialog allows you to easily access previously uploaded files, drag and drop multiple files and upload them.

![Link Preview](/assets/erpnext_com/img/version-12/upload.png)

## Frequently visited links appear in Awesomebar results
Allowing quicker access to relevant doctypes, this makes ERPNext easy to navigate.

![Awesomeplete Recent Items](/assets/erpnext_com/img/version-12/recent-items.png)

## Full Width Container
Full width view is useful for viewing large reports. It can be toggled from the user settings dropdown on the toolbar.
![Full Width](/assets/erpnext_com/img/version-12/full-width.gif)

## List View Enhancements
Percentage fields can be viewed as a progress bar in List View. It can be enbaled by checking 'In List View' option for that field in customize form.
![List View Percentage](/assets/erpnext_com/img/version-12/list-view-percentage.png)

Action buttons like Open reference doctypes in todo, can directly be triggered from the list view.
![List View Buttons](/assets/erpnext_com/img/version-12/list-view-buttons.png)

## Disable customization for single doctypes
Single doctypes are generaly used for storing configuration for various modules, customizing them without good knowledge of the system can cause the system to break, hence customization of these doctypes is disabled by default

## Google Contacts
## PDF Encryption
The frappe print API now supports encrypting PDFs, it can be accessed in the `frappe.get_print()` function by passing the `password` argument.

## Web Form Refactor
Webform client is refactored fixing broken filters and other fields. From version 12, the page break field has also been removed in webforms from Frappe.

## Added Track Views field to Customize Form
Tracking views of a doctype can be enabled from customized form.

## Recorder


## Add custom columns to any report