# Escreva um programa que retorne o que ambas as listas têm em comum
# (sem repetições).
# O seu programa deve funcionar para listas de qualquer tamanho.

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def common_in_list(list, list2):
    common = set()

    for item in list:
        for item2 in list2:
            if item == item2:
                common.add(item)

    return [item for item in common]


print(common_in_list(a, b))
