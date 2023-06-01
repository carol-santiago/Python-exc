# Faça duas funções que uma retorna o número de dígitos de um número inteiro não negativo e outra que inverter o número (ex. 127 -> 721).
# Faça uma única leitura de um número. Depois aplique este número as duas funções e imprima uma tupla como primeiro elemento sendo o número de dígitos e o segundo o número invertido.

# Ex: 
# Input: 12345
# Output: (5, 54321)
# Input: 2
# Output: (1, 2)
# Input:  10
# Output: (2, 1)


n = input()
def contagem(n):
    return(len(n))
def invert(n):
    return int(n[::-1])
r = [contagem(n), invert(n)]
print(tuple(r))
