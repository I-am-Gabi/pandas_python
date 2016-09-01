# coding=utf-8

# funções como parâmetros
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def imprime(a, b, foper):
    print(foper(a, b))


imprime(5, 4, soma)
imprime(10, 1, subtracao)


# Empacotamento e desempacotamento de parâmetros
def soma(a, b):
    print(a + b)


L = [2, 3]
soma(*L)


# lambda
x = 2
a = lambda z: x * 2
print(a(3))
