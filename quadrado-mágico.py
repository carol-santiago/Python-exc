# Faça uma função que retorna um booleano informando se uma matriz é um quadrado mágico.
# Dizemos que uma matriz quadrada de inteiros é um quadrado mágico se a soma dos elementos de cada linha, 
# a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal 
# e secundária são todas iguais.
# Ex: 
# Input: [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
# Output: True
# Input: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# Outpu: False

m = [[8, 3, 3], [1, 5, 9], [6, 7, 2]]
l = []
for i in (range(len(m))):
    l.append(i)
l = l[::-1]  #cria lista com os índices inversos (para uma matriz3x3: l = [2,1,0])
def diagonais():
    d1, d2 = [], []
    for i in range(len(m)): 
        d1.append(m[i][i]) #cria lista com a diagonal principal
    for i in range(len(m)): 
        d2.append(m[i][l[i]]) #cria lista com a diagonal inversa
    if sum(d1) == sum(d2): # compara as somas dos elementos de d1 e d2
        return True
def linhas():
    s = []
    for i in m:
        s.append(sum(i)) # cria lista com a soma dos elementos de cada linha de m
    if sum(s)/len(m) == s[0]: # checa se as somas são iguais
        return True
def colunas():
    y = []
    for i in range(len(m)):
        y.append([]) # cria matriz para as colunas
    for i in l:
        for j in range(len(m)):
            y[i].append(m[j][i]) # add elementos à matriz, fazendo com que cada linha de y seja uma coluna de m
    for i in range(len(y)): 
        y[i] = sum(y[i]) # substitui os elementos das listas, que representavam colunas de m, para a soma dos elementos das mesmas
    if sum(y)/len(m) == y[0]: # checa se as somas são iguais
        return True
if diagonais() and colunas() and linhas() == True: # checa se as somas das diagonais, linhas e colunas são iguais
    print(True)
else:
    print(False)
