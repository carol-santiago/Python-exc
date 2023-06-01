class Matriz:    

    def __init__(self, n,m,v):
        self.n = n  # def numero de linhas da matriz
        self.m = m  # def numero de colunas da matriz
        
        self.v = [] # transforma a lista inputada numa matriz
        for i in range(n):
            self.v.append([])
        for i in range(n):
            for x in v[i*m:]:
                self.v[i].append(x)
                if len(self.v[i])>=m:break


    def __add__(self,other):
    # função de soma
        r = []
        for i in range(self.n):
            r.append([])
            for x,y in zip(self.v[i], other.v[i]):
                r[i].append(x+y)
        return r

    def __sub__(self,other):
        # função de subtração
        r = []
        for i in range(self.n):
            r.append([])
            for x,y in zip(self.v[i], other.v[i]):
                r[i].append(x-y)
        return r

    def __mul__(self,other):
        # função de multiplicação
        r = []
        for i in range(self.n):
        # gera uma matriz vazia com o numero de linhas da matriz resultante
            r.append([])
            for j in range(other.m):
            # atribui à matriz vazia o numero de colunas da matriz resultante
                r[i].append(0)
        
        # multiplica as linhas da primeira pelas colunas da segunda, e add os resultados na matriz resultante
        for linha_a in range(self.n):
            for coluna_b in range(other.m):
                for linha_b in range(other.n):
                    r[linha_a][coluna_b] += self.v[linha_a][linha_b] * other.v[linha_b][coluna_b]
        return r

    def __repr__(self):
        return str(self.v)

# organiza o input no formato correto (Matriz(n1,m1,v1)(operador)Matriz(n2,m2,v2))
OP = input() 
for i in range(len(OP)):
    if OP[i] == '+' or OP[i] == '-' or OP[i] == '*':
        X = OP[:i]
        Y = OP[i+1:]
        r = 'Matriz'+X
        s = 'Matriz'+Y
        z = r+OP[i]+s
        break
print(eval(z))
