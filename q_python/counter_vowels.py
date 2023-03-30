# Utilizando high order functions, crie a função conta_vogais.
# O parâmetro de entrada será uma string e o resultado deverá ser
# a contagem de vogais presentes em seu conteúdo.
# (Obrigatório utilizar as funções: len(), filter() e lambdas)
# Obs.: Não considerar caracteres acentuados
def counter_vowels(string):
    return len(list(filter(lambda x: x in 'aeiou', string)))


print(counter_vowels('icaro joel'))