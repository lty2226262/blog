/* Player.java */

package player;

/**
 *  A class that is extended by all Network players (human and machine).
 *
 *  DO NOT CHANGE THIS FILE.
 */
public abstract class Player {
  // This player's name as recognized by the game Network.
  public String myName;

  // Returns a new move by "this" player.  Internally records the move (updates
  // the internal game board) as a move by "this" player.
  public abstract Move chooseMove();

  // If the Move m is legal, records the move as a move by the opponent
  // (updates the internal game board) and returns true.  If the move is
  // illegal, returns false without modifying the internal state of "this"
  // player.  This method allows your opponents to inform you of their moves.
  public abstract boolean opponentMove(Move m);

  // If the Move m is legal, records the move as a move by "this" player
  // (updates the internal game board) and returns true.  If the move is
  // illegal, returns false without modifying the internal state of "this"
  // player.  This method is used to help set up "Network problems" for your
  // player to solve.
  public abstract boolean forceMove(Move m);

}
