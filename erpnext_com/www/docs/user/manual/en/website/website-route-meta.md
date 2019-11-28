<!-- add-breadcrumbs -->
# Website Route Meta

**Arbitrary meta tags can be added in your web pages using Website Route Meta.**

To access Website Route Meta go to:

> Home > Website > Web Site > Website Route Meta

## 1. How to add meta tags to a web page

1. Click on New.
1. Enter the route. Make sure the route doesn't start with a slash (`/`). A Web
   Page for this route should exist.
1. Add key value pairs for each meta tag. For e.g., to add keywords to your web
   page, enter "keywords" as the Key and add comma separated keywords in the
   Value column.
1. Click on Save.

![New Website Route Meta](/docs/assets/img/website/new-website-route-meta.png)
*New Website Route Meta*

Now if you check the page source of your web page, the meta tags will look
something like this:

```html
<meta name="description" content="Now with an 8-core processor, the 15-inch MacBook Pro is the fastest Mac notebook ever.">
<meta name="keywords" content="apple, macbook, macbook pro, intel, 8 core, fastest">
```

> **Note:** Meta Tags are not only limited to Web Page, but they can be added to
> any route that has a website page in ERPNext.
>
> For e.g., You can add meta tags to your blog posts if you know the route which
> you can get from the Blog Post form.
