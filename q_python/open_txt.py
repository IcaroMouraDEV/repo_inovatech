#  Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt
# e imprime o seu conteúdo. Você deve criar um arquivo .txt na pasta do
# seu repositório e inserir seu nome, idade e ano de inicio do curso dentro
# dele com quebra de linhas por informação


def open_txt(path):
    with open(path, mode='r') as file:
        print(file.read())


open_txt('q_python/arquivo_texto.txt')
