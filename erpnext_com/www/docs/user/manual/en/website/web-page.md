<!-- add-breadcrumbs -->
# Web Page

Static Content like your Home Page, About Us, Contact Us, Terms pages can be
created using the Web Page.

To create a new Web Page, go to:

> Website > Web Page > New

![New Web Page](/docs/assets/img/website/new-web-page.png)
*New Web Page*

#### Title

The first thing to set is the title of your page. The title has the maximum
weight for search engines so choose a title that reflects the keywords that you
are targeting for your audience. The route will be auto-generated from the title
but you can change it.

#### Content

You can write your content in Rich Text, Markdown or HTML. If you want to make
simple content pages, Rich Text and Markdown are great options.

> Learn markdown in a few minutes at [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).

#### Images

For Rich Text Content, you can directly embed images using the editor.
For Markdown and HTML, you must attach the images to the document first.
Now get the URL of your image by right-clicking on your attachment and copying
the address.

![Image Link](/docs/assets/img/website/get-image-link.png)

Now, add them to your Markdown or HTML using the appropriate syntax.

```md
<!-- markdown -->
![Alt Text](/path/to/image-url.png)

<!-- html -->
<img src="/path/to/image-url.png" alt="Alt Text">
```

View your Web Page by clicking on **See on Website** in the sidebar.

![Web Page](/docs/assets/img/website/web-page.png)
*Web Page*

## Slideshow

You can also add a Slideshow to your Web Page. Refer how to create a Slideshow
at [Homepage Slideshow](/docs/user/manual/en/website/homepage#homepage-slideshow)

## Scheduled Publishing

You can schedule your Web Pages for publishing if you set Start Date and End
Date for your Web Page. They will be set as published inside the date ranges and
will be unpublished outside the range automatically.

Unpublished pages will throw an `Error 404` when they are visited.

## Javascript and CSS

You can add a JS script to your Web Page in the **Script** section. Make sure to
write your script inside the `frappe.ready` callback.

```js
frappe.ready(() => {
	// your script here
});
```

You can add CSS styling to your Web Page in the **Style** section. Inspect the
elements to see what classes are available for styling. If you are using HTML
Content, you can use your own classes and style them here.

## Sidebar

You can add a Website Sidebar with custom links on your Web Page. In the
**Sidebar and Comments** section enable **Show Sidebar**. Select an existing
Website Sidebar or create a new one.

![Web Page Sidebar](/docs/assets/img/website/web-page-sidebar.png)
*Web Page Sidebar*

Add links and their route in the Sidebar Items table.
![Website Sidebar](/docs/assets/img/website/new-website-sidebar.png)
*Website Sidebar*

![Web Page with Sidebar](/docs/assets/img/website/web-page-with-sidebar.png)
*Web Page with Sidebar*

## Comments

You can enable comments on your Web Page where people can leave a comment with
their Name and Email. Enable comments from the **Sidebar and Comments** section.

![Web Page Comments](/docs/assets/img/website/web-page-comments.gif)
*Web Page Comments*

## Header

You can add a custom HTML for the header section of the page. This will override
the title of the Web Page.

![Web Page Header](/docs/assets/img/website/web-page-header.png)
*Web Page Header*

![Web Page with Custom Header](/docs/assets/img/website/web-page-with-custom-header.png)
*Web Page with Custom Header*

## Breadcrumbs

You can add a list of breadcrumbs on your Web Page. These will be shown on top
before the header.

![Web Page Breadcrumbs](/docs/assets/img/website/web-page-breadcrumbs.png)
*Web Page Breadcrumbs*

![Web Page with Breadcrumbs](/docs/assets/img/website/web-page-with-breadcrumbs.png)
*Web Page with Breadcrumbs*

## Meta Tags

You can also add Meta Tags to your Web Page. You must add the property key and
its value in the Meta Tag Table and it will auto-generate HTML `meta` tags on
your Web Page.

![Web Page Meta Tags](/docs/assets/img/website/web-page-meta-tags.gif)
*Web Page Meta Tags*

{next}
