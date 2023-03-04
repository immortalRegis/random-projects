/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package wormgame.domain;

/**
 *
 * @author shegs
 */
public class Piece {
    private int x;
    private int y;
    
    public Piece(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
    
    public int getX ()
    {
        return this.x;
    }
    
    public int getY()
    {
        return this.y;
    }
    
    public boolean runsInto(Piece piece)
    {
        return (getX() == piece.getX() && getY() == piece.getY());            
    }
    
  
    
    @Override
    public String toString()
    {
        return "(" + getX() + "," + getY() + ")";
    }
}
