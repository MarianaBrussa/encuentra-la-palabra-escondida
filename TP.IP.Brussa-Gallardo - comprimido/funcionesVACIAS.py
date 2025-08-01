from principal import *
from configuracion import *
import random
import math

#esta funcion toma como parametro una lista y devuelve una palabra al azar de la lista creada por la funcion lectura.

def nuevaPalabra(lista):
    palabra_al_azar=random.choice(lista)
    palabra=palabra_al_azar.lower()# convierto la palabra a minuscula para evitar errores
    return palabra

#esta funcion lee el archivo de texto y en salida guarda todas las palabras con la longitud del tercer parametro.

def lectura(archivo, salida, largo):
    palabras = archivo.readlines();
    for palabra in palabras:
        if (len(palabra)-1)==largo:
            salida.append(palabra[:-1])

#esta funcion toma como parametros una palabra elegida al azar en la función nuevaPalabra y una palabra ingresada por el usuario, luego compara ambas y guarda
#los caracteres correctas incorrectas y parcialmente correctas, luego retorna True si la palabra es correcta, False si no lo es.

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
            if palabraCorrecta==palabra:
                return True
            else:
                for i in range(len(palabra)):
                    if palabra[i]==palabraCorrecta[i]:
                        correctas.append(palabra[i])
                    elif palabra[i]not in palabraCorrecta:
                        incorrectas.append(palabra[i])
                    elif palabra[i] in palabraCorrecta and palabra[i]!=palabraCorrecta[i]:
                        casi.append(palabra[i])
                return False