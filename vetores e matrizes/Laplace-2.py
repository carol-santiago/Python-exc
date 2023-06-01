# Calcular o determinante de uma matriz quadrada A de tamanho máximo n>=4.

# Obs: os coeficientes da matriz são inteiros e o formato da matriz é igual ao do exc.4 e 5

# Para calcular o determinante utilizar o teorema de Laplace: 

# "O determinante de uma matriz é igual à soma dos produtos dos elementos de qualquer linha ou coluna 
# pelos respectivos complementos algébricos (cofatores matriciais)"

# Laplace reduz o cálculo do determinante de uma matriz de ordem n ao cálculo de determinantes 
# de matrizes de ordem n-1, tem que fazer isso de forma recursiva até chegar a determinante de ordem 3 
# (tem que utilizar a função feita no Exercício 2.1). 

# Cofator: (-1)^i+j x D[i][j].

import copy

matriz = eval(input())

def sarrus(m): 
    d1 = m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1]
    d2 = m[0][0]*m[1][2]*m[2][1] + m[0][1]*m[1][0]*m[2][2] + m[0][2]*m[1][1]*m[2][0] 
    D = d1 - d2
    return D

def redutor(m, j):
    for i in range(len(m)):
        del m[i][j]
    del m[0]
    return laplace(m)

def cofator(m, j, coeficiente):
    m_deepcopy = copy.deepcopy(m)
    m_cofator = (coeficiente) * ((-1)**j) * redutor(m_deepcopy, j)
    return m_cofator

def laplace(m):
    if len(m) == 3:
        return sarrus(m)
    if len(m) > 3:

        D = []
        for x in range(len(m)):
            D.append(cofator(m, x, m[0][x]))
        return sum(D)

print(laplace(matriz))
