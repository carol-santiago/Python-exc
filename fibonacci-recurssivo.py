# Faça uma função lazy (geradora) chamada f_lazy_fibonacci(n) que retorna a sequencia de Fibonacci (igual ao Exercício 2.3).
# A entrada é uma tupla (n,m)
# n é o mesmo do Exercício 2.3. 
# m é outro inteiro que será usado no código abaixo que deve estar no seu código.

# l = []
# for x in f_lazy_fibonacci(n ):
#     if x > m:
#      break
#     else:
#      l.append(x)
# print(l)

# Ex:
# Input: (1,1) Output: [0, 1, 1]
# Input: (0,1) Output: [0]
# Input: (9,10) Output: [0, 1, 1, 2, 3, 5, 8]
# Input: (9,3) Output: [0, 1, 1, 2, 3]
# Input: (10000000000,10) Output: [0, 1, 1, 2, 3, 5, 8]
# obs: Se não fizer uma função do tipo Lazy, o código vai ser abortado por limite de tempo.

# resumo: gera todos os numeros até n, printa todos os números gerados 'n' que sao menores que m

n = (0,1)
n,m = n

def f_lazy_fibonacci(n):
    x = y = 1
    if n == 0: 
        yield n
    else:
        for i in range(-2, n):
            if i == -2: yield 0
            if i == -1: yield 1
            x, y = y, x + y
            yield x

l = []
for x in f_lazy_fibonacci(n): #f_lazy_fibinacci(n) == 0, 1, 1, 2, 3...
    if x > m:
     break
    else:
     l.append(x)
print(l)
