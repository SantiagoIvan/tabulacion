# de todas las posibles formas de llegar a un lugar, retorna la mejor
# Para ello puedo cortar ni bien lleno el bloque 7. Si se llena en las primeras iteraciones,
# quiere decir que esa es la forma mas rapida de llegar
def best_sum(target_sum, array):
    subproblems_array = [None for i in range(target_sum + 1)]
    subproblems_array[0] = []

    for i in range(target_sum + 1):
        if subproblems_array[i] == None:
            continue
        for n in array:
            if i + n > target_sum:
                continue
            # antes de pisarlo, pregunto si la combinacion que voy a meter es mas corta que la que esta
            new_comb = [n] + subproblems_array[i]
            if subproblems_array[i + n] == None or len(subproblems_array[i + n]) > len(
                new_comb
            ):
                subproblems_array[i + n] = new_comb
        if subproblems_array[-1]:
            return subproblems_array[-1]

    return subproblems_array[-1]


print(best_sum(5, [3, 4]))  # False
print(best_sum(7, [3, 2, 1]))  # True
print(best_sum(7, [5, 3, 2, 1]))  # True
print(best_sum(7, [2, 4]))  # False
print(best_sum(300, [7, 14]))  # False
print(best_sum(140, [7, 14]))  # True
