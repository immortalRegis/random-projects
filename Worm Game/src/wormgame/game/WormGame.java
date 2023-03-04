package wormgame.game;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;
import javax.swing.Timer;
import wormgame.Direction;
import wormgame.gui.Updatable;
import wormgame.domain.*;
import java.util.Random;
import java.util.List;

public class WormGame extends Timer implements ActionListener {

    private int width;
    private int height;
    private boolean continues;
    private Updatable updatable;
    private Worm worm;
    private Apple apple;
    private Random rand;
    
    public WormGame(int width, int height) {
        super(1000, null);

        this.width = width;
        this.height = height;
        this.continues = true;
        this.rand = new Random();
        
        worm = new Worm(width/2, height/2, Direction.DOWN);
        
        this.apple = freeApple();
        
        addActionListener(this);
        setInitialDelay(2000);

    }
    
    private Apple freeApple()
    {
        int appleX, appleY;
        Apple app;
        
        appleX = rand.nextInt(this.width);
        appleY = rand.nextInt(this. height);
            
        app = new Apple(appleX, appleY);
            
        while(worm.runsInto(app))
        {
            appleX = rand.nextInt(this.width);
            appleY = rand.nextInt(this. height);
            
            app = new Apple(appleX, appleY);
        }   
            
        
        return app;
    }
    
    public void setWorm(Worm worm)
    {
        this.worm = worm;
    }
    
    public Worm getWorm()
    {
        return this.worm;
    }
    
    public void setApple(Apple apple)
    {
        this.apple = apple;
    }
    
    public Apple getApple()
    {
        return this.apple;
    }
    
    public boolean continues() {
        return continues;
    }

    public void setUpdatable(Updatable updatable) {
        this.updatable = updatable;
    }

    public int getHeight() {
        return height;
    }

    public int getWidth() {
        return width;
    }

    @Override
    public void actionPerformed(ActionEvent ae) {
        if(!continues){
        return;
        }
      
        worm.move();
        
        if(worm.runsInto(apple))
        {
            worm.grow();
            setApple(freeApple());
        }
        
        if(worm.runsIntoItself())
            this.continues = false;
        for(Piece p : worm.getPieces())
        {
            if(p.getX() >= this.width || p.getX() < 0 || p.getY() >= this.height || p.getY() < 0)
            {
                continues = false;
            }
                }
        
        this.updatable.update();
        super.setDelay(1000/worm.getLength());
    
    }

}
