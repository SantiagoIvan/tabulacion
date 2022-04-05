# De cuantas formas se puede construir??


def can_construct(target_word, array):
    subproblems_array = [0 for i in range(len(target_word) + 1)]
    subproblems_array[0] = 1

    for i in range(len(target_word) + 1):
        if not subproblems_array[i]:
            continue
        for word in array:
            if target_word[i:].startswith(word):
                subproblems_array[i + len(word)] += subproblems_array[i]

    return subproblems_array[-1]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))  # 3 formas
# "ab", "cd", "ef" ; "abc","def" ; "abcd", "ef"
print(can_construct("abcdeef", ["ab", "abc", "cd", "def", "abcd"]))  # False
print(
    can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
)  # False
print(
    can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "f"],
    )
)  # Miles de formas
print(
    can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"],
    )
)  # False
