# Todas las formas posibles


def all_construct(target_word, array):
    subproblems_array = [[] for i in range(len(target_word) + 1)]
    subproblems_array[0] = [
        []
    ]  # Una sola combinacion, la combinacion nula. Los demas no tienen por el momento combinaciones posibles

    for i in range(len(target_word) + 1):
        if not subproblems_array[i]:
            continue

        for word in array:
            if target_word[i:].startswith(word):
                # agrego en el destino todas las combinaciones de i-index con la nueva palabra concatenada
                # sin pisar los valores que ya haya alli
                for comb in subproblems_array[i]:
                    subproblems_array[i + len(word)].append(comb + [word])

    return subproblems_array[-1]


print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))  # 3 formas
# "ab", "cd", "ef" ; "abc","def" ; "abcd", "ef"
print(all_construct("abcdeef", ["ab", "abc", "cd", "def", "abcd"]))  # []
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # []
print(
    all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar", "a"])
)  # True, [sk,ate,bo,a,rd]
print(
    all_construct("purple", ["purp", "p", "ur", "le", "purpl"])
)  # 2 formas, [purp,le],[p,ur,p,le]
# print(
#     can_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"],
#     )
# )  # False por su crecimiento exponencial no termina mas
# print(
#     all_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "f"],
#     )
# )  # Miles de formas, no termina mas
