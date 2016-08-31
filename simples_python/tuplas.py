# coding=utf-8

### TUPLAS
t = 1, 2, 'python'

print 'elemento 0 da tupla: ' + str(t[0])

print 't = ' + str(t)

# Podemos aninhar tuplas:
u = t, (1, 2, 3, 4, 5)
print 'u = ' + str(u)


# empacotamento: a lista de variáveis do lado esquerdo deve ter o mesmo comprimento da sequência à direita
a, b, c = t
print 'a = ' + str(a) + ' b = ' + str(b) + ' c = ' + str(c)
a, b = b, a
print '(a, b) = (' + str(a) + ', ' + str(b) + ')'

# concatenaçao
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print t1 + t2