# ¿Cómo resolver el problema del ahorcado?

### Se Necesita:
- Una variable con muchas palabras para tomar al azar.
    - Esta variable esta convertida a una lista con **.split()**, pues solo copie varias listas de palabras de internet y con el metodo le dí forma.
        - De igual manera, si quieres agregar más palabras solo añadelas a la variable con un espacio de por medio.

- Una lista vacía donde pondremos las letras ya utilizadas y erradas que ha ingresado el usuario, esto nos servirá para cuidar de los intentos del usuario a la vez que nos ayuda a saber que pocision de la horca va a imprimirse por consola.

- Una función que:
    - Si le ingresas una lista (tomada de la variable con muchas palabras) te devuelve una palabra tomada de la lista...
    - ...para que cada uno de sus elementos se seleccione de manera adecuada uso **Secrets**, pues puede hacer selección aleatoria de strings y no solo de intergers como lo haría random.
    - Posteriormente toma la longitud de esa lista y convierte los caracteres en guiones con un cliclo FOR.
    - La función guarda de manera **global** dos variables: Una donde la palabra esta en sí y otra donde esta fragmentada en una lista.
    - Y devuelve finalmente la lista de guiones.

- Un sistema en el cuál se ingresa una letra y verifica que solo se ingrese una letra, todo esta dentró de un bucle **while True**:
    - Primero verifica que la longitud del **input** sea de uno, si es más extenso te pide que ingreses un solo caracter, este paso ya tiene el metodo **.lower()** para que todo sea uniforme en minusculas.
    - Si el caracter ingresado ya se ha ingresado antes, te dice que ese ya ha sido utilizado, pues así no comprometes un intento del jugador por algún error de dedo o descuido.
    - También verifico que este **in** 'qwertyuiopasdfghjklñzxcvbnm', para evitar que el usuario ponga un número y que con ello pierda un turno.

- Una la función que imprime la horca según el número de su intento y le muestra sus errores al usuario:
    - Esto lo hace ingresando a la llave según el indice de la longitud de las letras usadas y erradas.

- Cambiar los guiones por las letras reales:
    - Esto lo hice con un ciclo for que recorra la longitud de una lista y cuando haya una coincidencia, ocupe ese indice para hacer el cambio.
