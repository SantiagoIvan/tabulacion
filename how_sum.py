def how_sum(target_sum, array):
    # en cada indice del array guardaria varios arrays, dependiendo de la cantidad de aristas que le lleguen
    subproblems_array = [None for i in range(target_sum + 1)]
    subproblems_array[
        0
    ] = (
        []
    )  # mi posicion inicial, para un target sum de 0, retorno un array vacio , ya que de esa forma es posible generarlo

    for i in range(target_sum + 1):
        if subproblems_array[i] == None:
            continue
        for elem in array:
            if i + elem > target_sum:
                continue
            # al elemento i+elem puedo llegar desde i
            # Entonces le copio todos los elementos de i al indice i + elem, y le añado elem
            subproblems_array[i + elem] = subproblems_array[i] + [elem]
    if not subproblems_array[-1]:
        return "There is no possible combination"
    return subproblems_array[-1]


# en cada indice donde tenga un array inicializado, es porque es posible llegar hasta alli
# sumando los elementos de su array

print(how_sum(5, [3, 4]))  # False
print(how_sum(7, [3, 2]))  # True
print(how_sum(7, [5, 3, 2]))  # True
print(how_sum(7, [2, 4]))  # False
print(how_sum(300, [7, 14]))  # False
print(how_sum(140, [7, 14]))  # True
