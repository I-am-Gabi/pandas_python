# coding=utf-8
# source: https://github.com/marcelcaraciolo/pandas-tutorial/blob/master/0%20-%20Introducao.ipynb

import pandas as pd

# objeto em uma dimensão similar ao array
example_series = pd.Series([1, 5, 10, 30, 50, 30, 15, 40, 45, 50])

print('media : ' + str(example_series.mean()))

# valor que separa a metade superior da metade inferior de uma distribuição de dados
print('mediana : ' + str(example_series.median()))

# o valor que mais se repete dentro de um conjunto
print('moda : \n' + str(example_series.mode()))

print('amplitude : ' + str(example_series.max() - example_series.min()))

# A variância é uma medida que expressa quanto os dados de um conjunto estão afastados de seu valor esperado
print('variância : ' + str(example_series.var()))

# O desvio padrao indica quanto os dados estão afastados da média
print('desvio padrão : ' + str(example_series.std()))

# desvio obsoluto: O Desvio Absoluto é calculado da seguinte forma: primeiro,
# encontramos a média dos valores; depois, calculamos a distância de cada
# ponto desta média; somamos as distâncias e dividimos o resultado pela média
# destas distâncias.
print('desvio obsoluto : ' + str(example_series.mad()))
print

# especificar o índice que será usado quando cria uma Series
example_series2 = pd.Series(['banana', 'morango', 'caju'], ['fruta1', 'fruta2', 'fruta3'])
print example_series2
print

# O construtor de Series pode converter um dicionario também
d = {'Recife': 1000, 'Brasilia': 1300, 'Maceio': 900, 'Salvador': 1100,
     'Aracaju': 450, 'Natal': None}
cities = pd.Series(d)
print cities
print
print cities['Brasilia']
print
print cities[['Brasilia', 'Salvador', 'Recife']]
print

#ou ate boolean indexing para selecao
print cities[cities < 1000]
print
print cities[cities.isnull()]

print
data = {'ano': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012, 2015, 2014],
        'time': ['Flamengo', 'Flamengo', 'Flamengo', 'Vasco', 'Vasco', 'Cruzeiro', 'Cruzeiro', 'Cruzeiro', 'Vasco', 'Flamengo'],
        'vitorias': [11, 8, 10, 15, 11, 6, 10, 4, 3, 1],
        'derrotas': [5, 8, 6, 1, 5, 10, 6, 12, 9, 10]}
football = pd.DataFrame(data, columns=['ano', 'time', 'vitorias', 'derrotas'])
print football
print
print football.describe()
print
print football[(football['ano'] > 2012) & (football['ano'] < 2015)].head(3)
