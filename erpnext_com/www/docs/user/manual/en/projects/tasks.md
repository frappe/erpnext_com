<!-- add-breadcrumbs -->
# Tasks

Project is divided into Tasks. 
In ERPNext, you can also create a Task independently.

<img class="screenshot" alt="Task" src="{{docs_base_url}}/assets/img/project/task.png">

### Status of the Task

A Task can have one of the following statuses - Open, Working, Pending Review, Closed, or Cancelled.

<img class="screenshot" alt="Task - Status" src="{{docs_base_url}}/assets/img/project/task_status.png">

* By default each new Task created has the status set to 'Open'.

* If a Time Log is made against a task, its status will be set to 'Working'.

### Dependent Task

You can specify a list of dependent tasks under the 'Depends On' section.

<img class="screenshot" alt="Depends On" src="{{docs_base_url}}/assets/img/project/task_depends_on.png">

* You cannot close the parent task until all dependent tasks are closed.

* If the dependent tasks are delayed and overlap with the expected Start Date of the Parent task, the system will reschedule the parent task.

### Managing Time

ERPNext uses [Timesheet](/docs/user/manual/en/projects/timesheet/timesheet-against-project) to track the progress of a Task.

You can create multiple Timesheets against each task.
The Actual Start and End Time along with the costing is updated based on the Timesheet.

* To view Timesheet made against a Task click on 'View' -> "Timesheet"

<img class="screenshot" alt="Task - View Timesheet" src="{{docs_base_url}}/assets/img/project/task_view_timesheet_log.png">

<img class="screenshot" alt="Task - Timesheet List" src="{{docs_base_url}}/assets/img/project/task-timesheet-list.png">

* You can also create a Timesheet directly and link it to the Task. 

<img class="screenshot" alt="Task - Link Timesheet" src="{{docs_base_url}}/assets/img/project/task-timesheet-link.png">

* It can be linked to an Employee as well, since Salary Slips can also be generated on basis of Timesheet. Notice that the Timesheet name is intuitively updated to the Employee's name so that accessibility is easier.

<img class="screenshot" alt="Task - Link Timesheet Employee" src="{{docs_base_url}}/assets/img/project/task-timesheet-emp-link.png">


### Managing Expenses

You can book [Expense Claim](/docs/user/manual/en/human-resources/expense-claim.html) against a task.
The system shall update the total amount from expense claims in the costing section.

* To view Expense Claims made against a Task click on 'Expense Claims'

<img class="screenshot" alt="Task - View Expense Claim" src="{{docs_base_url}}/assets/img/project/task_view_expense_claim.png">

* You can also create a Expense Claims directly and link it to the Task.

<img class="screenshot" alt="Task - Link Expense Claim" src="{{docs_base_url}}/assets/img/project/task_expense_claim_link.png">

* Total amount of Expense Claims booked against a task is shown under 'Total Expense Claim' in the Task Costing Section

<img class="screenshot" alt="Task - Total Expense Claim" src="{{docs_base_url}}/assets/img/project/task_total_expense_claim.png">

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/IxY-rSJsA6U?end=126rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

{next}
