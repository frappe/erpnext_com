<!-- add-breadcrumbs -->
# Item Variants

A Item Variant is a version of an Item, such as differing sizes or differing colors (like a _blue_ t-shirt in size _small_ rather then just a t-shirt).
Without Item variants, you would have to treat the _small, medium_ and _large_ versions of a t-shirt as three separate Items;
Item variants let you treat the _small, medium_ and _large_ versions of a t-shirt as variations of the one Item 't-shirt'.

### 1. Using Item Variants

Variants can be based on two things:

1. Item Attributes
1. Manufacturers

### 2. Item Variants Based on Item Attributes

To use Item Variants in ERPNext, create an Item and check 'Has Variants'.

 The Item shall then be referred to as a so called 'Template'. Such a Template is not identical to a regular 'Item' any longer. For example it (the Template) can not be used directly in any Transactions (Sales Order, Delivery Note, Purchase Invoice) itself. Only the Variants of an Item (_blue_ t-shirt in size _small)_ can be practically used in such. Therefore it would be ideal to decide whether an item 'Has Variants' or not directly when creating it.

<img class="screenshot" alt="Has Variants" src="{{docs_base_url}}/assets/img/stock/item-has-variants.png">

On selecting 'Has Variants' a table shall appear. Specify the variant attributes for the Item in the table. In case the attribute has Numeric Values, you can specify the range and increment values here.

<img class="screenshot" alt="Valid Attributes" src="{{docs_base_url}}/assets/img/stock/item-attributes.png">

> Note: You cannot make Transactions against a 'Template'

To create 'Item Variants' against a 'Template' select 'Make Variants'.

<img class="screenshot" alt="Make Variants" src="{{docs_base_url}}/assets/img/stock/make-variant.png">

<img class="screenshot" alt="Make Variants" src="{{docs_base_url}}/assets/img/stock/make-variant-1.png">

To learn more about setting Attributes Master check [Item Attributes](/docs/user/manual/en/stock/setup/item-attribute)

### 3. Item Variants Based on Manufacturers

To setup variants based on Manufacturers, in your Item template, set "Variants Based On" as "Manufacturers"

<img class='screenshot' alt='Setup Item Variant by Manufacturer'
	src='{{docs_base_url}}/assets/img/stock/select-mfg-for-variant.png'>

When you make a new Variant, the system will prompt you to select a Manufacturer. You can also optionally put in a Manufacturer Part Number

<img class='screenshot' alt='Setup Item Variant by Manufacturer'
	src='{{docs_base_url}}/assets/img/stock/set-variant-by-mfg.png'>

The naming of the variant will be the name (ID) of the template Item with a number suffix. e.g. "ITEM000" will have variant "ITEM000-1"

### 4. Update Item Variants Based on Template
To update the value in the variants items from the template item, select the respective fields first in the Item Variant Settings page. After that system will update the value of that fields in the variants if that values has been changed in the template item.

To set the fields Goto **Stock > Items and Pricing > Item Variant Settings**.
<img class='screenshot' alt='Item Variant Settings'
	src='{{docs_base_url}}/assets/img/stock/item_variants_settings.png'>

<div class="embed-container">
	<iframe src="https://www.youtube.com/embed/kogIricF40I?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
	</iframe>
</div>

#### 5. Related Topics
1. [Item Group](/docs/user/manual/en/stock/item-group)
1. [Item Attribute](/docs/user/manual/en/stock/item-attribute)
1. [Item Price](/docs/user/manual/en/stock/item-price)
1. [Item Codification](/docs/user/manual/en/stock/item-codification)
