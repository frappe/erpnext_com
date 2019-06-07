# Point of Sale

For retail operations, the delivery of goods, accrual of sale and payment all happens in one event, that is usually called the “Point of Sale” (POS).

In ERPNext all Sales and Purchase transactions, like Sales Invoice, Quotation, Sales Order, Purchase Order etc. can be edited via the POS. There two steps to Setup POS:

You have to create a POS Profile before you can start using POS.

### 1. How to create a POS Profile
1. Go to: **Accounts > Retail Operations > Point-of-Sale Profile > New**.
1. Enter a name for the profile.
1. Select a naming series if applicable.
1. Set a naming series.
1. Set a Write Off Account and Write Off Cost Center to which the transactions will be recorded.
1. Set up payment modes in the table, the default will be cash if nothing is set here.
1. Set one of them as the default payment method.
1. Click on the right arrow on the Payment Method in the table and set an account where the money will be received.
1. Set the default amountS for the payment methods (recommended: 0).
1. Save.

### 2. How to create a POS Invoice
Once you set up a POS profile, you can start billing on POS.

1. Go to: 1. Go to: **Accounts > Retail Operations > POS**.
1. Select a Customer.
1. Add items from the list displayed on the right by clicking on them.
1. Ensure that the item has a Selling Price set in the Item Price list.
1. Edit the quantities as needed.
1. In order to edit rate and discount, you need to check those boxes in the POS Profile.
1. A default Warehouse needs to be set to complete the transaction.
1. If it's set in both item and POS profile, the one in POS Profile will be given preference.
1. Do note that you need to have a stock of items in your Warehouse before you can sell.
1. When all items are added, click on Pay.
1. Select the payment mode, Submit
1. You can then print the POS invoice.

### 2. Features
#### 2.1 Different sections of the POS

  * Update Stock: If this is checked, Stock Ledger Entries will be made when you “Submit” this Sales Invoice thereby eliminating the need for a separate Delivery Note.
  * In your Items table, update inventory information like Warehouse (saved as default), Serial Number, or Batch Number if applicable.
  * Update Payment Details like your Bank / Cash Account, Paid amount etc.
  * If you are writing off certain amount. For example when you receive extra cash as a result of not having exact denomination of change, check on ‘Write off Outstanding Amount’ and set the Account.

#### 2.2 Customer
In POS, user can select the existing customer during making an order or create the new customer. This features works in the offline mode also. User can also add the customer details like contact number, address details etc on the form. The customer which has been created from the POS will be synced when the internet connection is active.

<img class="screenshot" alt="POS Customer" src="{{docs_base_url}}/assets/img/accounts/pos-customer.png">

#### 2.3 Adding an Item
At the billing counter, the retailer needs to select Items which the consumer buys. In the POS interface you can select an Item by two methods. One, is by clicking on the Item image and the other, is through the Barcode / Serial No.

**Select Item** \- To select a product click on the Item image and add it into the cart. A cart is an area that prepares a customer for checkout by allowing to edit product information, adjust taxes and add discounts.

**Barcode / Serial No** \- A Barcode / Serial No is an optical machine-readable representation of data relating to the object to which it is attached. Enter Barcode / Serial No in the box as shown in the image below and pause for a second, the item will be automatically added to the cart.

<img class="screenshot" alt="POS Item" src="{{docs_base_url}}/assets/img/accounts/pos-item.png">

> Tip: To change the quantity of an Item, enter your desired quantity in the
quantity box. These are mostly used if the same Item is purchased in bulk.

If your product list is very long use the Search field, type the product name
in Search box.

#### 2.4 Removing an Item from the Cart
1. Select row in the cart and clik on delete button in the numeric keypad

    <img class="screenshot" alt="POS Item" src="{{docs_base_url}}/assets/img/accounts/pos_deleted_item.gif">


2. Set Qty as zero to remove Item from the POS invoice. There are two ways to remove an Item.
  * If Item's Qty is 1, click on a minus sign to make it zero.
  * Manually enter 0(zero) quantity.

#### 2.5 Make Payment

After all the Items and their quantities are added into the cart, you are
ready to make the Payment. Payment process is divided into 3 steps -

  1. Click on “Make Payment” to get the Payment window.
  2. Select your “Mode of Payment”.
  3. Click on “Pay” button to Save the document.

<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/pos-payment.png">

Submit the document to finalise the record. After the document is submitted,
you can either print or email it directly to the customer.

#### 2.6 Write off Amount

Outstanding amount can be write off from the POS, user has to enter the amount under write off field on the payment screen.

<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/write-off.png">

System books the write off amount into the ledger which has selected on the POS Profile.

#### 2.7 Change Amount

POS calculate the extra amount paid by the customer, which user can return from the cash account. User has to set the account for the change amount on the POS profile.

<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/change-amount.png">

#### 2.8 Offline POS

In the retails business, invoicing needs to done very quickly, hence should less dependency. In the ERPNext, you can create POS Invoices, even when not connected to the internet.

POS Invoices created in the offline mode will be saved locally in the browser. If internet connection is lost which creating POS Invoice, you will still be able can proceed forward. Once internet connection is available again, offline invoices will be synced, and pushed onto your ERPNext account. To learn more on how POS Invoices can be created when offline, [check here.](https://frappe.io/blog/blog/erpnext-features/offline-pos-in-erpnext-7)

#### 2.9 Offline Records
All the records from the POS stores into the browser's local storegae and sync submitted records after every minute of the interval if system is connected to internet. User can view the offline records by clicking on Menu > View Offline Records

<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/offline-records.png">

#### 2.10 Accounting entries (GL Entry) for a Point of Sale:

Debits:

  * Customer (grand total)
  * Bank/Cash (payment)

Credits:

  * Income (net total, minus taxes for each Item)
  * Taxes (liabilities to be paid to the government)
  * Customer (payment)
  * Write Off (optional)
  * Account for Change Amount (optional)

To see entries after “Submit”, click on “View Ledger”.

#### 2.11 Email
User can send email from the POS, after submission of an order, user has to click on menu > email
<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/pos-email.png">
After sync of an order, email sent to the customer with the print of the bill in the attachment


#### 2.12 POS Closing Voucher

At the end of its shift, the cashier can close his/her PoS by creating a POS Closing Voucher.
Click on the menu and select "Close the POS"
Select the period, your POS Profile and your user to retrieve all sales registered.

<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/pos-closing-voucher.png">

Enter the collected amount for each mode of payment.
If you notice any difference between the theoretical amount and the collected amount, create a difference posting.

#### 3. Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Order](/docs/user/manual/en/buying/purchase-order)
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Payments](/docs/user/manual/en/accounts/payments)
1. [Payment Request](/docs/user/manual/en/accounts/payment-request)
