#HTML Basic Examples
##HTML Documents
All HTML documents must start with a type declaration: <!DOCTYPE html>.

The HTML document itself begins with \<html> and ends with \</html>.

The visible part of the HTML document is between \<body> and \</body>.

	<!DOCTYPE html>
	<html>
	<body>
	
	<h1>My First Heading</h1>
	
	<p>My first paragraph.</p>
	
	</body>
	</html>

##HTML Headings

HTML headings are defined with the \<h1> to \<h6> tags:
	
	<h1>This is a heading</h1>
	<h2>This is a heading</h2>
	<h3>This is a heading</h3>
	
##HTML Paragraphs

HTML paragraphs are defined with the \<p> tag:

	<p>This is a paragraph.</p>
	<p>This is another paragraph.</p>	
	
##HTML Links

HTML links are defined with the \<a> tag:

	<a href="http://www.w3schools.com">This is a link</a>
	
The link's destination is specified in the href attribute. 

Attributes are used to provide additional information about HTML elements.

##HTML Images

HTML images are defined with the \<img> tag.

The source file (src), alternative text (alt), and size (width and height) are provided as attributes:

	<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
	
