# Faça uma função que recebe um vetor l não necessariamente ordenado e 
# retorne um vetor v ordenado com os mesmos elementos de l.

# Faça isso usando busca binária (Exercício 5.3 deste laboratório).

# Comece a função criando um vetor v vazio (logo está ordenado).

# Para cada elemento x de l faça uma busca binária em v e descubra o 
# lugar certo de inserção do elemento, ou seja, para o vetor v 
# continuar ordenado com a inserção do elemento x. 

# Em seguida insira esse elemento nessa posição, não esqueça de 
# abrir espaço para a inserção do elemento.

l = eval(input())

def buscabinaria(v,i,j,x):
    print(v,i,j,x)
    m = (i+j)//2
    if i > j: 
        if v[i] >= x:
            v.insert(i, x)
        if len(v) == 1: return v+[[]]
        return v
    if i == j:
        v.insert(i,x)
        if type(v[i+1]) == int:
            if v[i]>v[i+1]:
                v[i+1], v[i] = v[i], v[i+1]
        return v
    if v[m] <= x: 
        i=m+1
        return buscabinaria(v,i,j,x)
    if v[m] > x: 
        j=m-1
        return buscabinaria(v,i,j,x)

def sort(v,l):
    if len(l) <= 1: return l
    for x in range(len(l)):
        if v[-1] != []:
            v += [[]]
        r = buscabinaria(v,0,len(v)-1, l[x])
    del r[-1]
    return r

print(sort([[]],l))
