#! /usr/bin/env python3
#função coloca em maiúscula os caracteres apropriados em uma string.
def capitalize(text):
    text = text[0].upper() + text[1:]
    tam = len(text)
    for i in range(1, tam-2, 1):
        #Um “i” minúsculo deve ser substituído por um “I” maiúsculo se for precedido e seguido por um espaço
        if(text[i] == 'i' and text[i-1] == ' ' and text[i+1] == ' '):
            text = text[:i] + 'I' + text[i+1:]
        #O primeiro caractere sem espaço após um “.”, “!” ou "?"
        elif(text[i] == '.' or text[i] == '!' or text[i] == '?'):
        #O primeiro caractere na string também deve estar em maiúscula.
            if(text[i+1] == ' '):
                text = text[:i+2] + text[i+2].upper() + text[i+3:]
            else:
                text = text[:i] + text[i+1].upper() + text[i+2:]
    return text
#coloca-a em maiúscula usando sua função e exibe o resultado.
texto = str(input('Escreva o texto a ser capitalizado: '))
print(capitalize(texto))