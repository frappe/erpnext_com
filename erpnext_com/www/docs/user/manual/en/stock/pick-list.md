---
title: Pick List
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: A Pick List is a document that indicates which items should be taken from your inventory to fulfill orders. This is particularly useful for shippers with a large amount of inventory, volume of orders, or customers ordering many SKUs.
 keywords: Pick List, Picking Slip, frappe, Pick Ticket, erpnext new features, erp, open source erp, free erp, stock
---

## Pick List

**A Pick List is a document that indicates which items should be taken from your inventory to fulfill orders.**

This is particularly useful for shippers with a large amount of inventory, volume of orders, or customers ordering many SKUs.
Pick list selects Warehouse where item is available on FIFO (First-In-First-Out) basis.
Selection of Warehouse for a batched item is different. In case of batched items, Warehouse where the batch is nearer to its expiry will be selected.

To access Pick List, go to:

> Home > Stock > Stock Transactions > Pick List

## 1. Prerequisites

Before creating and using a Pick List, it is advised that you have the following first:

- [Stock Item](/docs/user/manual/en/stock/item)
- [Warehouse](/docs/user/manual/en/stock/warehouse)

## 2. How to create Pick List

1. Go To Pick List, click on New.
1. Set Company.
1. Select the Purpose of Pick List. These are the options under Purpose:

   - **Delivery against Sales Order:** This option will let you add items from a Sales Order. After submitting Pick List a new Delivery Note can be created based on the Warehouse from which items were picked.

   - **Material Transfer for Manufacture:** This will let you select a Work Order from which raw materials will be pulled for picking. You will be presented with an option to select the number of finished goods item for which you want to pick raw materials. After picking the stock you can create Stock Entry for the picked items i.e., raw materials.

   - **Material Transfer:** This will let you select Material Request for which you want to pick items. After picking the stock you can create Stock Entry for the picked items.

1. Add Item and quantity of item you want to pick in the item locations table. You can then click on **Get Item Locations** to get the Warehouse and other details for each item.

1. **Parent Warehouse:** If parent Warehouse is selected, Warehouses only under that parent Warehouse will be suggested.

1. **Get Item Locations:** Once items to be picked is finalized you can click on the **Get Item Locations** button to get Warehouse selection for each item. Since Warehouse will be automatically fetched if you get item from any reference document, this button can be useful when you manually add additional items or change the quantity of the existing items in the Item Locations table.

1. **Item Locations:** This will have the information of the item location (Warehouse), serial number for serialized items and batch no for batched items.
<img class='screenshot' alt='Item Locations' src='{{docs_base_url}}/assets/img/stock/pick-list-item-locations.png'>
<img class='screenshot' alt='Item Location Detail' src='{{docs_base_url}}/assets/img/stock/pick-list-item-location-detail.png'>

1. Save and Submit.
<img class='screenshot' alt='Submitted Pick List' src='{{docs_base_url}}/assets/img/stock/pick-list-submitted-doc.png'>

### 2.1 Create Pick List from Sales Order

1. Go to Sales Order.
1. Click on **Create** button on the top right of the form and then click **Pick List** option.
1. Once you click Pick List, all the data required for Pick List will be fetched from Sales Order.
1. You should be able to see the item locations table with the Warehouse selected for each item.
1. Save this document and it can used for stock picking.
1. Submit the document once the stock picking is done and picked item quantities are updated in the document.

**Tip:** You can create a Pick List for multiple Sales Order from the same Customer. Click on Get Items and select the Sales Orders.

> **Note:**
>
> - Pick list can only be created for Sales Orders which has pending items to be delivered.
> - A **Delivery Note** can be created only if the Pick List is submitted.

### 2.2 Create Pick List from Work Order

1. Go to Work Order.
1. Click **Create Pick List** button.
1. You'll see the dialog box asking for the quantity of Finished Goods Item. This is required to calculate the number raw material items required to manufacture the entered quantity of Finished Goods Item.
<img class='screenshot' alt='Dailog For qty' src='{{docs_base_url}}/assets/img/stock/pick-list-dialog-for-qty.png'>

1. You should be able to see the item locations table with the Warehouse selected for each raw material item.
1. Save this document and then this document can be forwarded to stock picker.
1. Submit the document once the stock picking is done and the picked item is updated in the document accordingly.

> **Note:**
>
> - Pick list can only be created for Work Orders that are still in the state of 'Not Started' or 'In Progress'.
> - A **Stock Entry** can be created only after the Pick List is submitted.

### 2.3 Create Pick List from Material Request

1. Go to Material Request.
1. Click on **Create** button and then click **Pick List** option.
1. You should be able to see the item locations table with the Warehouse selected for each item in Material Request.
1. Save this document and then this document can be forwarded to stock picker.
1. Submit the document once the stock picking is done and the picked item is updated in the document accordingly.

> **Note:**
>
> - Only Material Requests with type 'Material Transfer' can be used for Pick List creation.
> - A **Stock Entry** of type 'Material Transfer' can be created after the Pick List is submitted.

## 3. Related Topics

1. [Sales Order](/docs/user/manual/en/selling/sales-order)
1. [Work Order](/docs/user/manual/en/manufacturing/work-order)
1. [Material Request](/docs/user/manual/en/stock/material-request)

{next}