# Dada as listas a seguir, faça um programa que imprima o dados
# na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]


def print_on_screen(firs_names, last_names, age):
    for i in range(len(firs_names)):
        print(f"{i} - {firs_names[i]} {last_names[i]} está com {age[i]} anos")


print_on_screen(primeirosNomes, sobreNomes, idades)
