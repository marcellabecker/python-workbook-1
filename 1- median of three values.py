#! /usr/bin/env python3
#Determina os valores para serem calculados na mediana.
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

#Função Comparação_numérica compara os 3 valores digitados pelo usuário.
def Comparacao_numerica(a, b, c):
  if a > b:
    if a < c:
        return a
  if a > c:
    if b > a:
        return a
  if a > b:
    if b > c:
        return b
  if c > b:
    if b > a:
        return b
  if b > c:
    if c > a:
        return c
    else:
        return c

#Calculo da mediana
mediana = Comparacao_numerica(a, b, c)

#Print do valor da mediana.
print("A mediana é: ", mediana)
