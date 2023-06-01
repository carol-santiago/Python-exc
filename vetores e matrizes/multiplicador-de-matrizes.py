#Ler duas matrizes (todos os elementos são inteiros)
#Retornar a multiplicação dessas duas matrizes.
#Caso a multiplicação não seja válida imprimir 'Erro!'
#obs: número de colunas e/ou número de linhas pode ser 1. 
#Exemplo
#input: [[2,1],[3, 2]] [[1,2],[1,1]] Output:[[3,5],[5,8]]
#input:[1] [2] Output: [2]
#input: [1,2] [[1],[2]] Output: [5]
#input:[[1],[2]] [1,2] Output: [[1,2],[2,4]]
#input:[[1,0],[0,0]] [2] Output: Erro!
#obs: Faça duas leituras, uma para cada matriz
#obs: O objetivo é fazer a multipicação sem o uso de funções.

matriz_a, matriz_b, matriz_final = eval(input()), eval(input()), []
if type(matriz_a[0]) != list or type(matriz_b[0]) != list: # nenhum input é uma matriz
    if type(matriz_a[0]) != list and type(matriz_b[0]) != list:
        if len(matriz_a) == 1 and len(matriz_b) == 1:
            for x in matriz_a:
                for y in matriz_b:
                    matriz_final = x*y
            r = []
            r.append(matriz_final)
            print(r)
    if type(matriz_a[0]) != list and type(matriz_b[0]) == list: # matriz_a não é uma matriz
        matriz_a2 = []
        matriz_a2.append(matriz_a)
        matriz_a = matriz_a2
    elif type(matriz_b[0]) != list and type(matriz_a[0]) == list: # matriz_b não é uma matriz
        matriz_b2 = []
        matriz_b2.append(matriz_b)
        matriz_b = matriz_b2
if type(matriz_a[0]) ==  list and type(matriz_b[0]) == list:  # ambos são matrizes
    if len(matriz_a[0]) == len(matriz_b): # checa se a multiplicação é válida
        if len(matriz_b[0]) > len(matriz_a[0]): # def quantidade de linhas e colunas na matriz_final
            if len(matriz_b) >= len(matriz_a):
                for x in range(len(matriz_b)):
                    matriz_final.append([])
                    for i_b in matriz_b[0]:
                        matriz_final[x].append(0)
            else:
                for x in range(len(matriz_a)):
                    matriz_final.append([])
                    for i_a in matriz_a:
                        matriz_final[x].append(0)
        else:
            for x in range(len(matriz_a)):
                matriz_final.append([])
                for i_a in matriz_a:
                    matriz_final[x].append(0)
        #multiplicador
        for i in range(len(matriz_a)): # para i linha da matriz_a
            for j in range(len(matriz_b[0])): # para j elemento da matriz_b
                for k in range(len(matriz_b)): # para k linha da matriz_b
                    matriz_final[i][j] += matriz_a[i][k] * matriz_b[k][j]
        print(matriz_final)
    else:
        print('Erro!')
