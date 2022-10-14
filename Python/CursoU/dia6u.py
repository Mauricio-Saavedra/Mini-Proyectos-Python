#Listas, Sets y Diccionarios:
#Ejercicio1:
#Ingrese 6 números en una lista y obtenga el número mayor y menor ingresado.
"""
num = []    #Empiezo declarando la lista.
con = 0     #Después delcaro un contador.
while con < 6:  #Mientras contador sea menor a 6, sigues en ciclo:
    var = int(input('Ingresa un número: ')) #Ingresas un valor.
    if var > -1:        #Si tu valor es mayor a -1...
        num.append(var) #A la lista NUM se le agregara el valor añadido.
        con += 1        #Contador suma uno para el ciclo.
    else:               #SINO...
        print('Intenta de nuevo.') #Intentalo de nuevo.
print(num)  #Imprimo los valores en forma de lista.
for i in num:   #Ciclo FOR en la cantidad de valores de NUM.
    ma = max(num)   #Sacamos el mayor
    me = min(num)   #Sacamos el menor
print(f'El número mayor es: {ma}\nEl número menor es: {me}')
"""
#Ingrese 12 número en 3 listas (en cada lista con 4 números), y obtenga la suma de cada lista.
"""
num1, num2, num3 = [], [], []    #Empiezo declarando la lista.
con = 0     #Después delcaro un contador.
while con < 4:  #Mientras contador sea menor a 6, sigues en ciclo:
    var = int(input('Ingresa un número: ')) #Ingresas un valor.
    if var > -1:        #Si tu valor es mayor a -1...
        num1.append(var) #A la lista NUM se le agregara el valor añadido.
        con += 1        #Contador suma uno para el ciclo.
    else:               #SINO...
        print('Intenta de nuevo.') #Intentalo de nuevo.
con = 0     #Reseteo el contador para repetir el ciclo con la segunda lista:
while con < 4: 
    var = int(input('Ingresa un número: '))
    if var > -1:        
        num2.append(var)
        con += 1 
    else:      
        print('Intenta de nuevo.') 
con = 0     #Reseteo el contador para repetir el ciclo con la tercer lista:
while con < 4: 
    var = int(input('Ingresa un número: '))
    if var > -1:        
        num3.append(var)
        con += 1 
    else:      
        print('Intenta de nuevo.') 
#Imprimo las listas para que el usuario las vea:
print(f"Lista1: {num1}, Lista2: {num2}, Lista3: {num3}")
#Declaro las funciones de suma junto con las variables para aguardar los resultados:
sum1, sum2, sum3 = sum(num1), sum(num2), sum(num3)
print(f"""#Suma1: {sum1}
# Sum2: {sum2}
# Suma3: {sum3}""")     <-RECUERDA DESCOMENTAR ESTOS.

#Ejercicio3:  Almacene en una lista de 6 números  y obtenga la cantidad de pares e impares.
"""
num = []    #Empiezo declarando la lista.
con = 0     #Después delcaro un contador.
par, impar = 0, 0     #Declaro las variables de pares e impares.
while con < 6:  #Mientras contador sea menor a 6, sigues en ciclo:
    var = int(input('Ingresa un número: ')) #Ingresas un valor.
    if var > -1:        #Si tu valor es mayor a -1...
        num.append(var) #A la lista NUM se le agregara el valor añadido.
        con += 1        #Contador suma uno para el ciclo.
    else:               #SINO...
        print('Intenta de nuevo.') #Intentalo de nuevo.
#FOR i en el rango de longitud de la lista NUM.
for i in range(len(num)):   #Lo que entiendo es que Len retorna el número de la poscision del item, más no el item en si.
    if num[i] % 2 == 0:     #Pero acá los esta leyendo de la manera correcta.
        par += 1
    else:
        impar += 1

print(f'La cantidad de pares son: {par}, impares: {impar}')
"""
# ++Tuplas():
# -Las tuplas son un tipo de dato iterativo estatico o inmutable.
# 	tupla = ()	#Así definimos una tupla.
# 	frutas = ('naranja','platano','guayaba')	#Así también se define una tupla.
# -Podemos ocupar las mismas funciones[0:9:2] que en las listas, la mayor diferencia radica en su inmutabilidad.
# -Si mandamos a imprimir una tupla en un elemento FOR veremos que los elementos se imprimen con un salto de línea "\n".
# 	-Si queremos que esto no sea así, debemos de hacerlo de la siguiente manera:
# 	print(fruta, end='')	#la función "end=" marca que el último caracter puede ser modificado, si entre las comillas ponemos ",", los items serán separados por una coma, si ponemos " " los items serán separados por un espacio.
# -Para cambiar los valores internos de una tupla, debemos de convertirla a lista, modificar la lista y después hacerla de nuevo una tupla:
# 	lista = list(tupla)
# 	lista[0] = "Nuevo"
# 	tupla = tuple(lista)
# -Las funciones .append() y demás no son validas en las tuplas, únicamente: del tupla | para eliminar la tupla.

