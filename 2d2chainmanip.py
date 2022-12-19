import sys, pygame, math
from pygame.locals import*

width=600
height=600
Color_screen=(49,150,100)
Color_line=(255,0,0)
Color_arm2 = (0,0,255)
center_x = 300
center_y = 300
circle_radius = 100
arm_radius = 60
base_angle = 0
arm_angle = 0
e = 5
timer = pygame.time.Clock()
fps=30
pos = (50,50)

def main():
    screen=pygame.display.set_mode((width,height))

    global base_angle, arm_angle, pos
    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
            if events.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                #print(pos)
        #print(pos)
        screen.fill(Color_screen)
        x_end = pos[0]
        y_end = pos[1]
        pygame.draw.circle(screen, Color_line,  pos, 4)   
        
       # end_angle = math.atan((y_end - center_y)/(x_end-center_x))
        #end_angle = math.pi*2
        #base_angle = (end_angle - base_angle)/10
        x1 = (circle_radius*math.cos(base_angle))+center_x
        y1 = (circle_radius*math.sin(base_angle))+center_y
        #print(abs(x1*x1-x_end*x_end)+abs(y1*y1-y_end*y_end))
        delta =  math.sqrt((x1-x_end)**2+(y1-y_end)**2)
        
        if delta <= arm_radius + e and delta >= arm_radius - e:
            
            x2 = x1 + (arm_radius*math.cos(arm_angle))
            y2 = y1 + (arm_radius*math.sin(arm_angle))
            delta2 = math.sqrt((x2-x_end)**2+(y2-y_end)**2)
            if delta2 > e or delta2 < -e :
                arm_angle += 0.5
            #arm_angle = math.atan((y_end - y1)/(x_end-x1))
            print (delta2)
            pygame.draw.line(screen, Color_arm2, (x1,y1 ), (x2,y2 ))
        else:
            base_angle +=  0.5
        pygame.draw.line(screen, Color_line, (center_x,center_y), ((x1, y1)), 5)
        
        
        pygame.display.flip()
        timer.tick(fps)
        #if (math.sqrt((x1*x1-x_end*x_end)+(y1*y1-y_end*y_end))) == arm_radius:



main()