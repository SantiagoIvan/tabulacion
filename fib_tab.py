def fib_tab(n):
    subproblems_array = [0 for i in range(n + 1)]
    # asi tengo los resultados de todos los subproblemas, desde el 0 hasta el n

    for i in range(n + 1):
        if i == 0:
            continue
        if i == 1:
            subproblems_array[i] = 1
            continue
        subproblems_array[i] = subproblems_array[i - 1] + subproblems_array[i - 2]
    return subproblems_array[-1]


print(fib_tab(8))
