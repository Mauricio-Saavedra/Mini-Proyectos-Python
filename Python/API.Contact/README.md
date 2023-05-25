# Práctica API REST

## Descripción

Creo una aplicación pequeña solo para ver el funcionamiento de una `API REST`, pues es una de las cosas que más se ocupa en el entorno laboral de la informatica y la programación por su fácilidad para transmitir información y escalabilidad.
En ésta aplicación juego con lo creado y `Thunder Client` en `VSCode`.
Uso las peticiones **GET**, **POST**, **PUT**, **PATCH** y **DELTE**.
Se recopilan tres datos del cliente: _name_, _email_, _phone_, ys e guardan en una **DB** para su almacenamiento y posterior consulta, la DB estará hecha con `SQLite`.

## Instrucciones de instalación

- Para hacer uso de ésta se debe descargar y ejecutar desde tu terminal con el comando:
- Para ello debes de tener lso paquetes que se encuentran especificados en `requirements.txt`

```Python3
py app.py
```

- Una vez que la aplicación se esta ejecutando se podría decir que el servidor está activo, ahora podemos hacerle peticiones con `Thunder Client` o con `Postman`.

## Ejemplos de uso

- Todas las peticiones que se hagan tienen que ser en formato `JSON`, éste formato funciona como los diccionarios de Python {k:v, k:v}, dónde k == Key y v == Value.
    -Por ejemplo, desde el apartado **Body** de `Thunder Client` vamos a ponerle el _metodo_ **POST** en el local:host/contacts y escribimos:

    ```JSON
    {
        "name" : "Mauricio",
        "email" : "correo@prueba.com",
        "phone" : "55-5555-5555"
    }
    ```

    -Y debajo nos arrojará:

    ```JSON
    {
        "contact": {
        "email": "correo@prueba.com",
        "id": 5,
        "name": "Mauricio",
        "phone": "55-5555-5555"
    },
      "message": "contacto creado con éxito"
    }
    ```

- Si queremos que nos muestre los contactos que tiene registrados ponemos en `Thunder Client` el _metodo_ **GET** y le damos _Send_.
- Si sólo queremos un contacto debemos de poner `/contacts/id`, dónde el id será el que tiene registrado en la **DB** el dato que queremos mostrar en pantalla.
- Si nuestra intención es _editar_ un registro debemos de copiar el JSON con todo y ID y pegarlo en el body, posteriormente hacemos los cambios requeridos y usando el metodo **PUT** le damos _Send_.
- Si nuestra intención es borrar un registro podemos `/contacts/id`, usamos el _metodo_ **DELETE** y le damos en _Send_.
    -Si damos otro **GET** veremos que ya no se encuentra e dato que buscabamos.

## Estado del proyecto

Ésta práctica esta finalizada, pues era solo para familiarizarme con lo que son las API's y también el perderle el miedo a los JSON, que estan en todas partes y a veces se ven descomunales, pero que realmente tienen una estructura bien definida.
