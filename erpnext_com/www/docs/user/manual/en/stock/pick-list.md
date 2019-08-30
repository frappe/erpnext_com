---
title: Pick List
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: A pick list is a document that indicates which items should be taken from your inventory to fulfill orders. This is particularly useful for shippers with a large amount of inventory, volume of orders, or customers ordering many SKUs.
 keywords: Pick List, Picking Slip, frappe, Pick Ticket, erpnext new features, erp, open source erp, free erp, stock
---

## Pick List

A pick list is a document that indicates which items should be taken from your inventory to fulfill orders. This is particularly useful for shippers with a large amount of inventory, volume of orders, or customers ordering many SKUs.

To access Pick List, go to:

> Home > Stock > Pick List

## How to create Pick List

1. Click on New.
1. Set Company.
1. Select the Purpose of Pick List. There are following options under Purpose.

  - **Delivery against Sales Order:** This will let you add items from Sales Order. Pick list will suggest the location to be picked. After stock picking new delivery note can be created based on the warehouse from which items were picked
  - **Material Transfer for Manufacture:** This will let you select Work Order from raw materials will be pulled for picking. There will be an option to select the no. of finished goods item for which you want to pick raw materials for. Once the stock picking is done you can create Stock Entry for the picked items(raw materials).
  - **Material Transfer:** This will let you select Material Request for which you want to pick items for. After stock picking you can create Stock Entry for the picked items.

1. Parent Warehouse: If parent warehouse is selected, items only under that warehouse will be suggested.
1. Get Item Locations: Once the items to be picked is finalized you can click on the get item locations button to populate item locations table. This stores all the information required about the item to be picked.
1. Item Locations: This will have the information of the item location (warehouse), serial no for serialized items and batch no for batched items.

### Create Pick List from Sales Order

> Home > Sales Order > Pick List

### Create Pick List from Work Order

> Home > Work Order > Pick List

### Create Pick List from Material Request

> Home > Material Request > Pick List
