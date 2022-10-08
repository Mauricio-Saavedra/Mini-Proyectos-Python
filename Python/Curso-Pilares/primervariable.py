a = 100
print(a)
#Este es un comentario.
#input es una función para que se ingresen datos del teclado.
nombre = input("Como te llamas?")
print("Usuario " + nombre)
#Lo que estoy haciendo es pedir que la consola imprima la String Usuario y concatenarle el resultado de la variable nombre.
print("Usuario",nombre)
#La concatenación también piede hacerse con una coma ,: print("Usuario " ,nombre) 
print("Usuario {}" .format(nombre))
#Format agrega a una string el valor de una variable
print(f"Usuario {nombre}")
#la primera f es una abreviación de format, estas usando Format pero de una manera diferente.