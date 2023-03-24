# Escreva uma função que recebe uma string de números separados por vírgula
# e retorne a soma de todos eles. Depois imprima a soma dos valores.
texto = "1,3,4,6,10,76"


def sum_string(string: str):
    nums = string.split(',')

    return sum([int(num) for num in nums])


print(sum_string(texto))
