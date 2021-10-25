import random

def passwordGenerator():
  
  lenght = random.randint(7,10)
  password = ''

  for x in range (lenght):
    
    randomChar = random.randint(33,126)
    password = password + chr(randomChar)

  print(password)

passwordGenerator()