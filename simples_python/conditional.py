# coding=utf-8

### TYPES
var_int = 5
var_str = 'python class'
var_bool = var_int > 10

print var_int, type(var_int)
print var_str, type(var_str)
print var_bool, type(var_bool)

#### IF
age = int(input("Qual sua idade: "))
if age < 12:
    print("Criança")
if age >= 12:
    print("Adolescente")
if age > 18:
    print("Adulto")
if age > 60:
    print("Idoso")

#### ELSE
mark = int(input("Digite sua nota: "))
if mark < 5:
    print ("Você está reprovado")
if mark < 7:
    print ("Você está em recuperação")
else:
    print ("você foi aprovado")

### ELSE IF
valor_compra = float(input("Valor da compra: "))
if valor_compra < 100:
    desconto = valor_compra * 0.10
else:
    if valor_compra < 500:
        desconto = valor_compra * 0.20
    else:
        desconto = valor_compra * 0.30