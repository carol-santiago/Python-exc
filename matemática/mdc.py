#Faça uma função que retorna um conjunto (set) com todos os divisores de um número inteiro positivo.
#Faça uma segunda função que recebe os dois ou mais números inteiros positivos.
#Chame a primeira função para um dos números obtendo os conjuntos de seus divisores.
#Calcule e retorne a interseção desses conjuntos, ou seja, os divisores comum desses números.
#Entrada uma tupla com os números.
#Saída um conjunto com os divisores comuns.

n = eval(input())

def divisores(numero):
    s = set()
    for i in range(1, numero+1):
        if numero%i == 0:
            s.add(i)
    return s
            
def itsc(n):
    l = []
    for i in n:
        l.append(divisores(i))
    for i in l:
        intersec = l[0].intersection(i)
    return intersec

print(itsc(n))
