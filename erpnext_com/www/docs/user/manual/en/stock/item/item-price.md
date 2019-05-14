<!-- add-breadcrumbs -->
# Item Price

Item Price is the record in which you can log selling and buying rate of an item.

There are two ways to reach to new Item Price form.

> Selling/Buying/Stock > Setup > Item Price > New Item Price

Or

> Item > Add/Edit Prices > Click on "+"  > New Item Price

Following are the steps to create new Item Price.

Step 1: Select Price List

You can create multiple Price List in ERPNext to track Selling and Buying Price List of an item separtely. Also if item's selling prices id changing based on territory, or due to other criteria, you can create multiple selling Price List for it.

![Item Price list](/assets/img/stock/item-price-1.png)

On selection of Price List, its currency and for selling or buying property will be fetched as well.

To have Item Price fetching in the sales or purchase transaction, you should have Price List id selected in the transaction, just above Item table.

Step 2: Select Item
Select item for which Item Price record is to be created. On selection of Item Code, Item Name and Description will be fetched as well.

Step 3: Enter Rate

Enter selling/buying rate of an item in Price List currency.

Step 4: Save Item Price

Below GIF captures this process:

<img class="screenshot" alt="Item Price" src="{{docs_base_url}}/assets/img/stock/item-price.gif">

To check all Item Price together, go to:

> Stock > Main Report > Itemwise Price List Rate

You will find option to create new Item Price record (+) in this report as well.

<div>
    <div class="embed-container">
        <iframe src='https://www.youtube.com/embed/FcOsV-e8ymE?start=193' frameborder='0' frameborder='0' allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
</div>

{next}
