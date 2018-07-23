<section class='top-section'>
<h1>Server Support</h1>
</section>

### Server Deployment

The Frappe team will setup or audit your installation based on your requirements depending on the best practices learned from hosting ERPNext since 2010. These include:

- DNS based multi-tenancy
- Setting up of firewall
- Setting up server security rules
- Best practices at time of migration
- Setup of domain and redirects
- Setup of email service
- Setup of uptime notification service like Uptime Robot

### Setup of Master-Slave

If 100% uptime is extremely important to your business, and there could be business losses even if the system is down for a day, we recommend that you setup a master-slave system.

In most cases, if some downtime / data loss is acceptable, a snapshot based backup system should be fine.

In a Master-Slave system, every query in the database is near-instantaneously executed in a parallel server (called slave). So if the main server (master) crashes, you can switch to the slave as the primary server within a few minutes. Also there is much less chance of a data loss.

In the regular snapshot system, you can only recover from the last available snapshot, which might be one day old.

To setup a master-slave system, you will need to provision two identical servers from your datacenter provider, Frappe team will help you setup a master-slave system once you have provisioned the server.

### Upgrade Support

Since ERPNext is 100% free and open source, every new release contains upgrade scripts that will automatically upgrade your system to the latest available version. Under this agreement you can choose to upgrade the system as many times as you want in the contract period. There is no additional cost or license associated with minor or major upgrades of the system.

Frappe recommends that you deploy the latest version every 2-4 weeks. Security and performance updates are pushed continuously and it is best to be on the latest version. The cloud version of ERPNext is always on the latest release.

Upgrade support would include help incase an update breaks or due to:

- Failing patches
- Slow patches
- Dependency issues

When you require upgrade support, you will have to schedule an upgrade with the Frappe team so that someone is available to monitor your upgrade when something fails.

### Major Upgrades

ERPNext upgrades do not usually affect the in-app customizations and permission rules, but this cannot be guaranteed, there may be edge cases where there might be some changes. At the time of major upgrade (example version 10 to version 11), Frappe recommends setting up a test instance to ensure minimum disruption due to customizations.

During this time, Frappe team will also arrange a webinar or sessions which would be beneficial for your ERP champion to attend to understand the impact of new upgrades.

### Bench Manager

We also recommend you install the “Bench Manager”. This is a user-interface driven tool to manage ERPNext Upgrade and backups. With Bench Manager, the ERP Champion or Frappe personnel can trigger an Update remotely without SSH access.

### Scaling Support

As your data scales, some database queries will start becoming a bottleneck. You may need support to optimize your database or analyze how to improve the database performance.

Scaling Support will include:

- Identification of the bottleneck
- Optimizing table indexes (if required)
- Redesign of a feature implementation (if necessary)

### Security Notifications

Frappe will notify you if your current version has any severe security risks and if it needs to be updated immediately. Frappe will also help you in the migration and actively support to fix any issues that may arise.

### Server Migration Crash Recovery

In case of a crashed or poor performing server, Frappe will help you migrate your database and instance from one server to another incase the server is still accessible or help you restore from your last available snapshot backup.

If you have a master-slave setup, Frappe personnel will help you switchover to the slave and setup a new slave, based on availability.

### Server Audit

Frappe team will conduct an audit of your server from time to time to check the performance and health of your server and the implement any preventive maintenance measures including:

- Log review and cleanup
- Review of snapshot backups
- Clearing disk space
- Clear memory
- Database deadlock review

<div class='my-5 text-center'>
	<a href='/contact' class='btn btn-primary'>Get in Touch</a>
</div>