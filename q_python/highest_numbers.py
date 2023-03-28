# Você está recebendo um arquivo contendo 10.000 números inteiros,
# um em cada linha. Utilizando lambdas e high order functions, apresente os 5
# maiores valores pares e a soma destes(Obrigatório utilizar as funções:
# filter(), sorted(),  sum() e lambdas. Função map() é opcional).
def highest_numbers(path):
    with open(path, mode='r') as file:
        data = file.read()
        data = list(sorted(filter(lambda x: x % 2 == 0, [
            int(num) for num in data.split('\n')
        ])))
        return sum(data[len(data)-5:])


print(highest_numbers('q_python/numbers.txt'))
