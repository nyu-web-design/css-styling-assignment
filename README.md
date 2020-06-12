# A Stylish Web Site About Me

Welcome! In this assignment, you will add CSS styles to your existing web site about you.

The updated HTML and CSS files must be published to the web by uploading them to your web root directory on the web server.

The new CSS file must be named `main.css` reside in a sub-directory named `css` and be linked from all pages of your site.

### Copy HTML

Before starting, copy the HTML code from your existing pages into the blank HTML documents in this new code repository.

- `index.html`
- `about_me.html`
- `more_about_me.html`

## Requirements

Some rules about styles for specific pages follow.

On top of these requirements, you are welcome to add any additional styles you believe will make this page compelling and visually stimulating to someone finding it on the web.

### All Pages

In this stylesheet, you must include some general styles that apply to all pages:

- **font family and font size** setting for all **paragraphs** that differ from the browser's defaults
- **font family and font size** setting for all all **h1**, **h2**, and **h3** elements that differ from the browser's defaults
- consistent **styles for all links** (`<a>` elements). At a minimum, the following link states must have at least different **background colors** or **text colors**: `link`, `visited`, `hover`, and `active`.

### About Me & More About Me Pages

The following styles must be applied to only the `<section>` elements in the files named `about_me.html` and `more_about_me.html`:

- apply a **padding** on all sides of all `<section>` elements in these pages to push the contents within them away from their edge.
- apply a **bottom margin** to all **section** elements in these pages to separate them from the other content below them.
- apply a **border** of your choosing around all **section** elements in these pages.

### About Me Page

The following specific styles will be applied to content only in the `about_me.html` document:

- in the HTML, give a **unique identifier** to each section element. Use the following identifiers: `my_background` for the section about your background, `my_interests` for the section about your interests.
- apply a **background image** OR **background color** to each of these two sections.
- apply a style that applies only to those **h2** elements that are nested within a **section** element on this page.

## Submit your work

In order to submit this assignment, you must publish it to the web and upload the code to GitHub.

### Upload the web page to a web server

Upload all files you have created to a web server. Your instructor will have given you instructions for how to do this.

Take note of the web address (URL) of your web page - this is the address that can be plugged into the address bar of any web browser for the web browser to load and display your web page.

### Add your web page's URL to the settings.json file

Make sure your name, NYU Net ID, and the exact URL of your web site's home page are placed into the `settings.json` file in the appropriate places. Make sure the URL works when plugged into a web browser beforehand.

### Submit your work on GitHub

You are now ready to submit this assignment. You can do so directly from Visual Studio Code with the following steps, in the indicated order:

1. Switch to the Source Control view in Visual Studio Code - this view will show you a list of the files you have modified.
1. In the "`Message`" text field towards the top-left, enter a unique message to yourself about what you have changed and, while still with the text field selected, type `Command`-`Enter` on Mac OS X, or `Control`-`Enter` on Windows, to "commit" the changes you've made with this custom message. If you forget to hit `Command`-`Enter` after typing the message, you can instead click the "`...`" button above the message field and click the "`Commit all`" option in the menu that appears.
1. Now, click the "`...`" button above the message field and click the "`Push`" option in the menu that appears - this will upload your changes to your personal code repository on GitHub.

You have now submitted your completed assignment. Your changes are now posted to GitHub.com, where the instructor and graders can access it. Your `settings.json` file has information about who you are and where we can view your page on the web.

You can verify all this yourself manually by visiting your repository on GitHub.com and making sure the code displayed there is what you submitted.
