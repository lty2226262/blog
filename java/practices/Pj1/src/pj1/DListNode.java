/* DListNode.java */

package pj1;

public class DListNode{
	int numberOfPixel;
	PixelColor valueOfPixel;
	DListNode next;
	DListNode prev;

	public DListNode(){
		this.numberOfPixel = 0;
		this.valueOfPixel = new PixelColor();
		this.next = null;
		this.prev = null;
	}

	public DListNode(int num){
		this.numberOfPixel = num;
		this.valueOfPixel = new PixelColor();
		this.next = null;
		this.prev = null;
	}

	public DListNode(int num, short r, short g, short b){
		this.numberOfPixel = num;
		this.valueOfPixel = new PixelColor(r,g,b);
		this.next = null;
		this.prev = null;
	}

	public DListNode(int num, short r, short g, short b, DListNode next, DListNode prev){
		this.numberOfPixel = num;
		this.valueOfPixel = new PixelColor(r,g,b);
		this.next = next;
		this.prev = prev;
	}

	public DListNode(int num, PixelColor a, DListNode next, DListNode prev){
		this.numberOfPixel = num;
		this.valueOfPixel = new PixelColor(a);
		this.next = next;
		this.prev = prev;
	}

}