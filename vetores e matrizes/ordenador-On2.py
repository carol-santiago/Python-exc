#Faça uma função recursiva que ordena o vetor usando a seguinte ideia:
#Acha o menor valor do vetor.
#Troca o primeiro elemento do vetor com o valor que encontrou, ou seja, o primeiro valor (o menor) agora está no lugar certo.
#Faça o mesmo de forma recursiva para o vetor que começa na segunda posição.
#Obviamente não é permitido usar nenhuma função de ordenação e nem de achar máximo ou mínimo de uma vetor.
#Exemplo: 
#Vetor: [6, 3, 0, 5], primeira troca [0, 3, 6, 5]
#Agora temos que ordenar o vetor [3, 6, 5], onde o mínimo já está na posição certa e não faz nada.
#...
#No fim o vetor original fica [0, 3, 5, 6]
#A complexidade deste algoritmo é O(n2).
#Para cada posição i das n possíveis, temos que verificar n−i elementos pelo menor deles.

v = eval(input())

def select_sort(v):
    menor = 0
    for i in range(len(v)):
        if v[i] < v[menor]:
            menor = i
    v[0], v[menor] = v[menor], v[0]
    if len(v) >= 2:
        v[1:] = select_sort(v[1:])
    return v

print(select_sort(v))
