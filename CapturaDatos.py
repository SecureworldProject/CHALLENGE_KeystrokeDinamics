import pygame,sys
from pygame.locals import *
import numpy as np
import pandas as pd
pygame.init()

WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Keystroke Dynamics")
X=True
teclas=[]
print(teclas)
#
while X:
    for event in pygame.event.get():
        if event.type == QUIT:
            X=False
        elif event.type == KEYDOWN:
            teclas.append([event.scancode,pygame.time.get_ticks(),'KEYDOWN'])
        elif event.type == KEYUP:
            teclas.append([event.scancode,pygame.time.get_ticks(),'KEYUP'])

pygame.quit()
vector=[]
UD=0
DD=0
for i in range(len(teclas)):
    if teclas[i][2]=='KEYDOWN':
        keyup=[]
        for j in range(i,len(teclas)):
            
            if teclas[j][2]=='KEYUP' and teclas[j][0]==teclas[i][0] :
                try:
                    keyup=teclas[j]
                    tiempul=abs(teclas[i][1]-teclas[j][1])
                    vector[-1].extend([teclas[i][0],tiempul,abs(UD-teclas[i][1]),abs(DD-teclas[i][1])])
                    vector.append([teclas[i][0],tiempul])
                    UD=teclas[j][1]
                    DD=teclas[i][1]
                except:
                    keyup=teclas[j]
                    UD=teclas[j][1]
                    DD=teclas[i][1]
                    tiempul=abs(teclas[i][1]-teclas[j][1])
                    vector.append([teclas[i][0],tiempul])
vector.pop(-1)
vector=np.array(vector)
np.save('array.npy', vector)
            

