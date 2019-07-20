# Production Plan

Production Plan helps user to plan production against multiple sales orders or the material requests. Also, it helps in Material Procurement planning for the raw-material item, based on the quantity of finished product to be manufactured.

To use the Production Plan, go to:

> Manufacturing > Production > Production Plan

<img class="screenshot" alt="Production Plan" src="{{docs_base_url}}/assets/img/manufacturing/production_plan.png">

## Planning for Production

### Production Against Sales Orders

* Select option as Sales Order from the drop down list of get items from. System will show the filters, using that we can pull the sales orders for the production.

<img class="screenshot" alt="Sales Order Filters" src="{{docs_base_url}}/assets/img/manufacturing/sales_order_filter.png">

* Click on Get Sales Orders to fetch sales orders based on above filters

<img class="screenshot" alt="Sales Orders" src="{{docs_base_url}}/assets/img/manufacturing/sales_orders.png">

* Click on Get Items for Work Order to fetch the items from the above sales orders.

<img class="screenshot" alt="Sales Order Item" src="{{docs_base_url}}/assets/img/manufacturing/sales_order_items.png">
	* Include Exploded Items :- To include subassembly items of raw materials in the production.

### Production Against Material Requests

* Select option as Material Request from the drop down list of get items from. System will show the filters, using that we can pull the material requests for the production.

<img class="screenshot" alt="Material Request Filters" src="{{docs_base_url}}/assets/img/manufacturing/material_request_filter.png">

* Click on Get Material Request to fetch material requests based on above filters

<img class="screenshot" alt="Material Requests" src="{{docs_base_url}}/assets/img/manufacturing/material_requests.png">

* Click on Get Items for Work Order to fetch the items from the above material requests.

<img class="screenshot" alt="Material Request Item" src="{{docs_base_url}}/assets/img/manufacturing/material_request_items.png">

## Planning for Material Requests

* Click on get raw materials for production button to fetch raw materials required in the production.

<img class="screenshot" alt="Material Request Plan" src="{{docs_base_url}}/assets/img/manufacturing/material_request_plan.png">

  * <b>Include Non Stock Items</b> :- To add non stock items in the material request planning.
  * <b>Include Subcontracted Items</b> :- To add subcontracted item's raw materials if include exploded items is disabled
  * <b>Ignore Existing Projected Quantity</b> :- If enabled then system will creates the material request even if the user has already ordered or requested the respective items.
  * <b>For Warehouse</b>:- User can set the warehouse for which they wants to create the material request.
  * <b>Download Materials Required</b>:- On click of this, user will get the excel sheet with the raw materials which needs to complete this production plan. User can select the warehouse to check the available quantity in the respective warehouse. If user has kept the For Warehouse as blank then system will gives the excel sheet with raw materials and warehouse wise available quantity of the respective raw materials. Excel sheet will look like as below:

 <img class="screenshot" alt="Material Request Plan" src="{{docs_base_url}}/assets/img/manufacturing/material_request_excel.png"> 

## Provision To Make Work Order and Material Request

Once the production plan is submitted user gets an option to make work orders for the production items and material requests for the raw materials.

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/make_po_mr.png">

### What if user wants to make work order for the sub-assembely items
<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/nokia_phone_bom.png">

* In above example, user creates the Nokia Headphone first and then creates the Nokia Charger and then creates final finished goods. Here user wants to make work order for the Nokia Headphone and Nokia Charger, to do this user has to enable the field "Make Work Order for Sub Assembly Items" in the production plan against the item Nokia Lumia.

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/production_plan_for_subassembely.png">

* On click of make work order, system will generate the work order for the sub assembely items and the foinished good items

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/wo_against_the_production_plan.png">