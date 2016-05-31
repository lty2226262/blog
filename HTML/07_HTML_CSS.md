#HTML Styles - CSS
##Styling HTML with CSS

CSS stands for Cascading Style Sheets

Styling can be added to HTML elements in 3 ways:

* Inline - using a style attribute in HTML elements
* Internal - using a \<style> element in the HTML \<head> section
* External - using one or more external CSS files
The most common way to add styling, is to keep the styles in separate CSS files. But, in this tutorial, we use internal styling, because it is easier to demonstrate, and easier for you to try it yourself.

###Note	
You can learn much more about CSS in our CSS Tutorial.

##Inline Styling (Inline CSS)
Inline styling is used to apply a unique style to a single HTML element:

Inline styling uses the style attribute.

This example changes the text color of the \<h1> element to blue:


	<h1 style="color:blue;">This is a Blue Heading</h1>

##Internal Styling (Internal CSS)
Internal styling is used to define a style for one HTML page.

Internal styling is defined in the <head> section of an HTML page, within a \<style> element:

	<!DOCTYPE html>
	<html>
	<head>
	<style>
	body {background-color:lightgrey;}
	h1   {color:blue;}
	p    {color:green;}
	</style>
	</head>
	<body>

	<h1>This is a heading</h1>
	<p>This is a paragraph.</p>
	
	</body>
	</html>

##External Styling (External CSS)
An external style sheet is used to define the style for many pages.

With an external style sheet, you can change the look of an entire web site by changing one file!

To use an external style sheet, add a link to it in the \<head> section of the HTML page:

	<!DOCTYPE html>
	<html>
	<head>
	  <link rel="stylesheet" href="styles.css">
	</head>
	<body>
	
	<h1>This is a heading</h1>
	<p>This is a paragraph.</p>
	
	</body>
	</html>

An external style sheet can be written in any text editor. The file should not contain any html tags. The style sheet file must be saved with a .css extension.

Here is how the "styles.css" looks:

	body {
	    background-color: lightgrey;
	}
	
	h1 {
	    color: blue;
	}
	
	p {
	    color:green;
	}

##CSS Fonts
The CSS color property defines the text color to be used for the HTML element.

The CSS font-family property defines the font to be used for the HTML element.

The CSS font-size property defines the text size to be used for the HTML element.

	<!DOCTYPE html>
	<html>
	<head>
	<style>
	h1 {
	    color: blue;
	    font-family: verdana;
	    font-size: 300%;
	}
	p  {
	    color: red;
	    font-family: courier;
	    font-size: 160%;
	}
	</style>
	</head>
	<body>
	
	<h1>This is a heading</h1>
	<p>This is a paragraph.</p>
	
	</body>
	</html>

##The CSS Box Model
Every HTML element has a box around it, even if you cannot see it.

The CSS border property defines a visible border around an HTML element:

	p {
	    border: 1px solid black;
	}

The CSS padding property defines a padding (space) inside the border:

	p {
	    border: 1px solid black;
	    padding: 10px;
	}

##The CSS margin property defines a margin (space) outside the border:


	p {
	    border: 1px solid black;
	    padding: 10px;
	    margin: 30px;
	}
 
###Note	
The CSS examples above use px to define sizes in pixels.

##The id Attribute
All the examples above use CSS to style HTML elements in a general way.

To define a special style for one special element, first add an id attribute to the element:

	<p id="p01">I am different</p>
then define a style for the element with the specific id:

	#p01 {
	    color: blue;
	}
 
##The class Attribute
To define a style for a special type (class) of elements, add a class attribute to the element:

	<p class="error">I am different</p>
Now you can define a different style for elements with the specific class:


	p.error {
	    color: red;
	}
 
###Note	
Use id to address a single element. Use class to address groups of elements.