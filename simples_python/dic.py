# coding=utf-8

mercadinho = {"Banana": 3.00,
              "Maçã": 5.00,
              "Uva": 8.00}

print("Manga" in mercadinho)
print("Uva" in mercadinho)


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel

print tel['jack']

del tel['sape']
tel['irv'] = 4127
print tel

print tel.keys()

print 'guido' in tel

print dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

print dict([(x, x**2) for x in (2, 4, 6)])     # use uma list comprehension


# Quando chaves são strings simples, é mais fácil especificar os pares usando argumentos nomeados no construtor
print dict(sape=4139, guido=4127, jack=4098)