import pygame,sys
from pygame.locals import *
import numpy as np
import pandas as pd


   


def capDatos(texto=None):
    #si no se le pasa a la funcion una frase entra en el bucle y coge una frase
    if texto is None:
        #frase que va a pedir al usuario que escriba
        texto="Recordaréis este día como el día en que casi capturáis al capitán Jack Sparrow"
    #inicializamos pygame
    pygame.init()
    #seleccionamos una variable que es el tamaño de la ventana
    WINDOW_SIZE = (500, 500)
    #inicializamos la ventana
    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Keystroke Dynamics")
    #texto que vamos a ir guardando lo que pulsamos
    textointrod=''
    #variable que contiene el tipo de letra y el tamaño
    font = pygame.font.SysFont('arial', 20 )
    #seleccionamos el el color en nuestro caso es blanco ya que el fondo es negro
    text = font.render(texto, True, (255, 255, 255))
    #escribimos la X e Y de donde vamos a posicionar el texto que vamos a pedir al usuario
    screen.blit(text, (0,0))
    #y mostramos todo
    pygame.display.flip()
    #creamos una variable para el while
    X=True
    #y creamos un array que es donde vamos a guardar las teclas que vamos pulsando
    teclas=[]

    while X:
        for event in pygame.event.get():
            #si pulsamos cerrar la pantalla se acaba el bucle while
            if event.type == QUIT:
                X=False
            elif event.type == KEYDOWN:
                #guardamos en el array la tecla pulsada, keydown y el tiempo
                teclas.append([pygame.key.name(event.key),'KeyDown',pygame.time.get_ticks()])
                #si es un backspace elimina el ultimo caracter si puede si no imprime a y continua con el codigo
                if event.key==8:
                    try:
                        textointrod=textointrod[:-1]
                    except:
                        print('a')
                else:
                    #si no es un backspace lo añade a la variable textointrod
                    textointrod=textointrod+str(event.unicode)
                # y rellenamos todo el fondo de negro y pintamos otra vez todo el texto que pide al usuario escribir y el texto introducido
                text = font.render(texto, True, (255, 255, 255))
                textintrod = font.render(textointrod, True, (255, 255, 255))
                screen.fill((0, 0, 0))
                screen.blit(text, (0,0))
                screen.blit(textintrod, (0,25))
                pygame.display.flip()
                
            elif event.type == KEYUP:
                #guardamos en el array la tecla pulsada, KeyUp y el tiempo
                teclas.append([pygame.key.name(event.key),'KeyUp',pygame.time.get_ticks()])
            
    #cerramos la pantalla
    pygame.quit()
    #pasamos el array a un array de numpy
    teclas=np.array(teclas, dtype='str')
    # todavia por definir pero si no hay 50 letras vuelcve a jecutarse el codigo (llamada recursiva)
    if len(teclas)<100:
        capDatos()
    return teclas

if __name__ == "__main__":
    Datos=capDatos()
    print(len(Datos))
    np.save('bea2.npy', Datos)