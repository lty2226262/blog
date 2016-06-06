/* HashTableChained.java */

package dict;

import list.DList;
import list.DListNode;

/**
 *  HashTableChained implements a Dictionary as a hash table with chaining.
 *  All objects used as keys must have a valid hashCode() method, which is
 *  used to determine which bucket of the hash table an entry is stored in.
 *  Each object's hashCode() is presumed to return an int between
 *  Integer.MIN_VALUE and Integer.MAX_VALUE.  The HashTableChained class
 *  implements only the compression function, which maps the hash code to
 *  a bucket in the table's range.
 *
 *  DO NOT CHANGE ANY PROTOTYPES IN THIS FILE.
 **/

public class HashTableChained implements Dictionary {

  /**
   *  Place any data fields here.
   **/

  private float loadFactor = 0.8f;
  private int size;
  private int bucketSize;
  private DList[] data;

  /** 
   *  Construct a new empty hash table intended to hold roughly sizeEstimate
   *  entries.  (The precise number of buckets is up to you, but we recommend
   *  you use a prime number, and shoot for a load factor between 0.5 and 1.)
   **/

  public HashTableChained(int sizeEstimate) {
    // Your solution here.
    while(!isPrime(sizeEstimate)){
      sizeEstimate++;
    }
    initHash(sizeEstimate);
  }
  
  private boolean isPrime(int a){
    for(int i = 2; i < Math.sqrt(a); i++){
      if(a % i == 0) return false;
    }
    return true;
  }
  
  /** 
   *  Construct a new empty hash table with a default size.  Say, a prime in
   *  the neighborhood of 100.
   **/

  public HashTableChained() {
    // Your solution here.
    initHash(101);
  }
  
  private void initHash(int bSize){
    bucketSize = bSize;
    size = 0;
    data = new DList[bucketSize];
    for(int i = 0;i < bucketSize; i++){
      data[i] = new DList();
    }
  }

  /**
   *  Converts a hash code in the range Integer.MIN_VALUE...Integer.MAX_VALUE
   *  to a value in the range 0...(size of hash table) - 1.
   *
   *  This function should have package protection (so we can test it), and
   *  should be used by insert, find, and remove.
   **/

  int compFunction(int code) {
    int a,b,p,N;
    a = 7;
    b = 11;
    p = 6707;
    N = bucketSize;
    // Replace the following line with your solution.
    return Math.abs(((code * a + b) % p) % N);
  }

  /** 
   *  Returns the number of entries stored in the dictionary.  Entries with
   *  the same key (or even the same key and value) each still count as
   *  a separate entry.
   *  @return number of entries in the dictionary.
   **/

  public int size() {
    // Replace the following line with your solution.
    return size;
  }

  /** 
   *  Tests if the dictionary is empty.
   *
   *  @return true if the dictionary has no entries; false otherwise.
   **/

  public boolean isEmpty() {
    // Replace the following line with your solution.
    return size==0;
  }

  /**
   *  Create a new Entry object referencing the input key and associated value,
   *  and insert the entry into the dictionary.  Return a reference to the new
   *  entry.  Multiple entries with the same key (or even the same key and
   *  value) can coexist in the dictionary.
   *
   *  This method should run in O(1) time if the number of collisions is small.
   *
   *  @param key the key by which the entry can be retrieved.
   *  @param value an arbitrary object.
   *  @return an entry containing the key and value.
   **/

  public Entry insert(Object key, Object value) {
    // Replace the following line with your solution.
    int thisHashCode = compFunction(key.hashCode());
    Entry thisEntry = new Entry();
    thisEntry.key = key;
    thisEntry.value = value;
    data[thisHashCode].insertBack(thisEntry);
    size ++;
    return thisEntry; 
  }

  /** 
   *  Search for an entry with the specified key.  If such an entry is found,
   *  return it; otherwise return null.  If several entries have the specified
   *  key, choose one arbitrarily and return it.
   *
   *  This method should run in O(1) time if the number of collisions is small.
   *
   *  @param key the search key.
   *  @return an entry containing the key and an associated value, or null if
   *          no entry contains the specified key.
   **/

  public Entry find(Object key) {
    // Replace the following line with your solution.
    int thisHashCode = compFunction(key.hashCode());
    DListNode cur = (DListNode)data[thisHashCode].front();
    Entry thisItem = null;
    try{
      while(cur.isValidNode()){
        thisItem = (Entry)cur.item();
        if(thisItem.key.equals(key)){
          return thisItem;
        }
        cur = (DListNode)cur.next();
      }
    }catch(Exception e){
      e.printStackTrace();
    }
    
    return thisItem;
  }

  /** 
   *  Remove an entry with the specified key.  If such an entry is found,
   *  remove it from the table and return it; otherwise return null.
   *  If several entries have the specified key, choose one arbitrarily, then
   *  remove and return it.
   *
   *  This method should run in O(1) time if the number of collisions is small.
   *
   *  @param key the search key.
   *  @return an entry containing the key and an associated value, or null if
   *          no entry contains the specified key.
   */

  public Entry remove(Object key) {
    // Replace the following line with your solution.
    int thisHashCode = compFunction(key.hashCode());
    DList thisList = data[thisHashCode];
    Entry tmpEntry = null;
    try{
      if(!thisList.isEmpty()){
        DListNode tmpNode = (DListNode)thisList.front();
        tmpEntry = (Entry)tmpNode.item();
        tmpNode.remove();
      }
    } catch (Exception e){
      e.printStackTrace();
    }
    return tmpEntry;
  }

  /**
   *  Remove all entries from the dictionary.
   */
  public void makeEmpty() {
    initHash(bucketSize);
  }
  
  public String toString(){
    String result = "";
    for(int i = 0; i < bucketSize;i++){
      result += ("["+data[i].length()+"]");
    }
    return result;
  }
  
  public static void main(String[] args){
	  HashTableChained t = new HashTableChained(13);
	  t.insert("apple", 89);
	  System.out.println(t.find("apple").value);
    HashTableChained t1 = new HashTableChained(97);

    System.out.println(t1.find("weed"));
    System.out.println(t1.size());
    t1.makeEmpty();
    System.out.println(t1.isEmpty());

    System.out.println(t1.isPrime(24));
    System.out.println(t1.size);
    System.out.println(t.isEmpty());
    System.out.println(t.remove("banana"));
    System.out.println(t.isEmpty());
    System.out.println(t.insert("aoe", 99));

  }
}
