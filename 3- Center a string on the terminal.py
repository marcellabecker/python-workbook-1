#! /usr/bin/env python3
from typing import Text

#função que tem uma string como seu primeiro parâmetro e a largura do terminal como seu segundo parâmetro,
def center_string (text, spaces):
    c =''
    a = len(text)
    b = (spaces/2) - (a/2) 
    for i in range(0, int(b), 1):
        c += ' '
    c += text
    return c

#programa principal que demonstre sua função
texto = str(input('texto: '))
espaço = int(input('espaços: '))

print(center_string(texto,espaço))