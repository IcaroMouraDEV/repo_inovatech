# Faça um programa que gere uma nova lista contendo apenas números ímpares.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def odd_list(list):
    odds = []
    for num in list:
        if num % 2 != 0:
            odds.append(num)

    return odds


print(odd_list(a))
