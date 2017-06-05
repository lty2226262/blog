# What are Jupyter notebooks?

The notebook is a web application that allows you to combine explanatory text, math equations, code, and visualizations all in one easily sharable document.

# Installing Jupyter Notebook

		conda install jupyter notebook

# Run server
		
		jupyter notebook

By default, the notebook server runs at http://localhost:8888

## Shutting down Jupyter

You can shutdown individual notebooks by marking the checkbox next to the notebook on the server home and clicking "Shutdown."

You can shutdown the entire server by pressing control + C twice in the terminal. Again, this will immediately shutdown all the running notebooks, so make sure your work is saved!

# Notebook interface

You’ll see a little box outlined in green. This is called a cell. Cells are where you write and run your code. You can also change it to render Markdown, a popular formatting syntax for writing web content. I'll cover Markdown in more detail later. In the toolbar, click “Code” to change it to Markdown and back. The little play button runs the cell, and the up and down arrows move cells up and down.

## Command palette

The little keyboard is the command palette. This will bring up a panel with a search bar where you can search for various commands. This is really helpful for speeding up your workflow as you don't need to search around in the menus with your mouse. 

# Code cells

## Run the cell

Shift + Enter

## Run a cell without changing the selected cell

Ctrl + Enter

## assigning a value to a variable

		mindset = 'growth'

## execute a code cell

		mindset[:4]

then output
	
		'grow'

## Code completion

		press 'Tab'

## Tooltips

		press "shift+tab"
# Markdown cells

we could using Latex symbols in Jupyter notebook. To start math mode, wrap the LaTeX in dollar signs \$y = mx + b\$ for inline math. For a math block, use double dollar signs,

		$$
		y = \frac{a}{b+c}
		$$

# Keyborad shortcuts

**h** - help menu
**a** - create a cell above
**b** - create a cell below
**y** - change from a markdown to a code cell
**m** - change from a code cell to a markdown
**d,d** - delete cells(type twice)
**s** - save the notebook
**Shift + Command + P** - command palette


