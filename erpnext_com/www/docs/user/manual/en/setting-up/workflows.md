<!-- add-breadcrumbs -->
# Workflows

**With workflows you can rewrite how a particular process/workflow is handled in ERPNext.**

In order to allow multiple people to submit multiple requests, for approvals
by multiple users, ERPNext requires you to fill the workflow conditions.
ERPNext tracks the multiple permissions before submission.

Example of a leave application workflow is given below:

If a user applies for leave, then his request will be sent to the HR
department. The HR department (HR User) will either reject or approve this
request. Once this process is completed, the user's Manager (leave approver)
will get an indication that the HR department has Accepted or Rejected. The
Manager, who is the approving authority, will either Approve or Reject this
request. Accordingly, the user will get his Approved or Rejected status.

<img class="screenshot" alt="Workflow" src="{{docs_base_url}}/assets/img/setup/workflow-leave-fl.png">

To make this Workflow and transition rules go to:

> Home > Settings > Workflow > Workflow

## 1. How to create a Workflow
1. Click on New.
1. Enter a name for the Workflow and select the DocType on which to be applied.
1. Enter the different states of Leave Approval Process.

    <img class="screenshot" alt="Workflow" src="{{docs_base_url}}/assets/img/setup/workflow-1.png">

1. Enter the Transition Rules.

    <img class="screenshot" alt="Workflow" src="{{docs_base_url}}/assets/img/setup/workflow-2.png">
1. Under Workflow State Field, enter a name for the Custom Field that'll be added to the DocType, Leave Application in this case.
1. On saving, the Custom Field will be created in the DocType.

### 1.2 Things to note when creating a Workflow

* Creating a workflow essentially overwrites the existing code written for that document. Thus the document will function based on your workflow and not based on the pre-set code settings. Hence there might be no submit button/option if you have not specified it in the workflow.

    If you don't apply workflow to a document, and that document is submittable, then it has the default workflow with states: Draft - Submitted - Cancelled. If you are applying workflow to a submittable document, then those default states should be handled by the user.

* Document statuses: Saved = 0, Submitted = 1, Cancelled = 2.

* A document cannot be canceled unless it is submitted.

* If you wish to give the option to cancel, you will have to write a
workflow transition step that says from submitted you can cancel.

* Workflow States can have different colors according to the state. Eg: Green for success.

### 1.3 Other options for a Workflow
1. Is Active: On ticking this, all other Workflows for the selected DocType become inactive.
1. Don't Override Status: This workflow's status will not override the status of the document (Leave Application) in the list view.
1. Send Email Alerts: Emails will be sent to the user with next possible workflow actions.

## 2. Features

## 2.1 Enable/Disable Optional Workflow State

> Introduced in Version 12

In States, optional workflow state means that the state may not be a part of final approval.

E.g. states like Canceled or Rejected can be optional.
![Optional State](/docs/assets/img/setup/workflow-optional-state.png)

**Note:** Workflow Actions are not created for optional states.

### 2.2 Conditions

> Introduced in Version 11

In Version 11, you can also add a condition for the Transition to be applicable. For example, in this case, if someone applies for a leave of more than 5 days, a particular role must approve. For this to happen in the particular transition, you can set a property for **Condition** under Approved by HR as:

```
doc.total_leave_days <= 5
```
Then if someone applied for leave for less than 5 days, only that particular transition will apply. Here, `total_leave_days` is the field name of the field 'Total Leave Days' of Leave Application. To see the field name of a field go to Menu > Customize.

This can be extended to any property of the document.

## 3. Example of a Leave Application Process:

When a Leave Application is saved by Employee, the status of the document changes to "Applied":

<img class="screenshot" alt="Workflow" src="{{docs_base_url}}/assets/img/setup/workflow-3.png">

When the HR User logs in, he can either Approve or Reject. If approved the
status of the document changes to "Approved by HR". However, it is yet to be approved by Leave Approver.

<img class="screenshot" alt="Workflow" src="{{docs_base_url}}/assets/img/setup/workflow-4.png">

When the Leave Approver opens the Leave Application page, he can finally "Approve" or "Reject" the Leave Application.

<img class="screenshot" alt="Workflow" src="{{docs_base_url}}/assets/img/setup/workflow-5.png">

<div>
    <div class="embed-container">
        <iframe src="https://www.youtube.com/embed/yObJUg9FxFs?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
</div>

### 4. Related Topics
1. [Workflow Actions](/docs/user/manual/en/setting-up/workflow-actions)
1. [Assignment Rule](/docs/user/manual/en/setting-up/automation/assignment-rule)
