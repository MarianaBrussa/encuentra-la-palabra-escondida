import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano,
                correctas, incorrectas, casi, error, intentos, palabraCorrecta):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    fondo = pygame.image.load("fondo.png")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    screen.blit(fondo, (0, 0))

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)
    if not gano and segundos>0 and intentos>0:
    #muestra lo que escribe el jugador
        screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
        screen.blit(defaultFont.render("LA PALABRA DEBE TENER "+str(LARGO)+" CARACTERES", 1, COLOR_TEXTO), (190, 535))#avisa cuantas letras tiene la palabra
    #muestra el puntaje
        screen.blit(defaultFont.render("Puntos: " + str(leerPuntaje(1)), 1, COLOR_TEXTO), (680, 10))
        #dibujo en pantalla los posibles errores
        if error == 1:
            screen.blit(defaultFont.render("La palabra no tiene " + str(LARGO) + " caracteres", 1, COLOR_TEXTO), (450, 580))
        elif error == 2:
            screen.blit(defaultFont.render("La palabra no está en el diccionario", 1, COLOR_TEXTO), (450, 580))
        elif error == 3:
            screen.blit(defaultFont.render("La palabra ya se había ingresado", 1, COLOR_TEXTO), (450, 580))
            #muestra los segundos y puede cambiar de color con el tiempo
        if(segundos<15):
            ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)

        else:
            ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
        screen.blit(ren, (10, 10))

    #muestra las palabras anteriores, las que se fueron arriesgando
        pos =1
        for palabra in listaDePalabrasUsuario:
            screen.blit(defaultFontGrande.render(palabra, 1, COLOR_LETRAS), (ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//4,20 + 80 * pos))
            pos += 1

    #muestra el abcdario
    #el color del avecederario fue reconfigurado para que tenga el mismo color que el texto
        abcdario = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        y=0
        for abc in abcdario:
            x = 0
            color=COLOR_LETRAS
            for letra in abc: # se agregaron los colores de las letras correctas, incorrectas y casi en la configuracion
                if letra in correctas:
                    color = COLOR_VERDE
                elif letra in incorrectas:
                    color=COLOR_ROJO
                elif letra in casi:
                    color=COLOR_AMARILLO
                else:
                    color=COLOR_LETRAS
                screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
                x += TAMANNO_LETRA
            y += TAMANNO_LETRA
    elif gano: # se agrego musica de victoria cuando el jugador acierta

        pygame.mixer.music.load('Musica victoria.mp3')
        pygame.mixer.music.set_volume(0.08)
        pygame.mixer.music.play()
        actualizarRacha(True)

        screen.blit(defaultFontGrande.render("¡FELICIDADES, GANO!",1,COLOR_VERDE),(5,140))# cartel de ganador con la palabra correcta
        screen.blit(defaultFontGrande.render("LA PALABRA ES:",1,COLOR_VERDE),(100,220))
        screen.blit(defaultFontGrande.render("{"+palabraCorrecta.upper()+"}",1,COLOR_VERDE),(250,300))
        screen.blit(defaultFont.render("presione enter para continuar jugando, o [x] si desea salir del juego", 1, COLOR_TEXTO), (70,550))

        #MOSTRAR RACHA ACTUAL Y RACHA MAXIMA DE ARCHIVO
        screen.blit(defaultFont.render("Racha actual:"+str(leerPuntaje(1)),1,COLOR_TEXTO),(300,400))
        screen.blit(defaultFont.render("Record de racha:"+str(leerPuntaje(2)),1,COLOR_TEXTO),(300,450))


    else: # se agrego musica de derrota cuando el jugador pierde
        pygame.mixer.music.load('Musica derrota.mp3')
        pygame.mixer.music.set_volume(0.08)
        pygame.mixer.music.play()
        actualizarRacha(False)

        screen.blit(defaultFontGrande.render("PERDIO, LA PALABRA",1,COLOR_ROJO),(10,140)) # cartel de perdedor con la palabra correcta
        screen.blit(defaultFontGrande.render("ES",1,COLOR_ROJO),(350,220))
        screen.blit(defaultFontGrande.render("{"+palabraCorrecta.upper()+"}",1,COLOR_ROJO),(250,300))
        screen.blit(defaultFont.render("presione enter para continuar jugando, o [x] si desea salir del juego", 1, COLOR_TEXTO), (70,550))#Aviso al jugador si desea seguir jugando o salir

         #MOSTRAR RACHA ACTUAL Y RACHA MAXIMA DE ARCHIVO
        screen.blit(defaultFont.render("Racha actual:"+str(leerPuntaje(1)),1,COLOR_TEXTO),(300,400))
        screen.blit(defaultFont.render("Record de racha:"+str(leerPuntaje(2)),1,COLOR_TEXTO),(300,450))



#las  funciones siguientes se crearon par leer y guardar el record mas alto y lo borran en caso de que el usuario lo supere

def leerPuntaje(opcion): #se creo la funcion leer puntaje de archivo. 1 devuelve record actual, 2 devuelve maximo

    if not os.path.exists(ARCHIVO_RECORD): # Crea archivo si no existe
        with open(ARCHIVO_RECORD, 'w') as file:
            file.write("recordActual = 0\nrecordMaximo = 0\n")

    with open(ARCHIVO_RECORD, "r") as file:
        data = file.readlines()
        recordActual, recordMaximo = [d.split('=')[1].split('\n')[0] for d in data]

    recordActual = int(recordActual)
    recordMaximo = int(recordMaximo)

    if opcion:
        if opcion== 1:
            return recordActual
        if opcion== 2:
            return recordMaximo


def actualizarRacha(gano): # Mantener puntaje y escribir en archivo
    recordActual = leerPuntaje(1)
    recordMaximo = leerPuntaje(2)

    #Gano = True, calcular puntaje. False, resetear puntaje
    if gano:
        recordActual+=1
        if recordActual > recordMaximo:
            recordMaximo = recordActual
    else:
        recordActual=0

    with open(ARCHIVO_RECORD, 'w') as file:
        file.write("recordActual = " + str(recordActual)+"\nrecordMaximo = " + str(recordMaximo))





