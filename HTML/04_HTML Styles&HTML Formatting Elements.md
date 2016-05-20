#HTML Styles&HTML Formatting Elements
##The HTML Style Attribute
Setting the style of an HTML element, can be done with the **style attribute**.

The HTML style attribute has the following **syntax**:

	style="property:value;"
	
The ***property*** is a CSS property. The ***value*** is a CSS value.

	<!DOCTYPE html>
	<html>
	<body>
	
	<h2 style="color:red;">I am red</h2>
	<h2 style="color:blue;">I am blue</h2>
	
	</body>
	</html>
	
##HTML Background Color
The background-color property defines the background color for an HTML element:

This example sets the background for a page to lightgrey:

	<body style="background-color:lightgrey;">
	
	<h1>This is a heading</h1>
	<p>This is a paragraph.</p>
	
	</body>
	
##HTML Text Color
The **color** property defines the text color for an HTML element:

	<h1 style="color:blue;">This is a heading</h1>
	<p style="color:red;">This is a paragraph.</p>

##HTML Fonts

The font-family property defines the font to be used for an HTML element:

	<h1 style="font-family:verdana;">This is a heading</h1>
	<p style="font-family:courier;">This is a paragraph.</p>
	
	
##HTML Text Size
The **font-size** property defines the text size for an HTML element:

	<h1 style="font-size:300%;">This is a heading</h1>
	<p style="font-size:160%;">This is a paragraph.</p>
	
##HTML Text Alignment
The text-align property defines the horizontal text alignment for an HTML element:

	<h1 style="text-align:center;">Centered Heading</h1>
	<p>This is a paragraph.</p>

##HTML Formatting Elements
In the previous chapter, you learned about HTML <b>styling</b>, using the HTML <b>style attribute</b>.

HTML also defines special <b>elements</b> for defining text with a special <b>meaning</b>.

HTML uses elements like \<b> and \<i> for formatting output, like <b>bold</b> or <i>italic</i> text.

Formatting elements were designed to display special <b>types of text</b>:

* Bold text
* Important text
* Italic text
* Emphasized text
* Marked text
* Small text
* Deleted text
* Inserted text
* Subscripts
* Superscripts

<hr>
##HTML Bold and Strong Formatting

The HTML \<b> element defines bold text, without any extra importance.

	<p>This text is normal.</p>
	
	<p><b>This text is bold</b>.</p>

The HTML \<strong> element defines strong text, with added semantic "strong" importance.

	<p>This text is normal.</p>
	
	<p><strong>This text is strong</strong>.</p>
	
##HTML <i>Italic</i> and <em>Emphasized</em> Formatting

The HTML \<i> element defines italic text, without any extra importance.

	<p>This text is normal.</p>
	
	<p><i>This text is italic</i>.</p>
	
The HTML \<em> element defines emphasized text, with added semantic importance.

	<p>This text is normal.</p>
	
	<p><em>This text is emphasized</em>.</p>
	
	
##HTML <small>Small</small> Formatting

The HTML \<small> element defines small text:

	<h2>HTML <small>Small</small> Formatting</h2>
	
##HTML <mark>Marked</mark> Formatting
The HTML \<mark> element defines marked or highlighted text:

	<h2>HTML <mark>Marked</mark> Formatting</h2>
	
##HTML <del>Deleted</del> Formatting

The HTML \<del> element defines deleted (removed) text.

	<p>My favorite color is <del>blue</del> red.</p>
	
##HTML <ins>Inserted</ins> Formatting

The HTML \<ins> element defines inserted (added) text.

	<p>My favorite <ins>color</ins> is red.</p>
	
##HTML <sub>Subscript</sub> Formatting

The HTML \<sub> element defines subscripted text.

	<p>This is <sub>subscripted</sub> text.</p>
	
##HTML <sup>Superscript</sup> Formatting

The HTML \<sup> element defines superscripted text.

	<p>This is <sup>superscripted</sup> text.</p>
	
	