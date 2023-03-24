# Escreva uma função que recebe um número variável de parâmetros não
# nomeados e um número variado de parâmetros nomeados e imprime o valor
# de cada parâmetro recebido. Dica: pesquise sobre *args e **kwargs.
# Aplique os seguintes parâmetros:


def print_args(*args, **keyargs):
    list = [*args, *keyargs.values()]

    for arg in list:
        print(arg)


print_args(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
