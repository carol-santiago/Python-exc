#Calcular o determinante de uma matriz quadrada A de tamanho máximo n=3.
#Fazer 3 funções: uma para cada tamanho da matriz.

m = eval(input())
if len(m) == 1: # matriz 1x1
    def det1x1():
        return m[0][0]
    print(det1x1())
if len(m) == 2: # matriz 2x2
    def det2x2(): 
        d1, d2 = m[0][0]*m[1][1], m[0][1]*m[1][0] # d1 = a*d, d2 = b*c
        return d1 - d2
    print(det2x2())
if len(m) == 3: # matriz 3x3
    def det3x3(): 
        d1 = m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1] # d1 = aei + bfg + cdh
        d2 = m[0][0]*m[1][2]*m[2][1] + m[0][1]*m[1][0]*m[2][2] + m[0][2]*m[1][1]*m[2][0] # d2 = afh + bdi + ceg
        return d1 - d2
    print(det3x3())
