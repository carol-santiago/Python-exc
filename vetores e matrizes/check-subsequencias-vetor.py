# Decidir se um vetor A[1 .. k] é uma subsequência de um vetor B[1 .. n]. (Por exemplo, (5, 6, 4) é subsequência de (9, 5, 6, 3, 9, 6, 4, 7).) Escreva um algoritmo RECURSIVO para resolver o problema.
# obs: fazer duas leituras, uma para cada vetor e retornar um booleano (True ou False).
# Ex:
# Input: [33, 9, 0] 
# [1, 3, 5, 7, 'a', 'aba']
#  Output: False

A, B = eval(input()), eval(input())
def check(a, b):
     # Casos base
    if a == []: return True
    if b == []: return False
    if a[0]==b[0]: return check(a[1:], b)
    # Passo indutivo
    return check(a,b[1:])
print(check(A, B))
