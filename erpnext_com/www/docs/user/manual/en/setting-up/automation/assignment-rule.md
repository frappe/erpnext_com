<!-- add-breadcrumbs -->

# Assignment Rule

You can set up automatic assignment of documents to users by creating an **Assignment Rule**.

> Introduced in Version 12

To access Assignment Rule, go to:
> Home > Settings > Workflow > Assignment Rule

## 1. How to create an Assignment Rule
To set up an automatic assignment:

1. Click on New.
1. Select the Document Type you want to assign automatically (for example **Issue**).
1. Write the "Description" that will be added to the To Do.
1. Select the condition for assignment (refer the section below(#assign/unassign-conditions)).
1. Select the assignment rule (**Round Robin** or **Load Balancing**).
1. Select the list of users to whom this Assignment Rule will apply.


You can use properties of the document in description that will be part of the assignment. Higher 'Priority' Assignment Rules will be applied first.

Example:

High Priority Issue -> "{{ name }}" has been assigned to you.

### 1.1 Assign/Unassign Conditions

You can write simple Python expressions for automatic assignment in the `Assign Rule` and `Unassign Rule`. You will have access to all the properties of the document and can use operators like >, <, ==, etc and also multiple conditions like `and` and `or`

Examples:

- `status == "Open"`
- `issue_type == "Technical" and priority=="High" and status == "Open"`

### 1.2 Assignment Rules

There are 2 rules:

1. **Round Robin**: Assign each document to a user in sequence.
2. **Load Balancing**: Assign new documents to the user who has the least number of assignments.

### 1.3 Multiple Assignment Rules

You can also setup multiple auto assignments for each Document Type, the one with the highest Priority will be applied first:

Here is an example of an Assignment Rule.

Set Document Type, Descriptions and Conditions.
<img class="screenshot" alt="Assign" src="{{docs_base_url}}/assets/img/setup/automation/auto-assign-1.png">


Set Rule and Users:
<img class="screenshot" alt="Assign" src="{{docs_base_url}}/assets/img/setup/automation/auto-assign-2.png">

{next}