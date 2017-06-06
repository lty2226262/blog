#HTML Elements & HTML Attributes
##Empty HTML Elements
HTML elements with no content are called empty elements.

\<br> is an empty element without a closing tag (the \<br> tag defines a line break).

Empty elements can be "closed" in the opening tag like this: \<br />.

HTML5 does not require empty elements to be closed. But if you want stricter validation, or you need to make your document readable by XML parsers, you should close all HTML elements.

##HTML Attributes
* HTML elements can have **attributes**
* Attributes provide **additional information** about an element
* Attributes are always specified **in the start tag**
* Attributes come in name/value pairs like: **name="value"**

##The lang Attribute

The document language can be declared in the \<html> tag.

The language is declared in the lang attribute.

Declaring a language is important for accessibility applications (screen readers) and search engines:

	<!DOCTYPE html>
	<html lang="en-US">
	<body>
	
	<h1>My First Heading</h1>
	<p>My first paragraph.</p>
	
	</body>
	</html>
	
The first two letters specify the language (en). If there is a dialect, use two more letters (US).

##The title Attribute

HTML paragraphs are defined with the \<p> tag.

In this example, the \<p> element has a title attribute. The value of the attribute is "About W3Schools":

	<p title="About W3Schools">
	W3Schools is a web developer's site.
	It provides tutorials and references covering
	many aspects of web programming,
	including HTML, CSS, JavaScript, XML, SQL, PHP, ASP, etc.
	</p>
	
##The href Attribute

HTML links are defined with the \<a> tag. The link address is specified in the href attribute:

	<a href="http://www.w3schools.com">This is a link</a>
	
##Size Attributes

HTML images are defined with the \<img> tag.

The filename of the source (src), and the size of the image (width and height) are all provided as attributes:

	<img src="w3schools.jpg" width="104" height="142">
	
The image size is specified in pixels: width="104" means 104 screen pixels wide.

You will learn more about images and the <img> tag later in this tutorial.

##The alt Attribute

The **alt** attribute specifies an alternative text to be used, when an HTML element cannot be displayed.

The value of the attribute can be read by "screen readers". This way, someone "listening" to the webpage, i.e. a blind person, can "hear" the element.

	<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
	
##Single or Double Quotes?

Double style quotes are the most common in HTML, but single style can also be used.

In some situations, when the attribute value itself contains double quotes, it is necessary to use single quotes:

	<p title='John "ShotGun" Nelson'>
	
Or vice versa:

	<p title="John 'ShotGun' Nelson">