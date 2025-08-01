#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *

from funcionesVACIAS import *

#Funcion principal
def main():
    #Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()

    #Preparar la ventana
    pygame.display.set_caption("La escondida...")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial
    tiempoInicio = pygame.time.get_ticks()/1000 #tiempo de ejecución al momento de empezar la partida nueva


    error = 0
    puntos = 0
    palabraUsuario = ""
    listaPalabrasDiccionario=[]
    ListaDePalabrasUsuario=[]
    correctas = []
    incorrectas = []
    casi = []
    gano = False
    intentos = 5

    archivo= open("lemario.txt","r",encoding='utf-8')
    #lectura del diccionario
    lectura(archivo, listaPalabrasDiccionario, LARGO)

    #elige una al azar
    palabraCorrecta=nuevaPalabra(listaPalabrasDiccionario)

    dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos,segundos, gano, correctas, incorrectas, casi, error, intentos, palabraCorrecta)
    print(palabraCorrecta)


    while segundos > fps/1000 and intentos > 0 and not gano:
    # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        #Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            #QUIT es apretar la X en la ventana
            if e.type == QUIT:
                actualizarRacha(False)
                pygame.quit()
                sys.exit()

            #Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                palabraUsuario += letra #es la palabra que escribe el usuario
                if e.key == K_BACKSPACE:
                    palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                if e.key == K_RETURN:
                    #Verifica si la palabra ingresada por el usuario coincide con la longitud de la palabra correcta
                    if len(palabraUsuario) == len(palabraCorrecta):
                        #Verifica si la palabra ingresada está incluida en el diccionario
                        enDiccionario = False
                        for palabraDicc in listaPalabrasDiccionario:
                            if palabraUsuario == palabraDicc:
                                enDiccionario = True
                        if enDiccionario == True:
                            error = 0
                            #Verifica si la palabra ingresada ya había sido ingresada anteriormente
                            repetida = False
                            for palabraRepe in ListaDePalabrasUsuario:
                                if palabraUsuario == palabraRepe:
                                    repetida = True
                            if repetida == False:
                                gano = revision(palabraCorrecta, palabraUsuario, correctas, incorrectas, casi)
                                ListaDePalabrasUsuario.append(palabraUsuario)
                                palabraUsuario = ""
                                intentos -= 1

                            else:
                            #si la palabra está repetida, le avisa al usuario
                                error = 3
                                palabraUsuario = "" # vacio la palabra para que el usuario no tenga que borrar letra por letra en los tres condiciones de error
                        else:
                        #si la palabra no está en el diccionario, le avisa al usuario
                            error = 2
                            palabraUsuario = ""
                    else:
                    #si la palabra ingresada no tiene el largo que establece el juego, le avisa al usuario
                        error = 1
                        palabraUsuario = ""

        segundos = TIEMPO_MAX - (pygame.time.get_ticks()/1000 - tiempoInicio) #tiempo de ejecucion actual menos tiempo de inicio de partida actual, para que cuando se continua con enter el reloj no siga corriendo

        #Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        #Dibujar de nuevo todo
        dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos,segundos, gano, correctas, incorrectas, casi, error, intentos, palabraCorrecta)

        pygame.display.flip()

    while 1:

        #Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                actualizarRacha(False)
                pygame.quit()
                sys.exit() #si el usuario no apreta QUIT

            elif e.type == KEYDOWN:
                if  e.key == K_RETURN: #para continuar presiona la tecla enter
                    main()

    archivo.close()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
