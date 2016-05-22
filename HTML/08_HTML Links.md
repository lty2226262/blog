#HTML Links
##HTML Links - Syntax
In HTML, links are defined with the \<a> tag:

	<a href="url">link text</a>
============== 
	
	<a href="http://www.w3schools.com/html/">Visit our HTML tutorial</a>
 
The href attribute specifies the destination address (http://www.w3schools.com/html/)

The link text is the visible part (Visit our HTML tutorial).

Clicking on the link text, will send you to the specified address.

###Note	
The link text does not have to be text. It can be an HTML image or any other HTML element.
###Note	
Without a trailing slash on subfolder addresses, you might generate two requests to the server. Many servers will automatically add a trailing slash to the address, and then create a new request.
##Local Links
The example above used an absolute URL (A full web address).

A local link (link to the same web site) is specified with a relative URL (without http://www....).


	<a href="html_images.asp">HTML Images</a>

##HTML Links - Colors
When you move the mouse over a link, two things will normally happen:

* The mouse arrow will turn into a little hand
* The color of the link element will change

By default, a link will appear like this (in all browsers):

* An unvisited link is underlined and blue
* A visited link is underlined and purple
* An active link is underlined and red

You can change the default colors, by using styles:

	<style>
	a:link    {color:green; background-color:transparent; text-decoration:none}
	a:visited {color:pink; background-color:transparent; text-decoration:none}
	a:hover   {color:red; background-color:transparent; text-decoration:underline}
	a:active  {color:yellow; background-color:transparent; text-decoration:underline}
	</style>

##HTML Links - The target Attribute
The target attribute specifies where to open the linked document.

This example will open the linked document in a new browser window or in a new tab:

	<a href="http://www.w3schools.com/" target="_blank">Visit W3Schools!</a>

<table> 
  <tbody><tr>
    <th style="width:20%">Target Value</th>
    <th>Description</th>
  </tr>  
  <tr>
    <td>_blank</td>
    <td>Opens the linked document in a new window or tab</td>
  </tr>
  <tr>
    <td>_self</td>
    <td>Opens the linked document in the same frame as it was clicked (this is default)</td>
  </tr>
	<tr>
    <td>_parent</td>
    <td>Opens the linked document in the parent frame</td>
  </tr>
	<tr>
    <td>_top</td>
    <td>Opens the linked document in the full body of the window</td>
  </tr>
  <tr>
    <td><i>framename</i></td>
    <td>Opens the linked document in a named frame</td>
  </tr>
  </tbody></table>
If your webpage is locked in a frame, you can use target="_top" to break out of the frame:

	<a href="http://www.w3schools.com/html/" target="_top">HTML5 tutorial!</a>

##HTML Links - Image as Link
It is common to use images as links:

	<a href="default.asp">
	  <img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;border:0">
	</a>

###Note	
border:0 is added to prevent IE9 (and earlier) from displaying a border around the image.
##HTML Links - Create a Bookmark
HTML bookmarks are used to allow readers to jump to specific parts of a Web page.

Bookmarks are practical if your website has long pages.

To make a bookmark, you must first create the bookmark, and then add a link to it.

When the link is clicked, the page will scroll to the location with the bookmark.

##Example
First, create a bookmark with the id attribute:

	<h2 id="tips">Useful Tips Section</h2>
Then, add a link to the bookmark ("Useful Tips Section"), from within the same page:

	<a href="#tips">Visit the Useful Tips Section</a>
Or, add a link to the bookmark ("Useful Tips Section"), from another page:

	<a href="html_tips.html#tips">Visit the Useful Tips Section</a>
