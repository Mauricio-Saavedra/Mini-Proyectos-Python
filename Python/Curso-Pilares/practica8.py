# PRÁCTICA 8 | Alexis Mauricio Saavedra Bueno | Folio: 914NL003.
# 8.1 Ejercicio 1 (2 puntos):
# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde
# el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.
"""
num = int(input('Favor de ingresar un número: '))
num += 1
numCruadrado = {}
for i in range(1, num):
    if num > 0:
        numCruadrado[i] = i*i
print(f'Aquí tienes los números y sus cuadrados:\n {numCruadrado}')
"""
# 8.2 Ejercicio 2 (2 puntos):
# Escribe un programa que lea una cadena y devuelva un diccionario donde las llaves seràn los caracteres y
# los valores de dichas llaves serà el número de veces que aparece el carácter en la cadena.
"""
#Declaro dos variables, una para el input y otra para hacer ese input puras minusculas y tener compatibilidad.
cadena = input('Ingresa una palabra: ')
cadena2 = cadena.lower()
contador = {}.fromkeys(cadena2, 0)  #.fromkeys(llave:valor) me permite asignar una lave y un valor especifico.
for i in cadena2:           #Hago que FOR  recorra la cadena en minusculas.
    if i in contador:       #SI el valor de "i" esta en contador{cadena2: 0} Entonces...
        contador[i] += 1    #La llave de Contador[i] será el valor de "i", y a su valor se le suma uno por cada vez que se encuentre.
print(contador)
"""
# 8.3 Ejercicio 3 (2 puntos):
# Vamos a crear un programa en python donde:
# 1.- Vamos a declarar un diccionario para guardar los precios de las distintas frutas.
# 2.- El programa pedirá el nombre de la fruta, la cantidad que se ha vendido y
# 3.- nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario.
# diccionario = {fruta: 'precio'}
# 4.- Si la fruta no existe nos dará un error.
# 5.- Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

listaFrutas = ['Aguacate','Albaricoque','Arándano azul','Arándano rojo','Anona roja','Almendra','Alquejenje','Avellana','Aceituna','Anona','Árbol de pan','Araza','Acerola','Badeas','Breja','Berenjena','Babiaco','Banana','Bergamota','Bala de cañón','Ciruela','Coco','Caqui','Castaña','Chirimolla','Corozo','Caimito','Cidra','Cacao','Copoazu','Durazno','Dátil','Dragonfly','Durian','Damasco','Escaramujo','Fresa','Frambuesa','Frutipan','Fruta de la pasión','Guanábana','Guayaba','Granada','Grosella','Grosella espinosa','Gayuba','Higos','Hesiteria','Ícacos','Ibo','Ilama','Jobo','Jalapeño','Jinicuil','Jono','Jabuticaba','Kiwi','Kino','Kaki','Kumkuat','Kiwano Melon','Limón','Lulo','Lima','Lichi','Melón','Mandarina','Manzana','Mango','Maní','Maracuyá','Mamón','Membrillo','Mora','Madroño','Naranja','Níspero','Noni','Nectarina','Nuez','Nance','Oroblanco','Pera','Papaya','Piña','Pomelo','Pitaya','Pistacho','Pimiento','Plátano','Quingombó','Quinoto','Quince','Queule','Quandong','Remolacha','Rabadilla','Rambután','Ruibarbo','Rocoto','Reina Claudia','Saúco','Sandía','Saguaro','Saputá','Sorveira','Tamarindo','Tomate','Toronja','Tuna','Tangelo','Tupinambo','Uva','Uchuva','Vainilla','Vitoria','Veludo','Xoconostle','Xocota','Ximenia','Xigua','Xylocarp','Zapote','Zarzamora','Zapayo']
salida = 125
frutasPrecio = {}
saber = int(input('Estás a punto de ingresar los precios de las frutas, si conoces las frutas que quieres ingresar, preciona 0.\nSi no sabes cuales frutas hay y quieres saber el listado, preciona 1.'))
if saber == 1:
    print(listaFrutas)
else:
    pass
while salida != 0:
    fruta = input('Ingresa el nombre de la fruta a registrar: ').capitalize()
    if fruta in listaFrutas:
        precio = int(input('Ingresa el costo de la fruta por kilo: '))
        frutasPrecio[fruta] = precio
    else:
        print('Fruta inexistente.')
        pass
    opcion = int(input('Preciona 1 para añadir más frutas, preciona 0 para salir: '))
    if opcion == 1:
        salida -=1
    else:
        salida = 0
print(frutasPrecio)
