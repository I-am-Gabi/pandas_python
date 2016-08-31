# coding=utf-8

cesta = ['uva', 'laranja', 'uva', 'abacaxi', 'laranja', 'banana']
frutas = set(cesta)   # criar um conjunto sem duplicatas
print 'laranja' in frutas   # testar se um elemento existe é muito rápido
print 'capim' in frutas


a = set('abracadabra')
b = set('alacazam')
print a - b
print a | b
print a & b
print a ^ b