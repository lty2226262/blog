/* DList.java */

package pj1;

public class DList{
	DListNode head;
	int length;

	public DList(){
		this.head = new DListNode(0,(short)0,(short)0,(short)0,head,head);
		this.length = 0;
		this.head.next = this.head;
		this.head.prev = this.head;
	}

	public void InsertFront(DListNode toInsert){
		toInsert.next = head.next;
		toInsert.prev = head;
		head.next.prev = toInsert;
		head.next = toInsert;
		length++;
	}

	public void InsertTail(DListNode toInsert){
		toInsert.next = head;
		toInsert.prev = head.prev;
		head.prev.next = toInsert;
		head.prev = toInsert;
		length++;
	}

}