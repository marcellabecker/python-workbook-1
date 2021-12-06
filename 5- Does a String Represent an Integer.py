#! /usr/bin/env python3
import string
#determina se os caracteres em uma string representam ou não um inteiro válido.
def isInteger(string): return False if len(''.join(c for c in string.strip() if not c.isdigit())) > 1 and ''.join(c for c in string.strip() if not c.isdigit()) != '-' and ''.join(c for c in string.strip() if not c.isdigit()) != '+'else True
#printa se é ou não inteiro
def main(): print("INTEIRO") if isInteger(input("DIGITE A STRING: ")) else print("NÃO É INTEIRO")
#chama a função de printar
if __name__ == "__main__": 
    main()