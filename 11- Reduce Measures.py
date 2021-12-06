#! /usr/bin/env python3
#definição das medidas
def Medidas(quantidade, medida):
  xicara = 0
  colher_de_sopa = 0
  colher_de_cha = 0
  #para a xicara
  if medida == "xicara":
    print(str(quantidade) + " xicaras")
  #para colher de sopa
  elif medida == "colher de sopa":
    if quantidade >= 16:
      xicara = quantidade/16
      quantidade = quantidade % 16

    if quantidade >= 3:
      colher_de_sopa = quantidade/3
      quantidade = quantidade % 3

    if quantidade < 3:
      colher_de_cha = quantidade
      quantidade = 0
  #para colher de chá
  else:
    if quantidade >= 48:
      xicara = quantidade/48
      quantidade = quantidade % 48

    if quantidade >= 3:
      colher_de_sopa = quantidade/3
      quantity = quantidade % 3

    if quantity < 3:
      colher_de_cha = quantidade
      quantity = 0

  #printa as medidas
  print(str(int(xicara)) + " xicaras, " + str(int(colher_de_sopa)) +" colher_de_sopa e " + str(int   (colher_de_cha)) + " colher_de_cha.")
#imputs da quantidade e unidade de medida
def main():
  a = int(input("Digite a quantidade: "))
  b = input("Digite a unidade de medida: ")

  Medidas(a, b)

if __name__ == '__main__':
    main()