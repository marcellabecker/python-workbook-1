#! /usr/bin/env python3
from typing import Text


def center_string (text, spaces):
    c =''
    a = len(text)
    b = (spaces/2) - (a/2) 
    for i in range(0, int(b), 1):
        c += ' '
    c += text
    return c


texto = str(input('texto: '))
espaço = int(input('espaços: '))

print(center_string(texto,espaço))