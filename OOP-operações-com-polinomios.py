# Implementação da classe Polinômio, que será usada para representar 
# polinômios envolvendo uma variável, isto é, polinômios da forma

# a0+a1x+a2x2+⋯+anxn

# A classe implementa soma, subtração e multiplicação 
# de polinômios, entre outros métodos.

class Polinomio:
    "Representa um polinomio de uma variavel"

    def __init__(self, coeficiente):
        "Construtor, onde a lista coeficientes contem os coeficientes para os termos de grau 0, grau 1, etc."
        self.coeficiente = coeficiente

    def __setitem__(self, grau, coeficiente):
        "Altera o coeficiente para o termo do grau dado"
        self.coeficiente[grau] = coeficiente
        pass

    def __getitem__(self,grau):
        "Retorna o coeficiente para o grau dado"
        return self.coeficiente[grau]

    def grau(self):
        "Retorna o grau do polinomio"
        return len(self.coeficiente)

    def __mul__(self,p):
        "Retorna o polinomio dado pela multiplicacao deste polinomio por p (tambem um polinomio)"
        
        # transforma os polinômios para que ambos tenham o mesmo grau
        if len(list(self)) > len(list(p)):
            l = len(list(self)) - len(list(p))
            for i in range(l):
                p.coeficiente.append(0)
        if len(list(self)) < len(list(p)):
            l = len(list(p)) - len(list(self))
            for i in range(l):
                self.coeficiente.append(0)
        
        # faz a multiplicação distributiva dos coeficientes e corrige o grau de acordo com sua posição
        r = []
        w = []
        for n in self.coeficiente:
            for m in p.coeficiente:
                r.append(n*m)
                if len(r) == len(self.coeficiente):
                    w.append(Polinomio(r).avalia(x))
                    r = []
        return Polinomio(w)

    def __add__(self,p):
        "Retorna o polinomio dado pela soma deste polinomio com p (tambem um polinomio)"
        
        # transforma os polinômios para que ambos tenham o mesmo grau
        if len(list(self)) > len(list(p)):
            l = len(list(self)) - len(list(p))
            for i in range(l):
                p.coeficiente.append(0)
        if len(list(self)) < len(list(p)):
            l = len(list(p)) - len(list(self))
            for i in range(l):
                self.coeficiente.append(0)
        
        # faz a soma 2 a 2 dos coeficientes
        r = []
        for x,y in zip(self, p):
            r.append(x+y)
        return Polinomio(r)

    def __sub__(self,p):
        "retorna o polinomio dado pela diferenca entre este polinomio e p (tambem um polinomio)"
        
        # transforma os polinômios para que ambos tenham o mesmo grau
        if len(list(self)) > len(list(p)):
            l = len(list(self)) - len(list(p))
            for i in range(l):
                p.coeficiente.append(0)
        if len(list(self)) < len(list(p)):
            l = len(list(p)) - len(list(self))
            for i in range(l):
                self.coeficiente.append(0)

        # faz a subtração 2 a 2 dos coeficientes
        r = []
        for x,y in zip(self, p):
            r.append(x-y)
        return Polinomio(r)

    def avalia (self,x):
        "Retorna a avaliacao do polinomio avaliado em x."
        # faz a substituição do "x" elevado ao seu respectivo grau
        s = []
        for i in range(len(self.coeficiente)):
            s.append(self.coeficiente[i] * x**i)
        return sum(s)


# O programa lê 3 entradas separadas onde (1) é a lista com
# os coeficiente do polinômio p; (2) é a lista com os coeficiente do 
# polinômio q; (3) um número x

# O programa imprime p.avalia(x),q.avalia(x),(p+q).avalia(x),(p-q).avalia(x),(p*q).avalia(x)

# Ex: Input: [1,2,0,0.5]
# [0,-1,2]
# 3
# Output:
# 20.5 15 35.5 5.5 307.5

coeficiente_p = eval(input())
coeficiente_q = eval(input())
x = eval(input())
p = Polinomio(coeficiente_p)
q = Polinomio(coeficiente_q)

print(p.avalia(x),q.avalia(x),(p+q).avalia(x),(p-q).avalia(x),(p*q).avalia(x))
