class NumeroDecimal:    
    def __init__(self, n):
        self.n = n
    def __add__(self,other):
        return self.n + other.n

    def __sub__(self,other):
        return self.n - other.n
    
    def __mul__(self,other):
        return self.n * other.n

    def __truediv__(self,other):
        return self.n / other.n

    def __repr__(self):
        return str(self.n)

num = input() # num = operação, ex: 1.1+0.3
for i in range(len(num)):
    # organiza o input para que fique legível para o comando "eval" na ultima 
    # linha, tranformando o exemplo '1.1+0.3' em 'NumeroDecimal(1.1)+NumeroDecimal(0.3)'
    if num[i] == '+' or num[i] == '-' or num[i] == '/' or num[i] == '*':
        X = num[:i]
        Y = num[i+1:]
        r = 'NumeroDecimal('+X+')'
        s = 'NumeroDecimal('+Y+')'
        z = r+num[i]+s
        break
    else: 
        z = 'NumeroDecimal('+num+')'
print(eval(z))
