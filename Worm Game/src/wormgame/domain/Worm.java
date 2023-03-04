/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package wormgame.domain;
import wormgame.Direction;
import java.util.List;
import java.util.ArrayList;
/**
 *
 * @author shegs
 */
public class Worm {
    private List<Piece> wormList;
    private Direction direction;
    private int x;
    private int y;
    private int lengthLimit;
    
    public Worm(int originalX, int originalY, Direction originalDirection)
    {
        wormList = new ArrayList<Piece>();
        wormList.add(new Piece(originalX, originalY));
        
        direction = originalDirection;
        x = originalX;
        y = originalY;
        lengthLimit = 3;
    }
    
    public Direction getDirection()
    {
        return direction;
    }
    
    public void setDirection(Direction dir)
    {
        direction = dir;
    }
    
    public List<Piece> getPieces()
    {
        return wormList;
    }
    
    public int getLength()
    {
        return wormList.size();
    }
    
    public void move()
    {
        Direction dir = getDirection();
        
        if(wormList.size() == lengthLimit)
            wormList.remove(0);
        
        if(dir == Direction.RIGHT)
            {
                this.x++;
                wormList.add(new Piece(x, y));
            }
        else if(dir == Direction.LEFT)
            {
                this.x--;
                wormList.add(new Piece(x, y));
            }
        else if(dir == Direction.DOWN)
            {
                this.y++;
                wormList.add(new Piece(x, y));
            }
         else
            {
                this.y--;
                wormList.add(new Piece(x, y));
            }
        
        
        
         
        
        
    }
    
    public void grow()
    {
        if(wormList.size() > 2)
            lengthLimit++;
    }
    
    public boolean runsInto(Piece piece)
    {
        for(Piece worm: wormList){
            if(worm.getX() == piece.getX() && worm.getY() == piece.getY())
                return true;
        }
        return false;
    }
    
    public boolean runsIntoItself()
    {
        int count = 0;
        
        // I hope this works! pick an element from the wormList
        // Get the coordinates of the element. Compare its coordinates
        // with the coordinates of every Piece object in the wormList
        // The coordinates must match at least one Piece (which is itself
        // If the coordinates match more than one piece, then there's an
        // overlap. 
        for(Piece worm: wormList)
        {
            count = 0;
            for(Piece wm: wormList)
            {
                if(worm.getX() == wm.getX() && worm.getY() == wm.getY())
                    count++;
            }
            
        }
        
        return (count > 1);
    }
    
}
