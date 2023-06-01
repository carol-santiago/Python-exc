#"Na matemática, a sucessão de Fibonacci (ou sequência de Fibonacci), é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores.
#Os números de Fibonacci são, portanto, os números que compõem a seguinte sequência:
#0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ... " Texto tirado da Wikipedia.org
#Leia um número inteiro positivo n.
#Crie uma lista (list) com todos os números da sequencia de Fibonacci até n. Imprima a lista.
#Depois (em outra linha) imprima a soma dos elementos da lista.
#Ex:
#Input: 1 Output: [0, 1, 1]
#2
#Input: 0 Output: [0]
#0
#Input: 9 Output: [0, 1, 1, 2, 3, 5, 8]
#20

n = int(input())
r = []
if n >= 2:
    list = [0, 1]
    a = 2
elif n < 2: 
    list = [0,1,1]
    a = 0

def fibonacci():
    for x in range(a, n+a):
        r = list[x-2] + list[x-1]
        list.append(r)
    return list
    
for x in fibonacci():
    if x <= n:
        r.append(x)

print(r)
print(sum(r))
