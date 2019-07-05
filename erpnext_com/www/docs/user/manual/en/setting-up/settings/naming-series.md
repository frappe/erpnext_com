<!-- add-breadcrumbs -->
# Naming Series

Data records are broadly classified as “Masters” or “Transaction”. A master
is a record that has a “name”, for example, Customer, Item, Supplier,
Employee, etc.

A Transaction is a record that has a “number”, for example, Sales Invoices, Quotations, etc. Transactions are made against a number of master records.

ERPNext allows you to make prefixes to your transactions, with each prefix
forming its own series. For example, a series with prefix INV12 will have
numbers INV120001, INV120002, and so on.

You can have multiple series for all your transactions. It is common to have a
separate series for each financial year. For example in Sales Invoice you
could have:

  * INV120001
  * INV120002
  * INV-A-120002

You can define or select the Naming Series pattern from:

> Home > Settings > Data > Naming Series

## 1. Setting up Naming Series for Documents

1. Select the transaction for which you want to make the series. The system will update the current series in the text box.
2. Edit the series as required with unique prefixes for each series. The first prefix will be the default prefix. Each new prefix must be added on a new line. The newly added naming series will be available in the document.
  ![Multiple naming series](/docs/assets/img/setup/settings/multiple-naming-series.png)
3. If you want the user to explicitly select a series instead of the default one, check the “User must always select” checkbox. There will be no default naming series if this is ticked.

You can also update the starting point of a series by entering the series
name and the starting point in the “Update Series” section.

## 2. Updating Naming Series for Documents

You can change the starting/current sequence number of an existing series.

1. Select the prefix whose sequence is to be changed.
1. The current value will be fetched and displayed.
1. Change starting/existing sequence number if needed.
1. Click on Update Series Number.

For example, if the current Sales Order series number is at 16, and you want to restart or set it as 50, enter 0 or 50 depending on your case. Any new Sales Order created will start from the new sequence number.

> Tip: You could have a separate series for each type of Customer or for
each of your retail outlets.

## 3. Using Custom Fields in Naming Series

Some companies prefer to make use of "short-codes" for suppliers, i.e. WN for company "Web Notes" that later can be used in naming series for quick identification.
 
For example:

    A custom field "Vendor ID" is created under Document: Supplier.
    Then under Naming Series, we allow something like
        PO-.YY.MM.-.vendor_id.-.####
        Resulting in "PO-1503-WN-00001"


<div>
  <div class='embed-container'>
    <iframe src='https://www.youtube.com/embed//IGyISSfI1qU' frameborder='0' allowfullscreen>
    </iframe>
  </div>
</div>


{next}
