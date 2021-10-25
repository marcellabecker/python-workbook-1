def biggestMeasure(quantity, measure):
  cup = 0
  tablespoons = 0
  teaspoons = 0

  if measure == "cup":
    print(str(quantity) + " Cups")

  elif measure == "tablespoon":
    if quantity >= 16:
      cup = quantity/16
      quantity = quantity % 16

    if quantity >= 3:
      tablespoons = quantity/3
      quantity = quantity % 3

    if quantity < 3:
      teaspoons = quantity
      quantity = 0

  else:
    if quantity >= 48:
      cup = quantity/48
      quantity = quantity % 48

    if quantity >= 3:
      tablespoons = quantity/3
      quantity = quantity % 3

    if quantity < 3:
      teaspoons = quantity
      quantity = 0


  print(str(int(cup)) + " Cups, " + str(int(tablespoons)) +" tablespoons " + str(int(teaspoons)) + " teaspoons.")

def main():
  a = int(input("Digite a quantidade: "))
  b = input("Digite a unidade de medida: ")

  biggestMeasure(a, b)

main()