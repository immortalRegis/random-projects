# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")

robot_x = 0
robot_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            robot_x = event.pos[0]-robot.get_width()/2
            robot_y = event.pos[1]-robot.get_height()/2
            window.fill((0, 0, 0))
            window.blit(robot, (robot_x, robot_y))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            exit(0)
