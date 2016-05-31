#[Compare two objects with .equals() and == operator](http://stackoverflow.com/questions/13387742/compare-two-objects-with-equals-and-operator)

`==` compares object references, it checks to see if the two operands point to the same object (not equivalent objects, the same object).

If you want to compare strings (to see if they contain the same characters), you need to compare the strings using `equals`.

In your case, if two instances of `MyClass` really are considered equal if the strings match, then:

	public boolean equals(Object object2) {
	    return object2 instanceof MyClass && a.equals(((MyClass)object2).a);
	}
	
...but usually if you are defining a class, there's more to equivalency than the equivalency of a single field (`a` in this case).

*from:[http://stackoverflow.com/questions/13387742/compare-two-objects-with-equals-and-operator](http://stackoverflow.com/questions/13387742/compare-two-objects-with-equals-and-operator)*

