#BREACK & CONTINUE:
# La sentencia break, como en C, termina el bucle for o while más anidado.
# Las sentencias de bucle pueden tener una cláusula ELSE que es ejecutada cuando el bucle termina:
    # Después de agotar el iterable (con for)
    # Cuando la condición se hace falsa (con while)
    # Pero no cuando el bucle se termina con la sentencia break.
# Se puede ver el ejemplo en el siguiente bucle, que busca números primos:
"""
from cmath import pi


num1 = int(input("Ingresa el valor de inicio: "))
num2 = int(input("Ingresa el valor de final: "))
for n in range(num1, num2):
    for x in range(num1, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # El bucle falló sin encontrar un factor:
        print(n, 'is a prime number')
#Sí, este es el código correcto. Fíjate bien: ELSE pertenece al ciclo FOR, no al IF.
#Cuando se usa con un bucle, la cláusula ELSE tiene más en común con el ELSE de una sentencia TRY que con el de un IF: en una sentencia TRY la cláusula ELSE se ejecuta ->cuando no se genera ninguna excepción<-, y el ELSE de un bucle se ejecuta ->cuando no hay ningún break<-.
#La sentencia TRY es especifica para gestionar excepciones o código de limpieza para un grupo de sentencias.}
c = 3 + 5j
print(c)       #(3+5j)
print(type(c)) #<class 'complex'>
"""
"""
#Break: Tenemos un ciclo for compuesto por 'Holanda':
for i in 'Holanda':
	if i == 'a':
		print(f'Letra encontrada: {i}')
	else:
		print(f'{i}')
print('Inicia el otro FOR:')
#Si nosotros quisiesemos que el programa terminará tras la primer letra 'a', ínicament le pondríamos la palabra reservada [ brake ] después del primer print:
for i in 'Holanda':
	if i == 'a':
		print(f'Letra encontrada: {i}')
		break
	else:
		print(f'{i}')
#Esta palabra esta diseñada para romper el cilco for tras encontrar un elemento que nosotros nesitemos.
"""
"""
#+Continue: Vamos a imprimir los pares dentro de un rango:
for i in range(1, 15):
	if i % 2 == 0:
		print(f'Valor: {i}')
print('Ahora con continue:')#Ahora con continue:
for i in range(1, 15):
	if i % 2 != 0:  #SI "i" modulo de 2 es diferente a 0 [ != 0 ]. O sea un impar.
		continue    ##Por lo tanto si es un número impar entonces no queremos que continue el código de este cilco FOR, sino que se vaya a la siguiente iteración de este ciclo y ya no ejecute las siguientes líneas, para ello ocupamos CONTINUE.
	print(f'Valor: {i}')
#Acá estamos cambiando la lógica, pero llegamos al mismo resultado, puede parecer un poco más enrevesado, pero es solo para saber cuando ocuparemos CONTINUE como se usa e interactua con el código.
"""
#Aunque un excelente y sencillo ejemplo lo encontramos en la documentación de Python:
for num in range(2, 10):
    if num % 2 == 0:
        print("Número --par:", num)
        continue
    else:
        print("Número impar:", num)
#Haremos un recorrido de 8 veces:
    #SI el modulo de 2 == 0:
        #Imprimirás: Número --par:
        #CONTINUAS -> La sentencia ya esta cumplida, entonces deberia saltarse la siguiente y regresar a ciclo, pero como esta el CONTINUE, pasa a la siguiente sentencia SI O SI:
    #SINO:
        #Imprimorás: Número impar: