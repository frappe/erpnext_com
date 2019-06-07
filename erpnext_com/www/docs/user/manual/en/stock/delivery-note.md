<!-- add-breadcrumbs -->
# Delivery Note

A Delivery Note is made when a shipment is shipped from the company’s
Warehouse.

A copy of the Delivery Note is usually sent with the transporter. The Delivery
Note contains the list of Items that are sent in the shipment and updates the
inventory.

### 1. How to create a Delivery Note
The entry of the Delivery Note is very similar to a Purchase Receipt. To create a delivery note:

1. Go to **Stock > Stock Transactions > Delivery Note > New**.
1. Select the Customer.
1. Select the Items and quantities in the Items table.
1. The UOM and Rates will be fetched automatically.
1. Save and Submit.

Or, from a “Submitted” Sales Order (that is not shipped) by clicking on
“Make Delivery Note”.

<img class="screenshot" alt="Delivery Note" src="{{docs_base_url}}/assets/img/stock/delivery-note.png">

You can also “fetch” the details from an unshipped Sales Order.

You will notice that all the information about unshipped Items and other
details are carried over from your Sales Order.

### 2. Related Actions
#### 2.1 Shipping Packets or Items with Product Bundle

If you are shipping Items that have a [Product Bundle](/docs/user/manual/en/selling/setup/product-bundle), ERPNext will automatically create a “Packing List” table for you based on the sub-Items in that Item.

If your Items are serialized, then for Product Bundle type of Items, you will have
to update the Serial Number in the “Packing List” table.

#### 2.2 Packing Items into Cases, for Container Shipment

If you are doing container shipment or by weight, then you can use the Packing
Slip to breakup your Delivery Note into smaller units. To make a Packing Slip
go to:

**Stock > Tools > Packing Slip > New Packing Slip**

You can create multiple Packing Slips for your Delivery Note and ERPNext will
ensure that the quantities in the Packing Slip do not exceed the quantities in
the Delivery Note.

* * *

##### Q1 How to Print Without Amount?

If you want to print your Delivery Note without the amount (this might be
useful if you are shipping high value items), check the “Print without
Amount” box in the “More Info” section.

##### Q2 What happens when the Delivery Note is “Submitted”?

A Stock Ledger Entry is made for each Item and stock is updated. Pending
Quantity in the Sales Order is updated (if applicable).

##### Q3 How to not allow the creation of delievery notes without a sales order against it ?

Go to **Selling > Selling Settings > Sales Order Required**, then turn this setting to Yes.

#### 3. Related Topics
1. [Warehouse](/docs/user/manual/en/stock/warehouse)
1. [Delivery Note Stock Error](/docs/user/manual/en/stock/articles/delivery-note-stock-error)
1. [Material Transfer From Delivery Note](/docs/user/manual/en/stock/articles/material-transfer-from-delivery-note)
