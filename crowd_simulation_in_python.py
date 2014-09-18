import pygame, sys,os
from pygame.locals import * 
from random import random, uniform, randrange
from math import sqrt, e, pi, cos, sin, atan
#--------------------------------------------------------------------------
#Anagent class
class anagent:
    def __init__(self, x, y):
        
        #position
        self.x = x
        self.y = y
        
        self.tx = x
        self.ty = y
        
        self.dx = 0
        self.dy = 0
        self.v = uniform(0.5, 2.5) #speed
        self.idle = False
        
    def setTarget(self,x,y):
        self.tx = x
        self.ty = y

#--------------------------------------------------------------------------
#Basic Setup
pygame.init() 
w=400
h=400
window = pygame.display.set_mode((w, h)) 
pygame.display.set_caption('Crowd Sim') 
screen = pygame.display.get_surface() 
layer1 = pygame.Surface((w,h))
layer1.fill((0,0,0))
layer1.set_colorkey((0,0,0))

#POT_EXTEND = 30         #how much the potential extends forwards from a person
#POT_DECAY = 0.01        #how fast the potential function decays per agent
POT_EXTEND = 22
POT_DECAY = 0.027
POT_STRENGTH = 350         #how much the agents are affected by the potential field

POT_DRAWFIELD = True    #draw the potential field?

iter = 0

PPL = 20
agent = []
footman = (pygame.image.load("C:/footman_1.gif"),pygame.image.load("C:/footman_2.gif"),pygame.image.load("C:/footman_3.gif"))
ttt = 0
#--------------------------------------------------------------------------
#Defs

#handler for events
def input(events): 
    global POT_EXTEND
    global POT_DECAY
    global POT_STRENGTH
    global POT_DRAWFIELD
    global agent
    global layer1
    for event in events: 
        if event.type == QUIT: 
            sys.exit(0) 
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit(0)
            elif event.key == K_i:
                POT_EXTEND += 1
                print "POT_EXTEND = " + `POT_EXTEND`
            elif event.key == K_u:
                POT_EXTEND -= 1
                print "POT_EXTEND = " + `POT_EXTEND`
            elif event.key == K_j:
                POT_DECAY -= 0.001
                print "POT_DECAY = " + `POT_DECAY`
            elif event.key == K_k:
                POT_DECAY += 0.001
                print "POT_DECAY = " + `POT_DECAY`
            elif event.key == K_m:
                POT_STRENGTH += 20
                print "POT_STRENGTH = " + `POT_STRENGTH`
            elif event.key == K_n:
                POT_STRENGTH -= 20
                print "POT_STRENGTH = " + `POT_STRENGTH`
            elif event.key == K_f:
                POT_DRAWFIELD = not POT_DRAWFIELD
                print "draw field toggled"
            elif event.key == K_r:
                agent = []
                resetAgents()
                layer1.fill((0,0,0))
                print "Agents reset"
#return total danger due to all agents from position x,y
def totalDangerAt(x, y):
    global agent
    danger = 0
    for a in agent:
       danger += dangerDue(x,y,a)
    return danger

#return danger to an agent a from position x,y
def dangerDue(x, y, a):
    global POT_EXTEND
    global POT_DECAY
    px2 = a.x + POT_EXTEND*a.dx
    py2 = a.y + POT_EXTEND*a.dy
    d1 = sqrt((a.x - x)**2 + (a.y - y)**2)
    d2 = sqrt((px2 - x)**2 + (py2 - y)**2)
    danger = e**(-POT_DECAY*(d1 + d2))
    return danger


#return the gradient of danger at position x,y due to agent a
def gradDangerDue(x,y,a):
    global POT_EXTEND
    global POT_DECAY
    px2 = a.x + POT_EXTEND*a.dx
    py2 = a.y + POT_EXTEND*a.dy
    d1 = sqrt((a.x - x)**2 + (a.y - y)**2)
    d2 = sqrt((px2 - x)**2 + (py2 - y)**2)
    danger = e**(-POT_DECAY*(d1 + d2))
    
    multiplierx = -POT_DECAY*(x - a.x)/(2*d1) - POT_DECAY*(x - px2)/(2*d2)
    multipliery = -POT_DECAY*(y - a.y)/(2*d1) - POT_DECAY*(y - py2)/(2*d2)
    
    return (danger*multiplierx, danger*multipliery)

#return the total gradient of danger at position x,y due to all agents
def gradDangerAt(x, y):
    global agent
    totx = 0
    toty = 0
    for a in agent:
        if not (a.x == x and a.y == y):
            res = gradDangerDue(x, y, a)
            totx += res[0]
            toty += res[1]
    return (totx, toty)

#generate agents
def resetAgents():
    global agent, PPL, w, h
    for i in range (0, PPL):
        if i < PPL/2: #left and right walkers
            newagent = anagent(w/10 + uniform(-100,100),random()*h/2 + h/4)
            newagent.setTarget(w +10,newagent.y)
            #newagent.setTarget(w/2,h/2)
        else:
            newagent = anagent(w - w/10 + uniform(-100,100),random()*h/2 + h/4)
            newagent.setTarget(-10,newagent.y)
            #newagent.setTarget(w/2,h/2)
        
        newagent.idle = False
        
        agent.append(newagent)