#Ejercicio Tupla: vas a tener una tupla con una serie de valores, lo que debes de hacer es pasar los valores especificados a una lista:
"""
tupla = (9,6,4,6,44,5,63,2,46,845,67,3,232,454,34,1,1,2,4,6,8,8,9,76,3,2)
lista= []
for i in tupla:
    if i < 8:
        lista.append(i)
print(lista)
#Así es como podemos filtrar elementos de una tupla y pasarlos a una lista.
"""
# ++SET: Esta colección de datos:
# -No admite valores duplicados.
# -No mantiene el orden de los datos.
#     -Por ello no tienen indice los valores.
# -No es posible modificar sus elementos
#    -Pero si se pueden agregar o eliminar datos.
"""
#Sintaxis de SET:
setto = {'Marte', 'Jupiter', 'Venus'}
#Si mandamos a imprimir los elementos estos no conservaran su orden.
-Funciones validas:
	print(len(setto)) #Para saber la longitud de el set.
	print('Marte' in setto) #Para saber si dicho string eciste dentro del set.
	setto.add('tierra') #Para añadir un nuevo elemento al set.
	setto.remove('tierra') #Para eliminar un elemento.
	setto.discard('pluton') #Elimina un elemento, pero si el elemnto no existe dentro del SET, no marcará error, como si lo hace .remove()
	setto.clear() #Para vaciar el set de todos los elementos.
	del setto #Para eliminar la variable completa.
"""
#++Diccionarios| dict:
# -Es una colección de datos con llave:valor
# -No hay orden o indices.
"""
#Sintaxis:
diccionario = {
	'Llave':'Valor',
	'key':'Value',
	'POO':'Programación Orientada a Objetos'
}
print(diccionario)

# -Funciones validas con los diccionarios:
	print(len(diccionario))
	print(diccionario['POO']) #Para acceder a un elemento, se hace con su llave.
	print(diccionario.get('llave')) #También de esta manera se accede a un elemento.
	diccionario['key'] = 'new value of key'   #Para modificar un elemento.
"""
#Para recorrer los elementos de un diccionario lo hacemos con un ciclo for:
"""
for termino in diccionario:
	print(termino)
    #Acá termino hace alución a las llaves, si queremos acceder a los valores de esto se hace con una coma y la función .items() en el diccionario, como lo veremos abajo:
for termino, valor in diccionario.items():
	print(termino, valor)
    #Solo para recuperar las llaves.
for termino in diccionario.keys():
	print(termino)
    #Solo los valores:
for valor in diccionario.values():
	print(valor)

#Más funciones con los diccionarios:
	print('POO' in diccionario)         #Comprobar existencia de algún elemento, esto nos arrojará un booleano.
	diccioanrio['PK'] = 'Primary Key'   #Agredar un elemento
	diccionario.pop('PK')	#Remover un elemento a traves de su llave con pop.
	diccionario.clear()	    #Para limpiar la variable pero dejarla.
	del diccionario		    #Para borrar la variable por completo.
"""
