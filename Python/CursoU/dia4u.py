#Ciclo FOR

datos = ['Alex', 'Mau', 27, 1.67, True] #Lista de datos variados
for dato in datos:
	print(dato)
#Este FOR va a sacar los datos de uno en uno imprimiendolos.

#Veamos como se haría esto mismo con WHILE:
c = 0
while c < len(datos): #El proceso cambia mucho, pues mientras el FOR hace las cosas directamente, WHILE dice que mientas C sea menor que len(datos), o sea la longitud de la lista Datos se seguirá ejecutando.
	print(datos[c]) #PRINT tiene la instrucción de ir imprimiendo un dato relacionado con el valor de C, en este primer caso es 0, lo cual índica que tiene el primer lugar de la lista.
	c += 1          #Se le va a sumar 1 a C para que tenga un nuevo valor y tome otro valor de la lista.
#Y se irá repitiendo hasta que acabé tu trabajo.

"""
#Función Range:
n = range(10)  #Lo que imprimira:
print(n)       #range(0, 10)
print(type(n)) #<class 'range'>
#Podemos ver que Range es un tipo de dato y que dentro de sí contiene el rango, más no todos los números.
#Pero si le añadimos la sentencia FOR e IN para decirle al FOR que recorrera el rango 10 veces empezando por el cero.
for i in range(10):
    print(i)
"""
#El valor final dado nunca es parte de la secuencia; range(10) genera 10 valores, los índices correspondientes para los ítems de una secuencia de longitud 10.
#RANGE siempre empieza en cero, a menos que lo especifiques: range(10, 20)
#Es posible hacer que el rango empiece con otro número, o especificar un incremento diferente (incluso negativo; algunas veces se lo llama “paso”):

#Ejercicio 1:Obtener la suma de pares e impares de los primeros N números enteros positivos.
#Para la solución de este problema, se requiere que el usuario ingrese un número, luego el sistema devuelve la suma de pares e impares.
#Primero vamos a ingresar las variables:
"""
n = int(input("Ingresa el número a dividir y sumar: "))
n += 1 #Se le suma uno al rango para que tmabién abarque el número dado por el usuario.
par, impar = 0, 0 #Las variables que contendran los resultados.
#Ciclo FOR:
for var_for in range(1, n): #cuando usas for, puedes declarar una variable interna, en este casó: var_for. Esta variable tomará el primer valor del rango, como aquí esta definido su valor es: 1. Si no lo estuviese, su valor sería: 0.
    if var_for % 2 == 0:        #Si el modulo2 de var_for es igual a cero... 
        par = par + var_for     #...el valor de par sería el de par + el número que esta en curso dentro de var_for.
    else:                       #SINO entonces...
        impar = impar + var_for #...el valor de impar será la suma de impar más el número que contenga la variable var_for en curso.
    print(f"Variable inetrna de for:{var_for} | par:{par} |impar:{impar}")
#Ahora los Resultados:
print(f"Suma de pares: {par}")
print(f"Suma de impares: {impar}")
"""
#Ejercicio 2:Crear el algoritmo que indique  si un número es perfecto  o no,
    # se dice que un número es perfecto si la suma de sus divisores es igual al número,
    # por ejemplo: 6 tiene como divisores 1, 2 y 3,
    # entonces 1 + 2 + 3 = 6 el número 6 es perfecto.
    # Si el número es 9 tiene como divisores 1, 3,
    # entonces 1 + 3 = 4 no es perfecto.
"""
#Empezamos por declarar cuatro variables:
n = int(input("Ingresa tú número para saber si es perfecto: "))
modulo = 0      #Acá vamos a almacenar el resultado del modulo.
resp = ""  #Acá va el string de la respuesta.
suma = 0        #Aquí la suma almacenada de los números que su MODULO sea igual a cero, o sea los números que si pasan.
#Cliclo FOR el Número de vuelta(n_vuelta) pasará por el rango (1 al número usado por el usuario).
for nVar in range(1, n):
    modulo = n % nVar   #El MODULO(nVar) de N se guardará en la variable modulo.
    if modulo == 0:     #Si el resultado de ese modulo es igual a cero entonces...
        suma += nVar    #...se sumará el número en curso de nVar a la variable SUMA.
    print(f"Número de vuelta:{nVar} | n:{n} | modulo:{modulo} | suma:{suma}")

if n == suma:       #Si el número ingresado por el usuario es igual a lo que este dentro de la variable SUMA.
    resp = "Perfecto"   #se pone dentro de la variable RESP que el número es perfecto.
else:               #SINO...
    resp = "Imperfecto" #...Pones imperfecto.
# Resultado:
print(f"El número {n} es: {resp}")
"""