#at corners
def resetAgents2():
    global agent, PPL, w, h
    n = PPL/4
    for i in range(n):
        newagent = anagent(uniform(0, 100),uniform(0, 100))
        newagent.setTarget(w,h)
        newagent.idle = False
        agent.append(newagent)
    for i in range(n):
        newagent = anagent(uniform(w-100, w),uniform(0, 100))
        newagent.setTarget(0,h)
        newagent.idle = False
        agent.append(newagent)
    for i in range(n):
        newagent = anagent(uniform(0, 100),uniform(h-100, h))
        newagent.setTarget(w,0)
        newagent.idle = False
        agent.append(newagent)
    for i in range(n):
        newagent = anagent(uniform(w-100,w),uniform(h-100, h))
        newagent.setTarget(0,0)
        newagent.idle = False
        agent.append(newagent)
        
#in circle
def resetAgents3():
    global agent, PPL, w, h
    r = min(w, h)*0.9/2
    incr = 2*pi/PPL
    for i in range(PPL):
        newagent = anagent(w/2 + r*cos(incr*i), h/2 + r*sin(incr*i))
        newagent.setTarget(w/2 + r*cos(incr*i + pi), h/2 + r*sin(incr*i + pi))
        agent.append(newagent)

#from all over the place to middle
def resetAgents4():
    global agent, PPL, w, h
    for i in range(PPL):
        newagent = anagent(uniform(-w, 2*w), uniform(-h, 2*h))
        newagent.setTarget(w/2, h/2)
        agent.append(newagent)
        
#--------------------------------------------------------------------------
resetAgents3()
#MAIN LOOP
while True: 
   input(pygame.event.get()) 
   pygame.time.delay(30)
   
   screen.fill((0,0,50))
   
   if POT_DRAWFIELD:
       #calculate the danger field
       for x in range(0,w,10):
           for y in range(0,h,10):
               
               danger = 2*POT_STRENGTH*totalDangerAt(x,y)
               
               #print danger
               dng = 0
               if danger > 255:
                   dng = danger - 255
                   danger = 255
               
               if dng > 255:
                   dng = 255
    
               pygame.draw.circle(screen, (danger,dng,0), (x,y), 7)
           
   #update agents
   for a in agent:
       dx = 0
       dy = 0
           
       if not a.idle:
           d = sqrt((a.tx - a.x)**2 + (a.ty - a.y)**2)
               
           if d > a.v:
               dx = a.v*(a.tx - a.x)/d
               dy = a.v*(a.ty - a.y)/d
           else:
               #a.idle = True
               a.setTarget(random()*w, random()*h)
               
               #if random() < 0.5:
               #    a.x = -30
               #    a.y = random()*h/2 + h/4
               #    a.setTarget(w +10,a.y)
               #else:
               #    a.x = w + 30
               #    a.y = random()*h/2 + h/4
               #    a.setTarget(-10,a.y)          
           
       #now calculate force due to poptential at this point.
       #we do this by summing up all the gradients at this point
       #of all functions that each agent generates.
       gradx,grady = gradDangerAt(a.x,a.y)
       gradx = -gradx*POT_STRENGTH
       grady = -grady*POT_STRENGTH
       #print gradx,grady
       dx += gradx
       dy += grady
       #pygame.draw.circle(screen, (0, 255, 0) , (a.x + a.dx, a.y + a.dy), 10, 5)
       #pygame.draw.circle(screen, (255, 255, 255) , (a.tx, a.ty), 5, 1)
       
       pygame.draw.line(screen, (255,255,0), (a.x,a.y), (a.tx, a.ty))
       #pygame.draw.line(screen, (0,0,255), (a.x,a.y), (a.x+30*gradx, a.y+30*grady)) 
           
       #normalize velocity to agents speed
       lengthv = sqrt(dx*dx + dy*dy)
       dx = a.v*dx/lengthv
       dy = a.v*dy/lengthv
       
       pygame.draw.line(layer1, (50,50,0), (a.x,a.y), (a.x + a.dx, a.y + a.dy))
       a.x += dx
       a.y += dy
       a.dx = dx
       a.dy = dy
       
       #draw agent and his direction of motion
       #pygame.draw.circle(screen, (255, 255, 0) , (a.x, a.y), 17, 1)
       #ang = atan(a.dy/a.dx)
       #if a.dx < 0:
       #    ang += pi
       
       #nf =pygame.transform.rotate(footman[int(ttt)],90 - ang*180/pi)
       #ttt+=0.025
       #if ttt > 3:
       #    ttt = 0
       #screen.blit(nf, (a.x - nf.get_rect().width/2, a.y - nf.get_rect().height/2))
       
       pygame.draw.circle(screen, (0, 255, 255) , (a.x, a.y), 10, 1)
       pygame.draw.line(screen, (255,255,255), (a.x,a.y), (a.x+6*a.dx, a.y+6*a.dy))
       
       
   #pygame.draw.line(screen, (255,255,255), (px,py), pygame.mouse.get_pos())
   #pygame.draw.circle(screen, (0, 255, 0) , (px, py), 10)
   #screen.blit(layer1, (0,0))
   
   pygame.display.flip()
   #pygame.image.save(screen, "C:\pics\p" + `iter` + ".bmp")
   #iter += 1
