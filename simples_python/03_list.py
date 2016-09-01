# coding=utf-8

### LISTS
a = [66.25, 333, 333, 1, 1234.5]
# Devolve o número de vezes que o valor x aparece na lista.
print str(a.count(333)) + " x333 | " + str(a.count(66.25)) + " x66.25 | " + str(a.count('x')) + " x66.25 \n"

a.insert(2, -1) # Insere um item em uma posição especificada
a.append(333) # a.insert(len(a), x)
a.append([3, 4]) # OBS: a lista será inteiramente adicionada, como se fosse um novo elemento
print 'a = ' + str(a)

L = [0, 4, 7]
a.extend(L) # O extend vai "extrair" os elementos passados por parâmetro e inserí-los em nossa lista
print 'a = ' + str(a) + '\n'

print 'índice de 333: ' + str(a.index(333)) # Devolve o índice do primeiro item cujo valor é igual a x

a.remove(333) # Remove o primeiro item encontrado na lista cujo valor é igual a x
print 'remove(333) | a = ' + str(a) + '\n'

a.reverse() # Inverte a ordem dos elementos na lista in place (sem gerar uma nova lista)
print 'reverse() | a = ' + str(a) + '\n'

a.sort() # Ordena os itens na própria lista in place.
print 'sort() | a = ' + str(a) + '\n'

a.pop(0)
print 'pop(0) | a = ' + str(a) + '\n'

del a[0]
print 'del a[0] | a = ' + str(a) + '\n'

del a[2:4]
print 'del a[2:4] | a = ' + str(a) + '\n'

del a[:]
print 'del a[:] | a = ' + str(a) + '\n'

