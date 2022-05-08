#Faça um algoritmo que receba dois vetores A[1 .. n] e B[1 .. m] e decida se existe um índice i tal que A[i] = B[i].
#obs: fazer duas leituras, uma para cada vetor e retornar um booleano (True ou False).
#Ex:
#Input: [1, 3, 5, 7, 'a', 'aba']
#[33, 9, 0]
#Output: False

A, B = eval(input()), eval(input())
for i in range(len(A)):
    for x in range(len(B)):
        if A[x] == B[x]:
            r = True
            break
        else:
            r = False
print(r)
