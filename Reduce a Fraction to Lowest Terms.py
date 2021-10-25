from fractions import Fraction

def reduceFractions(numerator, denominator):
  print(Fraction(numerator, denominator))

def main():
  a = int(input("Digite o numerador: "))
  b = int(input("Digite o denominador: "))
  reduceFractions(a, b)

main()