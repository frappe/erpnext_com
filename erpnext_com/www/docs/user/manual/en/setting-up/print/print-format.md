<!-- add-breadcrumbs -->
# Print Format

**The Print Format helps you quickly make a simple customized Print Format by dragging and dropping data fields and adding custom text or HTML.**

You can create a new Print Format either by going to:

> Home > Settings > Printing > Print Format

## 1. How to create a new Print Format
### 1.1 Via the menu
1. Click on New.
1. Enter a name and select a DocType for which the print format is for.
1. Select a module for which it should apply.

  ![Print Format menu](/docs/assets/img/setup/print/print-format-menu.png)

Under Style Settings, there are options to change the styling options.

To style the Print Format using custom Jinja/JS, click on Custom Format. If you select this option, there'll be a checkbox for raw printing. To know more about raw printing, [click here](/docs/user/manual/en/setting-up/print/raw-printing).

If developer mode is enabled, you can select Standard as yes to contribute a print format as a standard (preset) print format in the system.

### 1.2 Via a document
1. Open the document for which you want to make a Print Format. Click the Printer icon, or go to Menu > Print and click on the Customize... button. Note: You must have System Manager permission to do this.

  <img class="screenshot" alt="Send Email" src="{{docs_base_url}}/assets/img/setup/print/print-format-builder-1.gif">

1. To add a field, just drag it from the left sidebar and add it in your layout. You can edit the layouts in sections or individual fields by clicking on the settings <i class="octicon octicon-gear"></i> icon.

1. To remove a field, just drag it back into the fields sidebar.

1. Click on Save. 

You can add customized text, HTML in your print format, just drag and drop the **Custom HTML** field (in dark color) and add it to the place where you want to add the Custom HTML content.

Then click on **Edit HTML** to edit your content.

<div class="embed-container">
  <iframe src="https://www.youtube.com/embed/cKZHcx1znMc?start=82&rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
  </iframe>
</div>

### 2. Related Topics
1. [Print Style](/docs/user/manual/en/setting-up/print/print-style)
1. [Print Headings](/docs/user/manual/en/setting-up/print/print-headings)
1. [Letter Head](/docs/user/manual/en/setting-up/print/letter-head)
1. [Cheque Print Template](/docs/user/manual/en/setting-up/print/cheque-print-template)
