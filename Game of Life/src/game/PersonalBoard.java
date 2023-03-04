/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package game;
import gameoflife.GameOfLifeBoard;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
/**
 *
 * @author shegs
 */
public class PersonalBoard extends GameOfLifeBoard{
    
    public PersonalBoard(int length, int height)
    {
        super(length, height);
        
    }
    
    @Override
    public void initiateRandomCells(double d) {
        int area = this.getHeight()*this.getWidth();
        double number = d * area;
        
       int amountInArray = (int) (Math.round(number));
       
       List<Boolean> trueValues = new ArrayList<Boolean>();
       
       for(int i = 0; i < amountInArray; i++)
       {
           trueValues.add(true);
       }
       
       if(amountInArray != area)
       {
           for(int i = amountInArray; i < area; i++)
            {
                trueValues.add(false);
            }
       }
       
       Collections.shuffle(trueValues);
       int k = 0;
       
       for(int i = 0; i < this.getWidth();i++)
       {
           for(int j = 0; j < this.getHeight(); j++)
           {
               super.getBoard()[i][j] = trueValues.get(k);
               k++;
           }
       }
    }

    @Override
    public boolean isAlive(int i, int i1) {
        if(!legal(i, i1))
            return false;
        return super.getBoard()[i][i1];  
    }

    @Override
    public void turnToLiving(int i, int i1) {
        
        if(legal(i, i1))
            super.getBoard()[i][i1] = true;
    }

    @Override
    public void turnToDead(int i, int i1) {
        if(legal(i, i1))
            super.getBoard()[i][i1] = false;
    }

    @Override
    public int getNumberOfLivingNeighbours(int i, int i1) {
        int neighbours = 0;
        
        if(isAlive(i, i1 + 1))
            neighbours++;
        if(isAlive(i, i1 -1))
            neighbours++;
        if(isAlive(i+1, i1 + 1))
            neighbours++;
        if(isAlive(i + 1, i1))
            neighbours++;
        if(isAlive(i + 1, i1 - 1))
            neighbours++;
        if(isAlive(i -1, i1 + 1))
            neighbours++;
        if(isAlive(i -1, i1))
            neighbours++;
        if(isAlive(i - 1, i1 - 1))
            neighbours++;
        
        
        return neighbours;
    }
    
    public boolean legal(int i, int i1)
    {
        if(i < 0 || i1 < 0 || i >= getWidth() || i1 >= getHeight())
            return false;
        return true;
    }
    
    @Override
    public void manageCell(int i, int i1, int i2) {
        if(i2 < 2)
            turnToDead(i, i1);
        if(i2 == 2)
        {}
        if(i2 == 3)
            turnToLiving(i, i1);
        if(i2 > 3)
            turnToDead(i, i1);
        
    }
    
}
