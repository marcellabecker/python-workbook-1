#! /usr/bin/env python3
from fractions import Fraction
#printa a fração reduzida
def reduceFractions(numerator, denominator):
  print(Fraction(numerator, denominator))
#recebe os parametros
def main():
  a = int(input("Digite o numerador: "))
  b = int(input("Digite o denominador: "))
  reduceFractions(a, b)
#chama a função
if __name__ == '__main__':
    main()