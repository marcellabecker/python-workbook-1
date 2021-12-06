#! /usr/bin/env python3

# Definiremos uma boa senha como aquela que tem pelo menos 8 caracteres e contém pelo menos uma letra maiúscula, pelo menos uma letra minúscula e pelo menos um número.
def check_password(password): return False if (password.islower() or password.isupper() or len(password) < 8) else True

#A função que determina se uma senha é válida ou não.
def main(): print("senha ok") if check_password(input("digite sua senha: "))else print("senha fraca")

if __name__ == "__main__": main()