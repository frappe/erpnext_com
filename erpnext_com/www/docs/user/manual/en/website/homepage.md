<!-- add-breadcrumbs -->
# Homepage

ERPNext's Website Module generates a default landing page for your website. You
can customize it in Homepage.

> Go to Website > Portal > Homepage

![Homepage](/docs/assets/img/website/homepage.png)
*Homepage*

After you set your Tag Line, Description and Hero Image you'll have a decent
looking front page. You can also change the URL for the Explore button.

![Website Homepage](/docs/assets/img/website/website-homepage.png)
*Website Homepage*

> Make sure your default homepage is set as **home** in Website Settings for
> this to work.

## Homepage Slideshow

There are three types of Hero Section you can configure on the Homepage. The
first one (Default) is the one you have already seen above.

The second type is Slideshow. Set the **Hero Section Based On** to **Slideshow**.

![Homepage Slideshow Setting](/docs/assets/img/website/homepage-slideshow-setting.png)
*Homepage Slideshow Setting*

Now, select an existing Slideshow or create a new one.

![Website Slideshow](/docs/assets/img/website/website-slideshow.png)
*Website Slideshow*

> For best results, make sure all of your slideshow images have same height and
> their width is greater than the height.

![Website Homepage with Slideshow](/docs/assets/img/website/website-homepage-slideshow.gif)

## Custom Hero Section

The third type of Hero Section allows you to write your own HTML.

Set **Hero Section Based On** to **Hero Section**.

Now create a new Hero Section. Set **Section Based On** as **Custom HTML**.
Write your custom HTML in the Section HTML field.

![New Hero Section](/docs/assets/img/website/hero-custom.png)
*New Hero Section*

> You can write any valid [Bootstrap
> 4](https://getbootstrap.com/docs/4.3/getting-started/introduction/) markup
> here.

![Homepage Settings](/docs/assets/img/website/homepage-hero-custom.png)
*Homepage Settings*

![Homepage Hero Custom](/docs/assets/img/website/website-homepage-custom.png)
*Homepage Hero Custom*

## Featured Products

You can also show featured products on your Homepage by adding them to the
Products Table.

![Homepage Products Table](/docs/assets/img/website/homepage-featured-products.png)
*Homepage Products Table*


![Featured Products on Homepage](/docs/assets/img/website/website-featured-products.png)
*Featured Products on Homepage*

## Homepage Section

You can add custom sections on your Homepage by creating new Homepage Sections.

> Go to Website > Portal > Homepage Section

A homepage section can consist of cards or Custom HTML. Set **Section Based On**
to **Cards**.

![New Homepage Section](/docs/assets/img/website/new-homepage-section.png)
*New Homepage Section*

Add details for each card like Title, Subtitle, Image, Content and Route.

![Homepage Section](/docs/assets/img/website/homepage-section.png)
*Homepage Section*

You can also control the order in which these sections appear by setting the
**Section Order**. 0 will be shown first, followed by 1, and so on.

> To add Sections with Custom HTML refer [Custom Hero Section](#custom-hero-section).

## Custom Homepage

ERPNext allows you to have a completely different homepage if you dont want to
use the default one described above.

To setup a custom homepage:

1. Create a [Web Page](/docs/user/manual/en/website/web-page)
1. Go to Website > Setup > Website Settings
1. Set Home Page as the `route` of your Web Page.
   ![](/docs/assets/img/website/custom-homepage.png)

{next}