#! /usr/bin/env python3
import random
#função que gera a senha
def passwordGenerator():
# de 7 a 10 caracteres  
  lenght = random.randint(7,10)
  password = ''

  for x in range (lenght):
   #selecionado aleatoriamente das posições 33 a 126 na tabela ASCII. 
    randomChar = random.randint(33,126)
    password = password + chr(randomChar)
#printa a senha
  print(password)

passwordGenerator()