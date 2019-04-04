# Coupon Code

Everyone loves discount ! so do the coupons offering such discounts. To encourage customers to buy from the e-commerce website, 
coupon code feature is exciting.

Coupon Code Feature can be enabled from Shopping Cart Settings

`Explore > Settings > Shopping Cart Settings`

<img class="screenshot" alt="Shopping Cart Settings to enable Coupon Code" src="{{docs_base_url}}/assets/img/articles/CCShoppingCartSettings.png">



## Coupon Code Doctype

Coupon Code is basically exposing [Pricing Rule](https://erpnext.com/docs/user/videos/learn/pricing-rule.html) feature on shopping cart through application of the coupon.
So while creating Coupon Code it is necessary to link it to relvant [pricing rule](https://erpnext.com/docs/user/videos/learn/pricing-rule.html).

<img class="screenshot" alt="Coupon Code Doctype" src="{{docs_base_url}}/assets/img/articles/CouponCodeDoctype.png">

#### Field Information 
1. Coupon Code - this is unique code which can be used on the shopping cart page before placing the order.
2. Valid From - To - validity of the coupon
3. Maximum Use - Cap to limit the usage of the coupon code
4. Used - for each Sales Order submitted with coupon code , the used count increments by 1.
5. Coupon Code Description - can be used while creating Email Template to inform potential customers about the coupon code and scheme
information
6. Coupon Type - Promotional , Gift Card  to categories for analysis
7. Price List - Price List for which Coupon will be applicable
8. Pricing Rule - To which the coupon code is linked

In Pricing Rule it is important to have "Coupon Code Based" checked true as shown below
<img class="screenshot" alt="Pricing Rule Coupon Code Based" src="{{docs_base_url}}/assets/img/articles/PriceRuleCC.png">

### Coupon Code Can be applied two ways
1) Through URL , coupon code will be automatically fetched and filled in the Apply Coupon Code textbox , for ease of user to apply.

	http://xyz.erpnext.com/products/golden-ring?cc=SAVE5

2) Explicitly applying the code , by filling the code and clicking on Apply Coupon Code button as shown below in shopping cart page
<img class="screenshot" alt="Shopping Cart Apply CouponCode" src="{{docs_base_url}}/assets/img/articles/ShoppinCartApplyCouponCode.png">

Price will get updated on successful application of the coupon code.


