def grid_traveller(x, y):  # x, y dimensiones, por ejemplo 3x3
    # La idea de tabulacion es crear un array del size del input
    # en este caso vendria bien una tabla 2x2
    # cuantas veces se llego a destino? tendre que fijarme cuantas veces llegue al (0,0) en mi array

    subproblems_array = [[0 for i in range(x)] for j in range(y)]
    # mi caso base, si estoy en el origen, solo hay una forma de llegar hasta alli
    subproblems_array[0][0] = 1
    for i in range(x):
        for j in range(y):
            # sumo el contenido en la actual posicion a mis vecinos de abajo y a la derecha.
            # Voy sumando de a 1, de esa forma, si en un casillero hay un valor superior a 1,
            # significa que hay distintas formas de llegar a el
            if (i + 1) < x:
                subproblems_array[i + 1][j] += subproblems_array[i][j]
            if (j + 1) < x:
                subproblems_array[i][j + 1] += subproblems_array[i][j]
    return subproblems_array[-1][-1]


print(grid_traveller(30, 30))
