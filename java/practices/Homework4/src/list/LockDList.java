/* LockDList.java */

package list;

public class LockDList extends DList{
	
	protected DListNode newNode(Object item, DListNode prev, DListNode next) {
   		return new LockDListNode(item, prev, next);
  	}

	public void lockNode(DListNode node){
		LockDListNode temp = (LockDListNode)node;
		temp.isLock = true;
	}

	public void remove(DListNode node) {
    // Your solution here.
    	LockDListNode temp = (LockDListNode)node;
    	if (node != null && temp.isLock == false){
      		node.prev.next = node.next;
      		node.next.prev = node.prev;
      		size--;
    	}
  	}

  	public LockDListNode front() {
    // Your solution here.
    	if(size < 1) return null;
    	else return (LockDListNode)head.next; 
  	}

  	public LockDListNode back() {
    // Your solution here.
    	if(size < 1) return null;
    	else return (LockDListNode)head.prev;
  	}

  	public LockDListNode next(DListNode node) {
    // Your solution here.
    	if (node == null || node.next == head) return null;
    	else return (LockDListNode)node.next;
  	}

  	public LockDListNode prev(DListNode node) {
    // Your solution here.
    	if (node == null || node.prev == head) return null;
    	else return (LockDListNode)node.prev;
  	}

}