#https://stackoverflow.com/questions/50534617/draw-a-line-in-pygame

import sys, pygame, math
from pygame.locals import*

width=1000
height=500
Color_screen=(49,150,100)
Color_line=(255,0,0)
Color_arm2 = (0,0,255)
center_x = 300
center_y = 300
circle_radius = 100
arm_radius = 60
base_angle = 0
arm_angle = 0
timer = pygame.time.Clock()
fps=30
pos = (0,0)

def main():
    screen=pygame.display.set_mode((width,height))

    global base_angle,arm_angle, pos
    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
            if events.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                #print(pos)
        print(pos)
        screen.fill(Color_screen)
        pygame.draw.circle(screen, Color_line,  pos, 10)    
        
        x1 = (circle_radius*math.cos(base_angle*math.pi/180))+center_x
        y1 = (circle_radius*math.sin(base_angle*math.pi/180))+center_y

        pygame.draw.line(screen, Color_line, (center_x,center_y), ((x1, y1)))
            
        x2 = x1 + (arm_radius*math.cos((base_angle+arm_angle)*math.pi/180))
        y2 = y1 + (arm_radius*math.sin((base_angle+arm_angle)*math.pi/180))
        pygame.draw.line(screen, Color_arm2, (x1,y1 ), (x2,y2 ))
        base_angle+=1
        arm_angle += 20
        pygame.display.flip()
        timer.tick(fps)
        
        

main()
