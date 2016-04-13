/* LockDListNode.java */

package list;

public class LockDListNode extends DListNode {
	boolean isLock;
	
	LockDListNode(Object i, DListNode p, DListNode n){
		super(i,p,n);
		isLock = false;
	}

}