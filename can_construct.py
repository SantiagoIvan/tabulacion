# El enfoque que utilizaria seria similar al anterior
# Tendria un array de longitud target_word
# cada indice representa donde comienza cada letra, para saber donde estoy parado,
# y voy a necesitar un espacion extra para el ''


def can_construct(target_word, array):
    subproblems_array = [False for i in range(len(target_word) + 1)]
    # la posicion 0 se corresponde con la primer letra y siempre sera True, es mi semilla, mi punto de partida
    # todavia no consumi la a, pero es donde empiezo
    # cuando consumo todas las letras, termino en la ultima posicion, el string vacio

    subproblems_array[0] = True

    # Cuando empiezo, empiezo por la a, todavia no la consumi, pero es dodne estoy parado.
    # Leo la lista de palabras. Por cada una pregunto, si a partir de donde estoy parado, la palabra comienza con dicha palabra
    # Si es asi, significa que voy a poder avanzar m posiciones, siendo m la longitud de la palabra del array
    # Eso quiere decir que en la posicion i+m pondre True, porque todas las letras hasta ese momento (sin incluir a esa letra) las habre consumido
    for i in range(len(target_word) + 1):
        if not subproblems_array[i]:
            continue
        for word in array:
            if target_word[i:].startswith(word):
                subproblems_array[i + len(word)] = True

    return subproblems_array[-1]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
print(can_construct("abcdeef", ["ab", "abc", "cd", "def", "abcd"]))  # False
print(
    can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
)  # False
print(
    can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "f"],
    )
)  # True
print(
    can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"],
    )
)  # False
