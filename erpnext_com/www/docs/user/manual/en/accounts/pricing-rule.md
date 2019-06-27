<!-- add-breadcrumbs -->
#Pricing Rule

Pricing Rule is a master where you can define rules based on which discount is applied to specific Customer or Supplier.

Following are the few cases which can be addressed using Pricing Rule.

- As per a promotional sale policy, if customer purchases more than 10 units of an item, he enjoys 20% discount.
- For Customer "XYZ", selling price for the specific Item should be updated as ###.
- Items categorized under specific Item Group has same selling or buying price.
- Customers belonging to specific Customer Group should get ### selling price, or % of Discount on Items.
- Supplier categorized under specific Supplier Group should have ### buying rate applied.

To have Discount and Price List Rate for an Item auto-applied, create Pricing Rules for it.

## 1. How to create a Pricing Rule
1. Go to: **Selling > Items and Pricing > Pricing Rule > New**.
1. Set a title for the rule.
1. Select what to Apply On.
1. Select whether you want to apply price dicount or product discount. If you want to give free products then select the product discount.

<img alt="Applicable On" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-on.png">

1. For a single item, select Item Code and select the items.
1. If you want Pricing Rule to be applied on all the items, select 'Item Group' and select **All Item Group** (parent Item Group).
1. If you have multiple price lists, you can set the priority from 0 to 20.
1. Set whether the Pricing Rule is for Selling of Buying the item.
1. Set what type is this applicable for and select the record. You can set applicability to one of the following masters.

<img alt="Applicable for" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-for.png">

1. Specify minimum qty, maximum qty, minimum amount, maximum amount of an item when this Pricing Rule should be applicable.

<img alt="Applicable Qty" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-qty-amt.png">

1. You can also set a date interval for when the Pricing Rule will be valid. This is useful for a sales promotion.

<img alt="Period" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-period.png">

##2. How to apply the Pricing Rule

###2.1 Price Discount

1. Under the Margin Type, you can set whether the margin is calculated as a percentage or an amount. Eg: 10% margin on supplier price list at the time of sales.

1. Rate or Discount specified in the Pricing Rule will be applied only if above applicability rules are matched with values in the transaction. Rate mentioned in Pricing Rule will be given priority over item's Price List rate.

   <img alt="Applicable Rate" class="screenshot" src="/docs/assets/img/articles/pricing-rule-price.png">

1. Discount Percentage can be applied for a specific Price List (Selling or Buying). To apply it for both, leave the 'For Price List' field blank.

    <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-discount.png">

1. Discount can be set in terms of amount.

    <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-discount-amt.png">

### 2.2 Product Discount

1. "Buy 2 quantities get 1 free quantity of the same item." To configure such type of rules, set the Price or Product Discount as Product discount, tick the Same Item checkbox, and set the quantity.

    <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-same-product-free.png">

1. "Buy 2 quantities get 1 free quantity of the another item." To configure such type of rules. Set the Price or Product Discount as Product discount, untick the Same Item checkbox and set the Free Item and quantity.

    <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-other-product-free.png">

# 3. Scenarios with Pricing Rule
## 3.1 Make Price List
1. Create a new Pricing List by going to **Stock > Price List > New**.
1. Go to **Buying > Supplier** and set the new Price List.
1. Go to **Stock > Item Price** and set a newly created Price List here.
1. Also set the supplier who has the new Price List set.

<img alt="Disable" class="screenshot" src="{{docs_base_url}}/assets/img/articles/price-list.png">

## 3.2 Make Pricing Rule
1. Create a new Pricing Rule.
1. Select the item which has the new Price List set.
1. Tick the Selling checkbox.
1. Save.

<img alt="Disable" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-margin.png">

## 3.3 Make Invoice
When you make an invoice, the system applies the margin rate on the item price on selection of the specific item.

<img alt="Disable" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-invoice.png">

For more details about adding margins [Click Here](/docs/user/manual/en/selling/articles/adding-margin.html)

#### 4. Related Topics
1. [Promotional Scheme](/docs/user/manual/en/accounts/promotional-scheme)
1. [Tax Rule](/docs/user/manual/en/accounts/tax-rule)
1. [Supplier](/docs/user/manual/en/buying/supplier)
1. [Item](/docs/user/manual/en/stock/item)