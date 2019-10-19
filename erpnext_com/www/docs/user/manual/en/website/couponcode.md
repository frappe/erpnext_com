# Coupon Code

**Coupon Code allows a Customer to avail discount on shoppping cart products.**

Everyone loves discount! so do the coupons offering such discounts. To encourage customers to buy from the e-commerce website, 
coupon code feature is exciting.

There are resellers/other site which generates leads for your ERPNext e-commerce website products/items/services. 

When the potential customer comes from other sites OR promotional emails to your ERPNext website for purchase, you should have the ability
	
	a)to track from which affiliate /sales partner the lead is coming i.e. [referral code]
	(https://erpnext.com/docs/user/manual/en/selling/sales-partner)

	b) to give discount (based on Pricing Rule) on overall purchase i.e. Coupon code

## 1. Prerequisite

1) Coupon Code feature can be enabled from Shopping Cart Settings

> Home > Settings > Shopping Cart Settings

<img class="screenshot" alt="Shopping Cart Settings to enable Coupon Code" src="{{docs_base_url}}/assets/img/selling/CCShoppingCartSettings.png">

2) It is advised you create Pricing Rule having **Coupon Code Based** flag enabled.

## 2. How to create Coupon Code

To access Coupon Code, go to :

> Home > Accounts > Coupon Code

1. Go to Coupon Code, click on New.
2. Create **Coupon Name**, e.g. "SAVE 20"
3. **Coupon Type**, select from Promotional or Gift Card.
   	
	Promotional, is to promote a generic scheme. 
   	
	Giftcard, is to randomly generate coupon code and to distribute to specific customer/user.
   
4. **Coupon Code** is unique readonly code in all capital letters , which gets generated based on Coupon Type & Coupon Name.
	
	For Coupon Type,
	
	a) *Promotional* , it removes all spaces and takes upto the first 8 characters. e.g. SAVE20
	
	b) *GiftCard* ,it generates random code of 11 digits. e.g. AP48K7CT9LP

    It can be used on the shopping cart page before placing the order to avail discount. 
  
4. Select [Pricing Rule](https://erpnext.com/docs/user/videos/learn/pricing-rule.html)  having **coupon code based** flag enabled. 

5. Click  on Save 

	<img class="screenshot" alt="Coupon Code Doctype" src="{{docs_base_url}}/assets/img/selling/CouponCodeDoctype.png">

## 3. Features

#### 3.1 Validity and Usage

1. **Valid From - To** - validity of the coupon
2. **Maximum Use** - Cap to limit the usage of the coupon code
3. **Used** - for each Sales Order submitted with coupon code , the used count increments by 1.
4. **Coupon Code Description** - can be used while creating Email Template to inform potential customers about the coupon code and scheme information

	<img class="screenshot" alt="Pricing Rule Coupon Code Based" src="{{docs_base_url}}/assets/img/selling/PriceRuleCC.png">



#### 3.2 Coupon Code can be applied in two ways

1. Through URL , coupon code will be automatically fetched from the URL parameter ("cc") and filled in the Apply Coupon Code textbox , for ease of user to apply.

	http://xyz.erpnext.com/products/golden-ring?cc=SAVE5

2. Explicitly applying the code , by filling the code and clicking on "Apply Coupon Code" button as shown below in shopping cart page

	<img class="screenshot" alt="Shopping Cart Apply CouponCode" src="{{docs_base_url}}/assets/img/selling/ShoppinCartApplyCouponCode.png">

Price will get updated on successful application of the coupon code.


### 4. Related Topics

1. [Shopping Cart](https://erpnext.com/docs/user/manual/en/website/shopping-cart)
2. [Pricing Rule](https://erpnext.com/docs/user/videos/learn/pricing-rule.html)
