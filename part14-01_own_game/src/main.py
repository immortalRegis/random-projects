# Complete your game here
import pygame
import math
from random import randint

class Own_Game:
    def __init__(self):
        pygame.init()

        self.height = 480
        self.width = 640

        self.coin = pygame.image.load('C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part14-01_own_game/src/coin.png')
        self.monster = pygame.image.load('C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part14-01_own_game/src/monster.png')
        self.robot = pygame.image.load('C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part14-01_own_game/src/robot.png')
        
        
        self.to_left = False
        self.to_right = False

        self.robot_x = 0
        self.robot_y = self.height - self.robot.get_height()

        self.points = 0

        self.coins = []
        self.monsters = []

        

        for i in range(5):
            self.coins.append([randint(0, self.width - self.coin.get_width()), -randint(100, 200)])
        
        for i in range(5):
            self.monsters.append([randint(0, self.width - self.monster.get_width()), -randint(100, 200)])


        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Coin Game")

        self.game_font = pygame.font.SysFont("Arial", 24)
        self.text = self.game_font.render("Points: " + str(self.points), True, (255, 0, 0))

        self.game_over = False
        self.main_loop()    

    def collision_occurs(self, objectx, objecty, robot_x, robot_y):
        x_distance = objectx - robot_x
        y_distance = objecty - robot_y

        x_distance *= x_distance
        y_distance *= y_distance

        distance_in_pixels = math.sqrt(x_distance + y_distance)
        return distance_in_pixels < 40

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.to_left = True
                    if event.key == pygame.K_RIGHT:
                        self.to_right = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.to_left = False
                    if event.key == pygame.K_RIGHT:
                        self.to_right = False
                    
            if self.game_over:
                self.text = self.game_font.render(f"Game Over! You scored {self.points} points", True, (255, 0, 0))
                self.screen.blit(self.text, (320, 240))
                pygame.display.flip()
            else:            
                for i in range(5):
                    #coin falls down
                    if self.coins[i][1]+self.coin.get_height() < self.height:
                        self.coins[i][1] += 1
                    #if sprite takes coin, add 1 point to player
                        if self.collision_occurs(self.coins[i][0], self.coins[i][1], self.robot_x, self.robot_y):
                            self.points += 1
                            self.coins[i][0] = randint(0,self.width-self.coin.get_width())
                            self.coins[i][1] = -randint(100,1000)
                    else:
                        self.coins[i][0] = randint(0,self.width-self.coin.get_width())
                        self.coins[i][1] = -randint(100,1000)
                    #if monster touches sprite, game over
                    if self.monsters[i][1] + self.monster.get_height() < self.height:
                        self.monsters[i][1] += 1
                        if self.collision_occurs(self.monsters[i][0], self.monsters[i][1], self.robot_x, self.robot_y):
                            self.game_over = True
                            self.monsters[i][0] = randint(0,self.width-self.coin.get_width())
                            self.monsters[i][1] = -randint(100,1000)
                    else:
                        self.monsters[i][0] = randint(0,self.width-self.coin.get_width())
                        self.monsters[i][1] = -randint(100,1000)       
                

                if self.to_right and (self.robot_x + 2) + self.robot.get_width() <= self.width:
                    self.robot_x += 2
                if self.to_left and (self.robot_x - 2) >= 0:
                    self.robot_x -= 2

                self.screen.fill((0,0,200))

                for i in range(5):
                    self.screen.blit(self.coin, (self.coins[i][0], self.coins[i][1]))
                    self.screen.blit(self.monster, (self.monsters[i][0], self.monsters[i][1]))
                
                self.text = self.game_font.render("Points: " + str(self.points), True, (255, 0, 0))
                self.screen.blit(self.text, (500, 10))
                self.screen.blit(self.robot, (self.robot_x,self.robot_y))
                pygame.display.flip()
                clock = pygame.time.Clock().tick(60)



if __name__ == "__main__":
    Own_Game()