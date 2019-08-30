---
title: Pick List
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: A Pick List is a document that indicates which items should be taken from your inventory to fulfill orders. This is particularly useful for shippers with a large amount of inventory, volume of orders, or customers ordering many SKUs.
 keywords: Pick List, Picking Slip, frappe, Pick Ticket, erpnext new features, erp, open source erp, free erp, stock
---

## Pick List

A Pick List is a document that indicates which items should be taken from your inventory to fulfill orders. This is particularly useful for shippers with a large amount of inventory, volume of orders, or customers ordering many SKUs.

To access Pick List, go to:

> Home > Stock > Pick List

## How does Pick List Work

Pick list selects warehouse where item is available on FIFO (First-In-First-Out) basis.
Selection of warehouse for a batched item is different. In case of batched items, warehouse where the batch is nearer to its expiry will be selected, so it is based on "Expiry First" selection.

## How to create Pick List

1. Go To Pick List, click on New.
1. Set Company.
1. Select the Purpose of Pick List. There are following options under Purpose.

   - **Delivery against Sales Order:** This option will let you add items from Sales Order. After stock picking new delivery note can be created based on the warehouse from which items were picked.

   - **Material Transfer for Manufacture:** This will let you select Work Order from which raw materials will be pulled for picking. You will be presented with an option to select the number of finished goods item for which you want to pick raw materials for. Once the stock picking is done you can create Stock Entry for the picked items i.e., raw materials.

   - **Material Transfer:** This will let you select Material Request for which you want to pick items for. After stock picking you can create Stock Entry with stock entry type for the picked items.

1. Parent Warehouse: If parent warehouse is selected, warehouses only under that parent warehouse will be suggested.

1. Get Item Locations: Once items to be picked is finalized you can click on the get item locations button to get warehouse selection for each item. Since warehouse will be automatically fetched if you get item from any reference document, this button can be useful when you manually add additional item or change the quantity of the existing items in the item locations table.

1. Item Locations: This will have the information of the item location (warehouse), serial no for serialized items and batch no for batched items.

### Create Pick List from Sales Order

1. Go to Sales Order.
1. Click on **Create** button on the top right of the form and then click **Pick List** option.
1. Once you click Pick List, all the data required for Pick List will be fetched from Sales Order.
1. You should be able to see the item locations table with the warehouse selected for each item.
1. Save this document and it can used for stock picking.
1. Submit the document once the stock picking is done and picked item quantities are updated in the document.

> **Note:**
>
> - Pick list can only be created for Sales Orders which has pending items to be delivered.
> - Further document like Delivery Note can be created only if the Pick List is submitted.

### Create Pick List from Multiple Sales orders

1. Go to Pick List, click on New.
1. Set Company.
1. Select the Purpose of Pick List as **Delivery Against Sales Order**.
1. Set Customer.
1. Now click the **Get Items** button on the top right of the form.
1. You'll get the list of all the sales order for the selected customer. From here you can select multiple Sales Orders.
1. All items from the selected Sales Orders will be pulled to the item locations table with warehouse for each item.
1. Save the document and then this document can be forwarded to stock picker.
1. Submit the document once the stock picking is done and picked item quantities are updated in the document.

> **Note:**
>
> - Pick list can only be created for Sales Orders which has pending items to be delivered.
> - Further document like Delivery Note can be created only after the Pick List is submitted.

### Create Pick List from Work Order

1. Go to Work Order.
1. Click **Create Pick List** button.
1. You'll see the dialog box asking for the quantity of Finished Goods Item. This is required to calculate the number raw material items required to manufacture the entered quantity of Finished Goods Item.
1. You should be able to see the item locations table with the warehouse selected for each raw material item.
1. Save this document and then this document can be forwarded to stock picker.
1. Submit the document once the stock picking is done and the picked item is updated in the document accordingly.

> **Note:**
>
> - Pick list can only be created for Work Orders that are still in the state of 'Not Started' or 'In Progress'.
> - Further document like Stock Entry can be created only after the Pick List is submitted.

### Create Pick List from Material Request

> Home > Material Request > Pick List


### Create Delivery Note from Pick List

### Create Stock Entry from Pick List

Pick list will suggest the location to be picked.
This stores all the information required about the item to be picked