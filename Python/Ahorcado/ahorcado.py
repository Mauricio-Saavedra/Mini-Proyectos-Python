#GitHub.com/Mauricio-Saavedra
#GithubPages.

import secrets
from complementos import *

#Empiezo por la lista de palabras
erradas = []     #Una lista que guarde las letras INcorrectas
correctas = []

#Creo una funcion para tomar una palabra de la lista al azar, tenerla en una variable, la misma en guiones y la misma en lista.
def transform (x:list):
    global palabraVar, palabraLista         #Variables Glovales que ocuparé.
    palabraVar = secrets.choice(palabras)   #Acá guardo la palabra EN SÍ.
    palabraLista = list(palabraVar)         #Acá la palabra hecha lista.
    palabraGuiones = []                     #Una lista con la longitud de la palabra en guiones.
    #caracteres por guiones:
    for i in palabraVar:            #Ciclor for para sacar los guiones.
        z = '_'
        palabraGuiones.append(z)
    return palabraGuiones

#Hago una introduccion al juego, guardo la palabra en una variable y se la muestro al usuario.
print('Bienvenido al juego del ahorcado, tendras siete intentos para descubrir la palabra antes de morir, suerte!')
palabraSecreta = transform(palabras)    #Acá ya estan generadas la palabra secreta con sus tres variables.
print(f'La palabra secreta es:\n{palabraSecreta}')

#Acá va la entrada de datos por parte del usuario en un bucle:
def respuesta(erradas):      #A la función le vamos a dar la variable de la lista vacía "erradas" para almacenar las letras en las cuales ya ha errado el usuario.
    while True:
        respuesta = input('Ingresa tu letra: ').lower()
        if len(respuesta) != 1:
            print('Por favor introduce Solo una letra.')
        elif respuesta in erradas:
            print('ya has intentado con esta letra')
        elif respuesta not in 'qwertyuiopasdfghjklñzxcvbnm':
            print('Por favor ingresa un caracter tipo letra')
        else:
            return respuesta  #La función va a retornar una letra filtrada por esta función, pues siempre será una letra valida, en minusculas y que no haya usado previamente.

#Creo una función para que muestre al ahorcado conforme se va qeuivicando el usuario y le muestro las palabras erradas.
def horcaInteligente(horca:dict, erradas:list):
    print(horca[len(erradas)])
    print(f'Las letras que ya has intentado son:\n{erradas}')

#Ahora si empieza el juego dentro de un bucle para que este dentro hasta que gane o pierda
while True:
    letra = respuesta(erradas)
    if len(correctas) != len(palabraLista):     #->SI la longitud lista de letras correctas es diferente a la longitud de la lista de la palabra escogida:
        if letra not in palabraVar:     #Si le letra no esta en la palabra escogida:
            erradas.append(letra)            #Se añade a la lista de erradas.
            print(f'Respuesta erronea {horcaInteligente(horca, erradas)}') #Y se imprime que falló, junto con su correspondiente parte de lal horca.
        else:                                   #Si no es el caso y la letra SI  esta dentro de la palabra:
            for i in range(len(palabraLista)):      #"i" recorrera la longitud de la lista que contiene a la palabra.
                if letra == palabraLista[i]:            #Si la letra coincide con el indice de una letra de la lista:
                    palabraSecreta[i] = letra               #Se cambiara el valor que haya en ese indice por la letra.
                    correctas.append(letra)                 #Se añade la letra a la lista de las palabras correctas.
    if len(correctas) == len(palabraLista):     #->SI la longitud de las lista-correctas es igual a la longitud de la lista-palabra  
        print(f'¡Ganaste! La palabra secreta era:\n{palabraVar}') #Entonces el usuario a ganado y se le imprime la palabra completa.
        break                                                     #Le damos un break para salir del ciclo y que acabe el código
    if len(erradas) >= 7:                        #->SI la longitud de las erradas es igual o mayor a siete significa que se ham impreso todas las horcas y qeu ha perdido.
        print(f'La palabra Secreta era: {palabraVar}')
        break

    print(palabraSecreta)
