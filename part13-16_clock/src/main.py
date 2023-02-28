# WRITE YOUR SOLUTION HERE:
import pygame
import math
import datetime

pygame.init()
width = 640
height = 480

screen = pygame.display.set_mode((width,height))


def get_endpoint(radius, angle):
    x = math.sin(2*math.pi*angle/360) * radius
    y = math.cos(2*math.pi*angle/360)*radius
    return (x + (width/2), -(y - height/2))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    current_time = datetime.datetime.now()
    seconds = current_time.second
    minutes = current_time.minute
    hour = current_time.hour
    screen.fill((0,0,0))
    pygame.display.set_caption(current_time.strftime('%H:%M:%S'))

    pygame.draw.circle(screen,(255, 0 , 0) ,(320, 240), 200, 2 )
    pygame.draw.circle(screen,(255, 0 , 0) ,(320, 240), 15 )

    #hour
    hour_radius = 130
    hour_angle = (hour+minutes/60+seconds/3600)*(360/12)
    pygame.draw.line(screen, (0,0,255), (320,240), get_endpoint(hour_radius, hour_angle),4)
    
    #minutes
    min_radius = 160
    min_angle = (minutes+seconds/60)*(360/60)
    pygame.draw.line(screen, (0,0,255), (320,240), get_endpoint(min_radius, min_angle),2)
    
    #seconds
    sec_radius = 190
    sec_angle = seconds*(360/60)
    pygame.draw.line(screen, (0,0,255), (320,240), get_endpoint(sec_radius, sec_angle),1)
    
    pygame.display.flip()
