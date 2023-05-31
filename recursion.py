'''
#Funcion escensial utilizando un while
def conteo(n):
    i = n
    while i > 0:
        print(i)
        i -=1

conteo(10)

#recursion utilizando if en reemplazo de un while
def recconteo(n):
    if n <= 0:
        return 0
    print(n)
    recconteo(n-1)
recconteo(10)

#fibonacci

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-2)+fib(n-1)

print(fib(3)) #busco el valor de la posicion 20 / siempre fibonaci busca posiciones no numeros'''

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence

n = 8
fib_sequence = fibonacci(n)
print(fib_sequence)