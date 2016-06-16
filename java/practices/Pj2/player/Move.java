/* Move.java  */

package player;

/**
 *  A public class for holding all the fields in a move.  This class is a
 *  container for data, not an ADT; hence, all fields are public.
 *
 *  The moveKind field stores the type of move.  The x-coordinates index the
 *  horizontal direction (left to right) and the y-coordinates index the
 *  vertical direction (top to bottom).  x- and y-coordinates start at zero.
 *
 *  DO NOT CHANGE THIS FILE.
 */
public class Move {

  public final static int QUIT = 0;
  public final static int ADD = 1;
  public final static int STEP = 2;

  public int moveKind;  // ADD, STEP, or QUIT.
                        
  public int x1;        // If moveKind == ADD, then x1, y1 are the new
  public int y1;        //   position in which a chip is being added;
  public int x2;        //   x2, y2 are unused.
  public int y2;        // If moveKind == STEP, then x1, y1 are the new
                        //   position, and x2, y2 are the old position
                        //   of the chip.
                        // If moveKind == QUIT, then x1, x2, y1, y2 are unused.

  // Construct a step move. 
  public Move(int xx1, int yy1, int xx2, int yy2) {
    moveKind = STEP;
    x1 = xx1;
    x2 = xx2;
    y1 = yy1;
    y2 = yy2;
  }

  // Construct an add move. 
  public Move(int x, int y) {
    moveKind = ADD;
    x1 = x;
    y1 = y;
  }

  // Construct a quit move. 
  public Move() {
    moveKind = QUIT;
  }

  // toString() converts the move to a String.
  public String toString() {
    switch (moveKind) {
    case QUIT:
      return "[quit]";
    case ADD:
      return "[add to " + x1 + "" + y1 + "]";
    default:
      return "[step from " + x2 + "" + y2 + " to " + x1 + "" + y1 + "]";
    }
  }

}
