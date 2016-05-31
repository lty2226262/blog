#HTML Tables
##Defining HTML Tables
	<table style="width:100%">
	  <tr>
	    <td>Jill</td>
	    <td>Smith</td> 
	    <td>50</td>
	  </tr>
	  <tr>
	    <td>Eve</td>
	    <td>Jackson</td> 
	    <td>94</td>
	  </tr>
	</table>


	
Example explained:

Tables are defined with the \<table> tag.

Tables are divided into table rows with the \<tr> tag.

Table rows are divided into table data with the \<td> tag.

A table row can also be divided into table headings with the \<th> tag.

###Note
Table data \<td> are the data containers of the table.
They can contain all sorts of HTML elements like text, images, lists, other tables, etc.

##An HTML Table with a Border Attribute
If you do not specify a border for the table, it will be displayed without borders.

A border can be added using the border attribute:

	<table border="1" style="width:100%">
	  <tr>
	    <td>Jill</td>
	    <td>Smith</td> 
	    <td>50</td>
	  </tr>
	  <tr>
	    <td>Eve</td>
	    <td>Jackson</td> 
	    <td>94</td>
	  </tr>
	</table>

###Note	
The border attribute is on its way out of the HTML standard! It is better to use CSS.

To add borders, use the CSS border property:

	table, th, td {
	    border: 1px solid black;
	}

Remember to define borders for both the table and the table cells.

##An HTML Table with Collapsed Borders
If you want the borders to collapse into one border, add CSS border-collapse:

	table, th, td {
	    border: 1px solid black;
	    border-collapse: collapse;
	}

##An HTML Table with Cell Padding
Cell padding specifies the space between the cell content and its borders.

If you do not specify a padding, the table cells will be displayed without padding.

To set the padding, use the CSS padding property:

	table, th, td {
	    border: 1px solid black;
	    border-collapse: collapse;
	}
	th, td {
	    padding: 15px;
	}

##HTML Table Headings
Table headings are defined with the \<th> tag.

By default, all major browsers display table headings as bold and centered:

	<table style="width:100%">
	  <tr>
	    <th>Firstname</th>
	    <th>Lastname</th> 
	    <th>Points</th>
	  </tr>
	  <tr>
	    <td>Eve</td>
	    <td>Jackson</td> 
	    <td>94</td>
	  </tr>
	</table>

To left-align the table headings, use the CSS text-align property:


	th {
	    text-align: left;
	}

##An HTML Table with Border Spacing
Border spacing specifies the space between the cells.

To set the border spacing for a table, use the CSS border-spacing property:

	table {
	    border-spacing: 5px;
	}

###Note	
If the table has collapsed borders, border-spacing has no effect.
##Table Cells that Span Many Columns
To make a cell span more than one column, use the colspan attribute:

	<table style="width:100%">
	  <tr>
	    <th>Name</th>
	    <th colspan="2">Telephone</th>
	  </tr>
	  <tr>
	    <td>Bill Gates</td>
	    <td>555 77 854</td>
	    <td>555 77 855</td>
	  </tr>
	</table>

##Table Cells that Span Many Rows
To make a cell span more than one row, use the rowspan attribute:

	<table style="width:100%">
	  <tr>
	    <th>Name:</th>
	    <td>Bill Gates</td>
	  </tr>
	  <tr>
	    <th rowspan="2">Telephone:</th>
	    <td>555 77 854</td>
	  </tr>
	  <tr>
	    <td>555 77 855</td>
	  </tr>
	</table>

##An HTML Table With a Caption
To add a caption to a table, use the \<caption> tag:

	<table style="width:100%">
	  <caption>Monthly savings</caption>
	  <tr>
	    <th>Month</th>
	    <th>Savings</th>
	  </tr>
	  <tr>
	    <td>January</td>
	    <td>$100</td>
	  </tr>
	  <tr>
	    <td>February</td>
	    <td>$50</td>
	  </tr>
	</table>

###Note	
The \<caption> tag must be inserted immediately after the \<table> tag.
##A Special Style for One Table
To define a special style for a special table, add an id attribute to the table:


	<table id="t01">
	  <tr>
	    <th>Firstname</th>
	    <th>Lastname</th> 
	    <th>Points</th>
	  </tr>
	  <tr>
	    <td>Eve</td>
	    <td>Jackson</td> 
	    <td>94</td>
	  </tr>
	</table>
Now you can define a special style for this table:
	
	table#t01 {
	    width: 100%; 
	    background-color: #f1f1c1;
	}

And add more styles:

	table#t01 tr:nth-child(even) {
	    background-color: #eee;
	}
	table#t01 tr:nth-child(odd) {
	    background-color: #fff;
	}
	table#t01 th {
	    color: white;
	    background-color: black;
	}

