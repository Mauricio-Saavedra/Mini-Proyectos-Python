#CICLO WHILE:
#haz un programa en el cual ingresemos un número y que sume los números anteriones:
#Primero vamos a declarar tres variables:
    #n: Número, Para que el usuario ingrese un Número.
    #c: Contenedor, Aquí guardaremos la Suma que tendra M condigo misma.
    #m: Menores, Para recorrer los números menores al número ingresado
"""
n = int(input("Favor de ingresar un número: "))
c = 0 #
m = 0 #M ira avanzando desde el 1 hasta el número seleccionado.
while m < n: #MIENTRAS M sea menor a N este bloque hará:
    c += m   #C guardará la SUMA que menores tiene consigo misma, o sea que será un contenedor.*
    m += 1   #M tiene por valor inicial 0, por ello le sumaremos 1 hasta que llegué a cumplir la condición WHILE.
    print(f"Contenedor vale:{c}, + MenorqueN que vale:{m}, es igual al:\n")
print(f"La suma de {n} es {c}")
"""
#*Recuerda que si una variable vae 1 y se suma a si misma puede atascarse en 1, en lugar de Avanzar, por eso necesitamos un contenedor.

#Dado un rango de números enteros, obtener la cantidad de números enteros que contiene.
"""
pr = int(input("Favor de ingresar el 1er número: "))
sg = int(input("Favor de ingresar el 2do número: "))
cn = pr + 1
rs = 0
while cn < sg:
    rs += 1
    cn += 1
    print(f"pr={pr} sg={sg} cn={cn} rs={rs}")
print(f"La diferencia de números es: {rs}")
"""
#La solución a esto es bastante curiosa:
    #Declaramos 4 variables:
        #dos que pondrá el usuario (pr y sg)
            #Las dos son inputs.
        #Las dos que ocuparemos nosotros:
            #cn, que lo ocuparemos como contador.
            #rs, que lo ocuparemos como resultado.
    #Ahora, le diremos al programa que MIENTRAS nuestro contador sea menor que el segundo valor siga girando la rueda:
    #Contador es igual al primer valor + 1,
        #Pues la diferencia de números siempre va a tener menos 2 de valor, pues los números ocupan espacio.
    #Resultado es igual a cero, porque:
        #Lo que haremos será hacer que el loop siga girando hasta que se cumpla la condición, pero no vamos a mostrar el valor del contenedor, sino del resultado.
        #Pues él al ser quien cuenta las vueltas es quien sabe cuantos espacios entre un número y otro hay.

#Dado un rango de números enteros, obtener la cantidad de números pares que contiene.
"""
pr = int(input("Favor de ingresar el 1er número: "))
sg = int(input("Favor de ingresar el 2do número: "))
cn = pr + 1
rs = 0
while cn < sg:
    if cn % 2 == 0:
        rs += 1
    cn += 1
    print(f"cn={cn} rs={rs}")
print(f"Los números pares que hay entre estos dos números son: {rs}")
"""
#El funcionamiento es casí igual que en el anterior ejercicio, lo que cambia es:
    #Dentro del WHILE le ponemos una condicional, y le decimos:
        #Ejecuta MIENTRAS el contador sea menor al segundo valor.
            #  SI el modulo2 de contador es igual a cero, entonces:
                #le sumas uno al RESULTADO
        #Ejecuta contador + 1
    #Entonces antes de que se sume 1 al contador revisa si el número que contiene es igual a cero:
        #Si lo es, le suma uno.
        #Si no lo es, no le suma.
    #Le suma 1 al contador y vuelve a ejecutarse.

#Obtener la cantidad de los primeros números múltiplos de 5.
"""
n = int(input("Favor de ingresar tú número: "))
cn = 0
rs = 0
while cn < n:
    if cn % 5 == 0:
        rs += 1
    cn += 1
    print(f"cn={cn} rs={rs}")
print(f"Los números multiplos de 5 que hay entre estos dos números son: {rs}")
"""
#Es casi igual que el primero, pero con una variable menos.

#Dado un número, determina cuantos digitos tiene, yo lo hice así:
"""
n = input("Favor de ingresar tú número: ")
print(f"La cantidad de digitos que tiene tu número es: {len(n)}")

#El profesor lo hizo así:
# Variables | Ingresar Datos.
numero = int(input('Número: '))
i = 0
contador = 0
# Solución
while numero > 0:
    numero = numero // 10
    contador += 1
    print(f"número={numero} i={i} contador={contador}")
# Mostrar Datos
print(f'Cantidad de dígitos: {contador}')

#lo que hace el profesor es que:
    #MIENTRAS la variable número sea mayor que cero se ejecutará lo siguiente:
        #numero será igual al cociente (en entero) número entre 10.
        #Una vez eso, al contador se le suma 1.
        #Vuelve a dividirse hasta que sea menor a cero y con ello el contador se detenga.
        #Con las divisiones entre 10 se le va quitando un digito al número, por ello el contador registra eso.
"""
#Dado un número, determinar  la cantidad de dígitos pares que contiene.
"""La verdad me siento bien de como realice este ejercicio, por el como indagué para saber su funcionamiento.
n = int(input("Favor de ingresar tú número: "))
c = 0 #contador
d = 0 #digito
while n > 0:
    d = n % 10
    if d % 2 == 0:
        c += 1
    print(f"--Antes de n//= 10: n{n}, c{c}, d{d}")
    n //= 10
    print(f"Después de n//= 10: n{n}, c{c}, d{d}")
print(f"Cantidad de dígitos pares: {c}")
#MIENTRAS que NUMERO sea mayor a cero ejecutaras:
    #DIGITO será igual al modulo10 de NUMERO (Esto se hace para sustraer el último dígito)
    # Si el modulo2 de la variable DIGITO es igual a 0...
        #Entonces harás que a CONTADOR se le sume 1.
    # DESPUÉS a NUMERO se les sustaerá el último digito para ser evaluado.
"""
#La temible serie de fibonacci:
a, b = 0, 1   #Empezamos definiendo dos variables juntas.
while a < 10: #Mientras a sea menos a diez:
    print(a)      #Primero imprimirás a para el registro.
    a, b = b, a+b #Después a = b y b = a+b Para poder dezplazar los valores.

#Creo que con esto podría dejar al usuario dejar que la suma corra más número dejandole seleccionar el valor de 10, y dejando las variables en una sola línea:
a, b, c = 0, 1, int(input("Favor de poner un número que detenga la serie: "))
while a < c:
    print(a)
    a, b = b, a+b