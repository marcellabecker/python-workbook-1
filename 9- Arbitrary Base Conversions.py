#! /usr/bin/env python3
#base original do numero de 0 a f pois pode ser de 2 a 16 a base
def base1(num_original,base_original):
    num_original = str(num_original)
    base_original = int(base_original)
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    dec = 0
    dec_temp = list(num_original)
    dec_temp.reverse()
    for x,i in enumerate(dec_temp):
        dec += dic.index(i) * base_original**(x)
    return str(dec)
#base final do numero de 0 a f pois pode ser de 2 a 16 a base
def base2(dec,base_final):
    base_final = int(base_final)
    dec = int(dec)
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    numero_final_temp = []
    numero_final = ''
    while True:
        temp_numero_final = dec%base_final
        numero_final_temp.append(temp_numero_final)
        if int(dec/base_final) == 0:
            break
        dec = int(dec/base_final)
    numero_final_temp.reverse()
    for i in numero_final_temp:
        numero_final += dic[i]     
    return numero_final
#conversão
def Converter(num_original,base_original,base_final):
    num_or = base1(num_original,base_original)
    num_final = base2(num_or,base_final)
    return print(num_final)
#imputs
def main():
    num = (input("Digite um numero para converter: "))
    original_base = input("Digite a base orginal do numero: ")
    final_base = input("Digite a base a ser convertida: ")
   
    Converter(num, original_base, final_base)
#chama a função.    
if __name__ == '__main__':
    main()