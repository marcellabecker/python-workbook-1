num = int(input('digite um numero:'))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
if total == 2:
    print('Ele é primo')
else:
    print('Não é primo')