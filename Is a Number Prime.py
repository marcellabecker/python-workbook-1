from math import sqrt
from itertools import count, islice

if __name__ == "__main__": main()

def isPrime(n):
    count=0
    if(n == 1): return True
    for i in range(2, n, 1):
        if(n % i == 0): count += 1
    if(count > 1): return False
    else: return True

num = int(input('Digite o numero: '))

if(isPrime(num)): print('PrimO')
else: print('Não primo')