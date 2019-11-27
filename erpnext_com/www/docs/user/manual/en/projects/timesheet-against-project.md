<!-- add-breadcrumbs -->
#Timesheet against Project and Task

Timesheets can be tracked against Project and Tasks so that you can get reports on how much time was spent on each Task or Project.

If standard working hours are set up in the Company master and the user enters from time and to time, the system would
automatically calculate the number of hours. Eg: standard working hours are set up as 8 at the company level and start
time and end time are 4 days apart, the calculated hours would be 32. If the standard working hours are not set up, then
the system would calculate the hours as 96 hours in this case.

<img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/project/timesheet/timesheet-project.gif">

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/IxY-rSJsA6U?start=126rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>


####Billable Timesheet

To bill Customer based on Timesheet, check "Is Billable" in the Timesheet created against Project and Task. To learn more about billing Customer from Timesheet, click [here](/docs/user/manual/en/projects/sales-invoice-from-timesheet).

User can also make invoice against timesheet by selecting the Project on the invoice. System will fetch the records from the timesheet based on selected project, for mode detail check below video
<iframe width="560" height="315" src="https://www.youtube.com/embed/hVAjtOFFhDI" frameborder="0" allowfullscreen></iframe>

####Project Costing

When creating Timesheet, Employee will have to select an Activity Type. For each Activity Type, you can create an Activity Cost master. In the Activity Cost, Billing Rate and Costing rate is defined for each Employee. 

In the Timesheet, costing will be done based on Activity Cost multiplied with number of hours. Based the Timesheet Cost, total costing will be doen for the Task and Project as well.

To learn about setup of Activity Type and Activity Cost, click [here](/docs/user/manual/en/projects/activity-cost).