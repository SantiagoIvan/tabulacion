# Mismo problema, pero retorna cuantas combinaciones dan el target_sum
def count_sum(n, array):
    subproblems_array = [0 for i in range(n + 1)]
    subproblems_array[0] = 1
    # Sumo un 1 donde es posible llegar
    for i in range(n + 1):
        if not subproblems_array[i]:
            continue
        for elem in array:
            if i + elem <= n:  # si no me paso del limite
                subproblems_array[i + elem] += subproblems_array[i]
    return subproblems_array[-1]


print(count_sum(5, [3, 4]))  # 0
print(count_sum(7, [3, 2]))  # 3 : 2+2+3 ^ 3+2+2 ^ 2+3+2
print(count_sum(7, [2, 4]))  # 0
print(count_sum(300, [7, 14]))  # 0
