 <!-- add-breadcrumbs -->
# Event Streaming

Event Streaming enables inter site communications.

From version 13, you can **subscribe** to DocTypes and **stream** documents between different sites.

For Example: If you have 4-5 companies hosted on different sites, one among them is the main site where you want to do ledger posting and others where sites where the Sales Invoices are generated. You could use Event Streaming in this case. For this, your child companies can subscribe to the main company for Item, Customer and Supplier DocTypes and the main company can subscribe to the child companies for Sales Invoices.

To access Event Streaming, go to:
> Home > Integrations > Event Streaming

## 1. How to set up Event Streaming

### 1.1 Create an Event Producer
1. The site which you want to subscribe to is called as the Event Producer. Create an Event Producer document for the site you wish to get the updates from.
2. Go to: **Home > Integrations > Event Streaming > Event Producer**.
3. Enter the site URL of the site you want to subscribe to in the Producer URL field.
4. Add all the DocTypes you want to subscribe to, in the Event Configuration child table.
5. If you want to have the created documents with the same name as it is on the remote Event Producer site, check the 'Use Same Name' checkbox in the child table against the required DocTypes.
6. Set the Event Subscriber field to a user that will be used to create the documents fetched from the Event Producer. You need to create the same user both ways, i.e on the Event Consumer as well as the Event Producer site before creating the Event Producer.
7. Save.
8. The API key and API secret are then set in the Event Producer document for Authentication.

    ![Event Producer](/docs/assets/img/setup/integrations/event-producer-doc.png)

### 1.2 Approve Event Consumer on the Event Producer site
1. After the Event Producer has been created, an Event Consumer automatically gets created on the other site. By default all the Subscribed Document Types have the status as 'Pending'. In order to enable the Event Consumer to consume the documents of these DocTypes, their Status needs to be updated to 'Approved'.
2. Go to: **Home > Integrations > Event Streaming > Event Consumer**.
3. Once you open the Event Consumer document you will see all the DocTypes that have subscribers. Change the status from 'Pending' to 'Approved' for all the DocTypes that you want to approve to be consumed. You can change the status to 'Rejected' if you do not want the documents of that DocType to be consumed.
4. Save.

    ![Event Consumer](/docs/assets/img/setup/integrations/event-consumer-doc.png)

**Note**: Document updates for Subscribed DocTypes won't be synced unless they are Approved.

## 2. Features

### 2.1 Update Log
Update Log logs every create, update, delete for documents that have consumers on the Event Producer site.
In order to view the Update Log:

Go to: **Home > Integrations > Event Streaming > Update Log**.

- For 'Create' type the Update Type, DocType, Document Name and the entire document (as json) is logged.
- For 'Update' type the Update Type, DocType, Document Name and the updated data (difference between the previous state and current state of the document) is logged.
- For 'Delete' type only the Update Type, DocType and Document Name is logged.

![Update Log](/docs/assets/img/setup/integrations/event-update-log-doc.png)

### 2.2 Event Sync Log
Like the Update Log, Event Sync Log logs every document synced from the Event Producer on the Event Consumer site.
In order to view the Event Sync Log:

Go to: **Home > Integrations > Event Streaming > Event Sync Log**.

![Event Sync Log](/docs/assets/img/setup/integrations/event-sync-log.png)

A successfully synced event generates a log document with:

- **Update Type**: Create, Update or Delete
- **Status**: Sync Status
- **DocType**
- **Event Producer**: The site URL from where the document was synced
- **Document Name**
- **Remote Document Name**: If 'Use Same Name' is unchecked
- **Use Same Name**
- **Data**: The document data as JSON

    ![Event Sync Log](/docs/assets/img/setup/integrations/event-synced.png)

A failed event generates a log doc with the above fields along with:

- **Error**: The error because of which the document was not synced.
    ![Event Synced](/docs/assets/img/setup/integrations/event-failed-error.png)

- **Retry Button**: It also provides a 'Resync' button in order to resync the failed event.
    ![Event Failed](/docs/assets/img/setup/integrations/event-failed.png)

### 2.3 Dependency Syncing
Certain DocTypes have dependencies. For example, before syncing a Sales Invoice, the Item and Customer need to be present in the current site. So, Item and Customer are dependencies for Sales Invoice. Event Streaming handles this by on demand dependency syncing. Whenever any document is to be synced, it first checks whether the document has any dependencies (Link fields, Dynamic Link fields, Child Table fields, etc.). If that dependency is not fullfilled i.e. the dependent document (eg: Item) is not present on your consumer site, it will be synced first and then the Sales Invoice will be synced.

For example: Sales Invoice syncing with Item dependency
    ![Event Dependency](/docs/assets/img/setup/integrations/event-dependency-sync.gif)

### 2.4 Naming Configuration
Check the 'Use Same Name' checkbox to let the documents have same name on both Event Producer and Event Consumer sites. If this is not checked, then the document will be created using the naming conventions of the current site.

![Use Same Name Config](/docs/assets/img/setup/integrations/event-use-same-name.png)

**Note**: For DocTypes that have naming series, it is adviced to keep the 'Use Same Name' checkbox unchecked, to prevent naming conflicts. If this is unchecked, the Documents are created by following the naming conventions on the current site and the 'Remote Site Name' and 'Remote Document Name' custom fields are set to store the Event Producer site name URL and the document name on the remote site respectively.

![Subscribed Document](/docs/assets/img/setup/integrations/event-subscribed-doc.png)

### 2.5 Mapping Configuration
If you want to stream documents between an ERPNext instance and another Frappe app for a particular DocType which has the same structure but fieldnames are different in both the sites, you can use Event Streaming with Mapping Configuration.
For this you need to first set up a Document Type Mapping:

- **Mapping Name**: Give a unique name to the mapping
- **Local Document Type**: The DocType in your current site
- **Remote Document Type**: The DocType in the Event Producer site which you want to sync.

In the Field Mapping child table:

- **Local Fieldname**: The fieldname in the Local Document type of your current site.
- **Remote Fieldname**: The fieldname in the Remote Document type of the Event Producer site which you want to map to the Local Fieldname

![Document Type Mapping](/docs/assets/img/setup/integrations/event-field-mapping.png)

- **Is Child Table**: If the field you are trying to map is a child table, you need to check this.
- **Child Table Mapping**: Create another Document Type Mapping for the child table fields and select it here.

![Child Table Mapping](/docs/assets/img/setup/integrations/event-map-is-child-table.png)

After this, check the 'Has Mapping' checkbox in the Event Configuration child table in Event Producer against the required DocType and select the Document Type Mapping you just created.

![Mapping Configuration](/docs/assets/img/setup/integrations/event-mapping-conf.png)