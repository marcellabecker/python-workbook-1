import string

def isInteger(string): return False if len(''.join(c for c in string.strip() if not c.isdigit())) > 1 and ''.join(c for c in string.strip() if not c.isdigit()) != '-' and ''.join(c for c in string.strip() if not c.isdigit()) != '+' else True

def main(): print("INTEIRO") if isInteger(input("DIGITE A STRING: ")) else print("NÃO É INTEIRO")

if __name__ == "__main__": main()