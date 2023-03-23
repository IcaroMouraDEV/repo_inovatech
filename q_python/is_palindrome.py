# Verifique se cada uma das palavras da lista é ou não um palíndromo.
list = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']


def is_palindrome(word_list):
    res = []
    for word in word_list:
        res.append((word, True) if word == word[::-1] else (word, False))

    return res


print(is_palindrome(list))