#Ejercicio 3: Dado 2 números diga si son amigos o no, recuerde que dos números son amigos si la suma de sus divisores de uno de ellos es igual al otro y viceversa, por ejemplo 220 y 284 son amigos.
    # Divisores de 220 son: 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
    # Divisores de 284 son: 1 + 2 + 4 + 71 + 142 = 220
#Se declaran seis variables: 2 para datos del usuario. 2 Para resultados. 2 Dos contenedores y una respuesta:
"""
var1 = int(input('Ingresa tu 1er número: '))
var2 = int(input('Ingresa tu 2do número: '))
resultado1 = 0
resultado2 = 0
output = ''
contenedor1 = 0
contenedor2 = 0

#Haremos que la variable NUM1 recorra de 1 hasta el primer número del usuario.
for num1 in range(1, var1):
    resultado1 = var1 % num1 #Guardando en RESULTADO1 el moduloNUM1 de VAR1

    if resultado1 == 0:      #SI ese RESULTADO1 es igual a Cero.
        contenedor1 += num1  #CONTENEDOR se le sumará su valor más el de NUM1

for num2 in range(1, var2):  #Se repite el proceso de arriba con el segundo número
    resultado2 = var2 % num2

    if resultado2 == 0:
        contenedor2 += num2
#Acá vamos a comparar los números entre si; SI VAR1 es igual a CONTENEDOR2 & VAR2 es igual a CONTENERDOR1, entonces...
if (var1 == contenedor2 and var2 == contenedor1):
    output = 'Son amigos' #Los números son amigos
else:                                 #Sino, pues no.
    output = 'NO son amigos'

#Imprime el resultado
print(f"Los números {var1} y {var2}: {output}")
"""
#Ejercicio 4: Dado un rango de numérico entero num. inicial y num. fina, obtener la cantidad de números positivos y negativos que existen en el rango.
    #Primero voy a declarar 4 varibales, dos para pedir números, uno para contar los números positivos y otra para los negativos.
"""
ni = int(input("Favor de ingresar el número inicial: "))
nf = int(input("Favor de ingresar el número final: "))
contadorMas = 0
contadorMenos = 0
    #En este ciclo estoy declarando que "i" recorrera el rango que haya entre el primer y el segundo número:
for i in range(ni, nf):
    #SI "NI" es menor a cero & la variable "i" también es menor a 0, entonces a CONTADORMENOS se le suma 1. 
    if ni < 0 and i < 0:
        contadorMenos += 1
    #ELIF la variable "i" es mayor o igual a cero entonces a CONTADORMAS se le suma 1.
    elif i >= 0:
        contadorMas += 1

print(f"Entre {ni} y {nf} hay: {contadorMas} positivos y {contadorMenos} negativos")
"""
#Ejercicio 5: Hallar cuantos múltiplos de M hay en un rango de números enteros.
    # ANÁLISIS: Para la solución de este problema, se requiere que el usuario ingrese tres números (NumInicial, NumFinal y NumMúltiplo).
        # luego el sistema devuelve la cantidad de múltiplos que hay en el rango.
#Si no estoy leyendo mal es que el usuario debe definir un rango, y elegir un número del cual se le buscarán sus multiplos dentro de dicho rango.
#Entonces empezaré por definir 4 variables: dos para el rango, una para buscar el multiplo y un contador para que guarde cuantos hay y que los muestre al usuario.
"""
ni = int(input("Favor de ingresar el número inicial: "))
nf = int(input("Favor de ingresar el número final: "))
nm = int(input("¿A cual le buscamos sus multiplos?: "))
contador = 0
#La variable "i" recorrera de NI a NF.
for i in range(ni, nf):
    #Si el modulo"i" de NM es igual a cero, se le suma 1 al contador. 
    if i % nm == 0:
        contador +=1

print(f"Los multiplos de {nm} que hay entre {ni} y {nf} son: {contador}")
"""