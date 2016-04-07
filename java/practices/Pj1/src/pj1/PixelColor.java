/* PixelColor.java */

package pj1;

public class PixelColor{
	short red;
	short green;
	short blue;

	public PixelColor(){
		red = 0;
		green = 0;
		blue = 0;
	}

	public PixelColor(PixelColor a){
		red = a.getRed();
		green = a.getGreen();
		blue = a.getBlue();
	}

	public PixelColor(short r,short g,short b){
		red = r;
		green = g;
		blue = b;
	}

	public boolean equals(PixelColor a){
		return ((this.red == a.red) && (this.green == a.green) && (this.blue == a.blue)); 
	}

	public short getRed(){
		return red;
	}

	public short getGreen(){
		return green;
	}

	public short getBlue(){
		return blue;
	}
}