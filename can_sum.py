def can_sum(n, array):
    # yo se que el branch factor seria m, siendo m la cantidad de elementos
    # del array. Sin embargo, este numero sera constante, no sera modificado en el tiempo
    # Lo que si va a modifcarse es la suma
    # Yo se que tengo que llegar a 7, puedo tener 0,1,2,3..., hasta 7 como acumulado.
    # Entonces creo un array hasta el indice 7, cosa de incluir al 0 y al 7.

    subproblems_array = [False for i in range(n + 1)]

    # Itero sobre el array, viendo si hay una forma de llegar al casillero 7.
    # Cada indice del array representa el acumulado hasta ese momento.
    # Desde un casillero me puedo mover a otro, sumando algun elemento del array,
    # Por lo tanto, un casillero se tornara a True si es posible llegar al mismo desde cualquier lugar
    # Si yo estoy en la posicion n-esima, y sumo un elemento del array k
    # Entonces la posicion n-esima se conecta con la posicion n+k. Como es posible llegar hasta esa posicion
    # Se pone True.
    # Es como que de un casillero voy sacando  aristas hacia otros casilleros, formando un digrafo.

    # Como el principio acumulado es 0, ese casillero lo pongo True
    subproblems_array[0] = True
    for i in range(n + 1):
        if not subproblems_array[i]:
            continue
        for elem in array:
            if i + elem <= n:  # si no me paso del limite
                subproblems_array[i + elem] = True
    return subproblems_array[-1]


print(can_sum(5, [3, 4]))  # False
print(can_sum(7, [3, 2]))  # True
print(can_sum(7, [2, 4]))  # False
print(can_sum(300, [7, 14]))  # False
