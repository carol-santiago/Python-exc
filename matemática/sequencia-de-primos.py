# Leia um número inteiro positivo n.
# Crie uma lista (list) com todos os números primos de 1 a n.
# Transforme essa lista em uma string e imprima a string.
# Ex:
# Input: 1 Output: '[]'
# Input: 5 Output: '[2,3,5]'

n = int(input())
list = []
for x in range(2,n+1):
    primo = True
    for y in range(2,x):
        if x%y == 0:
            primo = False
            break
    if primo == True:
                list.append(x)
list = str(list)
print(list)
