<!-- add-breadcrumbs -->
# Warranty Claim

**If you are selling Items under warranty or if you have sold and extended service contract like the Annual Maintenance Contract (AMC), your Customer may contact you about an issue or a break-down of the product and provide you the Serial No of this
Item.**

To create a new Warranty Claim:

> Support > Warranty Claim > New Warranty Claim

## 1. Prerequisites
Before creating and using Warranty Claim, it is advised that you create the following first:

* [Customer](docs/user/manual/en/CRM/customer)
* [Serial Number](docs/user/manual/en/stock/serial-no)


## 2. How to Create Warranty Claim

1. Go to the Warranty Claim list, click on New.

### 2.1 Additional Options when Creating an Warranty Claim
* **Status**: While creating a Warranty Claim, status have to select as "Open". User can change teh status from list to "Closed", "Work-In-Progress" and "Cancelled".
* **Issue Date**: While creating the Warranty Claim, current date will be captured. This field is editable.
* **Customer**: User have to create or select the Customer from the list. This is a mandatory field.
* **Serial No**: User can select the Serial Number from the master. The system will then automatically fetch the Serial No’s details and indicate whether this is under warranty or AMC.

* **Issue** This is a text field. User can enter a details about the issue. Also, user can upload the image, enter or create a table.


## 3 Features

### 3.1 Item and Warranty Details:

* **Item Code:** Item code will be fetched automatically once user has defined the serial number. This field is editable. User can select deferent item as required.
* **Item Name:** Selected Item code's name will be displayed. 
* **Item Description:** Selected Item code's description will be displayed.
* **Warranty / AMC Status:** User can select the "Under Warranty", "Out of Warranty", "Under AMC", "Out of AMC" from list. 
* **Warranty Expiry Date:** In this field user can select the date when the item's warranty is going to expire.
* **Warranty Expiry Date:** In this field user can select the date when the item's AMC is going to expire.

### 3.2 Resolution:
* **Resolution Date:** When the warranty or AMC is Closed, current date and time will be fetched in resolution Date field automatically. This field is editable.

* **Resolved By:** User need to select the email id who has resolved / closed the Warranty. This will be link with User created in the system.

* **Resolved Details:** This is a text field. User can enter a details about the Warranty or AMC claim. Also, user can upload the image, enter or create a table.

### 3.3 More Information:

* **Company:** The Warranty or AMC is created from company will be selected automatically. This is editable field.

* **Raised By:** User can enter the Name who has raised the Warranty or AMC.

* **From Company:** User can write the name of the company for the warranty or AMC has been created.


### 3.4 Customer Details:

Once the status of Warranty or AMC is changed to "Work in Progress", "Closed" or "Cancelled", above defined customer's details are fetched automatically:

* **Customer Name:** Customer Name will be display. This field is not editable.
* **Contact Person:** The person to contact will be fetch from the customer's master. This field is editable.
* **Territory:** Customer territory will be display. This field is not editable.
* **Customer Group:** Customer group will be display. This field is not editable.
* **Customer Address:** Customer address will be display. User can select the customer address.
* **Service Address:** User can enter the Service Address if it is different from customer address. 






![Warranty Claim]({{docs_base_url}}/assets/img/support/warranty-claim.png)

If a Customer visit is required to address the issue, you can create a new
Maintenance Visit record from this.

{next}
