# Escreva uma função que recebe uma lista e retorna uma nova lista
# sem elementos duplicados. Utilize a lista a seguir para testar sua função.
lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']


def filter_list(list):
    new_list = set()

    for item in list:
        new_list.add(item)

    return [item for item in new_list]


print(filter_list(lista))
