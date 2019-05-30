<!-- add-breadcrumbs -->

### What is Energy Point System?
Energy Points System is basically a rating/karma system that you can enable for your organization. This system can be used to track performance of a user.

> To enable Energy Point System go to `Energy Point Settings` > check `Enabled`.


### How to use Energy Point System?
To start using this system you need to [create some Energy Point Rules](#how-to-create-energy-point-rules?) so that user can get energy points based on their activities.

### What is Energy Point Rules?
Energy Point Rules store the information about the activity and the value of points to be alloted.

Energy Point Rule has following fields:

| Field        | Description  |
| ------------- |:-------------|
| Reference DocType      | Document Type you want to apply rule on eg. Task, ToDo, Issue, etc. |
| Condition      | Condition for the point allocation. <br>eg. `doc.status == 'Closed'`<br>The above condition will check whether the `status` field in the document is 'Closed' and if yes then the points will be alloted to the user.       |
| Points | Points to be alloted.      |
| User Field | Field from which user will be selected eg. `Resolved By`, `Modified By`, `Owner`, etc. can be used.      |
| Multiplier Field | Field which stores value for multiplier. This field must have numeric value, this will be multiplied with Points defined in the rule.      |

> **Note:** User Field and Multiplier Field are fetched from the reference doctype.

### How to create Energy Point Rules?

Go To Awesome Bar > search for Energy Point Rules > Create New
<!-- Since almost all work can be tracked through Document Types, you can apply rules on Document Type with some conditions.
So when a document matches the provided condition, user will get the points defined in the rule. -->

Check following example rule:
<img class="screenshot" src="/docs/assets/img/energy-point-system/issue-closed-rule.png">
The screenshot above is the rule for **Issue Closing**.
So when any user closes the issue he/she will be rewarded with **10** points.

Other cases can be covered similarly,

Suppose, you want to create a rule where user gets points on completing a task,
you can do so by creating following rule
<img class="screenshot" src="/docs/assets/img/energy-point-system/task-complete-rule.png">


### Features:

#### 1. Auto Point allocation
Based on created energy point rules user's will be automatically get points when they do certain activity.

#### 2. Review System
Review system can be used to "Appreciate" or "Criticize" someone's work.

Check out following GIF for the review process.
<img class="screenshot" src="/docs/assets/img/energy-point-system/review-system.gif">
For reviewing, user needs to have review points which can be assigned by System Manager through `Energy Point Settings`

#### 3. Leaderboard
> Social Home > Leaderboard (in side navigation bar)

Leaderboard shows user's standing in the organization.

<img class="screenshot" src="/docs/assets/img/energy-point-system/leaderboard.png">
