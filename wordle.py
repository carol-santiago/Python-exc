from random import randint, random
from words import lista
x = randint(0, len(lista)-1)
r, t = ['','','','',''], ''
memoria = []
word = list(lista[x])

while r != word:
    if r == word:
            break
    else:
        INPUT = input('digite uma palavra de 5 letras: ')
        INPUT = list(INPUT)
        for i in range(len(word)):
            if word[i] == INPUT[i]:
                r[i] = INPUT[i]
            if INPUT[i] in word:
                print('a palavra contém', str(INPUT[i]))
    print(r)
for i in r:
    t += i
print('a palavra é', t, '\nparabéns!')