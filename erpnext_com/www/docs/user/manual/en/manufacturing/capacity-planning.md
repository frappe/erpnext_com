<!-- add-breadcrumbs -->
# Capacity Planning

Capacity planning is the process where an organization decides whether to accept the new orders or not based upon the resources and the existing work.

Capacity planning has been enabled by default in your account, to know more go to:

> Home > Manufacturing > Settings > Manufacturing Settings

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/capacity_planning_settings.png">

## 1. Prerequisites
Before creating and using a Work Order, it is advised that you create the following first:

* [Bill Of Materials](/docs/user/manual/en/manufacturing/bill-of-materials)
* [Operation](/docs/user/manual/en/manufacturing/operation)
* [Workstation](/docs/user/manual/en/manufacturing/workstation)
* [Work Order](/docs/user/manual/en/manufacturing/work-order)

## 2. How Capacity Planning Works in ERPNext
The user has to define the number of days in the "Capacity Planning For" under manufacturing settings to plan the upcoming work orders. For example, if you have kept the Capacity Planning For 30 days and to make 1 finished good required 5 days then on the current date user can only accept the 6 work orders. You can take the next work order when your work station gets free.

### 2.1 Create Work Order With Operations
User need to create the work orders with the operation so that the system will track the job card timings against the work order.

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/work_order_with_operations.png">

Once the user submits the work order system will generate the job card with the available workstation's time details. If Allow Overtime is disabled in the manufacturing settings then the system schedules the job as per the timings defined in the work station. If "Allow Production on Holidays" is disabled then the system schedules job on working days only.

### 2.2 Workstation's Production Capacity

In the workstation, the user can set the "Production Capacity" in a number so that the system will allow you to do work on the same number of jobs at a time.

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/work_station_capacity.png">

### 2.3 Job Card With Timing
The system will auto-create the job card with timing against each operation based upon the time required to complete that operation and workstation's availability. The user has to set the planned start date and based upon the operation time system calculate the planned end date.

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/job_card_timing.png">

### 2.4 Work Order Planned Start Date and End Date
Based upon the planned start date and end date users will calculate the capacity of their work stations. Also, they can track the status of the work order using the calendar.

To view calendar, goto:

> Work Order List > Calendar > Default

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/work_order_calendar.png">

### 2.5 Capacity Planning Error
If capcity days is less than time required to complete the opertion then system throws the capcity planning error. In that case user has to increase the number of ""Production Capacity"" days in the manufacturing settings or reduce the number of finished goods as per the capcity of the workstations.

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/capacity_planning_error.png">
