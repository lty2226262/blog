#HTML Images

##HTML Images Syntax
In HTML, images are defined with the <img> tag.

The <img> tag is empty, it contains attributes only, and does not have a closing tag.

The src attribute specifies the URL (web address) of the image:

	<img src="url" alt="some_text">
	
##The alt Attribute
The alt attribute specifies an alternate text for an image, if the image cannot be displayed.

The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).

If a browser cannot find an image, it will display the alt text:

	<img src="wrongname.gif" alt="HTML5 Icon" style="width:128px;height:128px;">
	
The alt attribute is required. A web page will not validate correctly without it.

##HTML Screen Readers
A screen reader is a software program that can read what is displayed on a screen.

Screen readers are useful to people who are blind, visually impaired, or learning disabled.

###Note	
Screen readers can read the alt attribute.
##Image Size - Width and Height
You can use the <b>style</b> attribute to specify the width and height of an image.

The values are specified in pixels (use px after the value):

	<img src="html5.gif" alt="HTML5 Icon" style="width:128px;height:128px;">
	
Alternatively, you can use width and height attributes. Here, the values are specified in pixels by default:

 
	<img src="html5.gif" alt="HTML5 Icon" width="128" height="128">
 
##Width and Height or Style?
Both the width, height, and style attributes are valid in the latest HTML5 standard.

We suggest you use the style attribute. It prevents styles sheets from changing the original size of images:

	<!DOCTYPE html>
	<html>
	<head>
	<style>
	img { 
	    width:100%; 
	}
	</style>
	</head>
	<body>
	
	<img src="html5.gif" alt="HTML5 Icon" style="width:128px;height:128px;">
	<img src="html5.gif" alt="HTML5 Icon" width="128" height="128">
	
	</body>
	</html>
 
##Images in Another Folder
If not specified, the browser expects to find the image in the same folder as the web page.

However, it is common to store images in a sub-folder. You must then include the folder name in the src attribute:

	<img src="/images/html5.gif" alt="HTML5 Icon" style="width:128px;height:128px;">

##Images on Another Server
Some web sites store their images on image servers.

Actually, you can access images from any web address in the world:

	<img src="http://www.w3schools.com/images/w3schools_green.jpg" alt="W3Schools.com">

##Animated Images
The GIF standard allows animated images:

	<img src="programming.gif" alt="Computer Man" style="width:48px;height:48px;">

Note that the syntax of inserting animated images is no different from non-animated images.

##Using an Image as a Link
 To use an image as a link, simply nest the \<img> tag inside the \<a> tag:

	<a href="default.asp">
	  <img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;border:0;">
	</a>

###Note	
Add "border:0;" to prevent IE9 (and earlier) from displaying a border around the image.
##Image Floating
Use the CSS float property to let the image float.

The image can float to the right or to the left of a text:

	<p>
	<img src="smiley.gif" alt="Smiley face" style="float:right;width:42px;height:42px;">
	The image will float to the right of the text.
	</p>
	
	<p>
	<img src="smiley.gif" alt="Smiley face" style="float:left;width:42px;height:42px;">
	The image will float to the left of the text.
	</p>

##Image Maps
Use the \<map> tag to define an image-map. An image-map is an image with clickable areas.

The name attribute of the \<map> tag is associated with the \<img>'s usemap attribute and creates a relationship between the image and the map.

The \<map> tag contains a number of \<area> tags, that defines the clickable areas in the image-map:

	<img src="planets.gif" alt="Planets" usemap="#planetmap" style="width:145px;height:126px;">
	
	<map name="planetmap">
	  <area shape="rect" coords="0,0,82,126" alt="Sun" href="sun.htm">
	  <area shape="circle" coords="90,58,3" alt="Mercury" href="mercur.htm">
	  <area shape="circle" coords="124,58,8" alt="Venus" href="venus.htm">
	</map>
