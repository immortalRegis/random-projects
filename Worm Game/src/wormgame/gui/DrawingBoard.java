/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package wormgame.gui;
import java.awt.Color;
import wormgame.game.WormGame;
import javax.swing.*;
import wormgame.domain.*;
import java.awt.Graphics;
/**
 *
 * @author shegs
 */
public class DrawingBoard extends JPanel implements Updatable{
    private WormGame drawWormGame;
    private int pieceLength;

    public DrawingBoard(WormGame drawWormGame, int pieceLength) {
        this.drawWormGame = drawWormGame;
        this.pieceLength = pieceLength;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLACK);
        for (Piece p : this.drawWormGame.getWorm().getPieces()) {
            g.fill3DRect(p.getX()*this.pieceLength, p.getY()*this.pieceLength, this.pieceLength, this.pieceLength, true);
        }
        g.setColor(Color.RED);
        Apple ap = this.drawWormGame.getApple();
        g.fillOval(ap.getX()*this.pieceLength, ap.getY()*this.pieceLength, this.pieceLength, this.pieceLength);
    }

    @Override
    public void update() {
        super.repaint();
    }
}

