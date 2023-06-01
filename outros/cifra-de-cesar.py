# Faça duas duas funções: uma codificar uma mensagem e outra para descodificar uma mensagem.
# Deve receber uma mensagem (string), essa mensagem só tem as letras padrões e espaço (não tem acento, símbolo, maiúscula e número). A ordem deste alfabeto começa com "a" e termina com espaço, ou seja espaço fica depois da letra "z".
# Além da mensagem, receba um número que é a senha para codificar ou descodificar a mensagem.
# Para codificar, cada letra deve ser movida pelo alfabeto o número de letras. Exemplo: letra "a" e senha 1 retorna "b";  letra "a" e senha 3 retorna "d"; letra "b" e senha 2 retorna "d".
# Exemplo de codificação: "abc", senha 1, retorna "bcd".
# Para descodificar o processo é inverso. A mensagem recebida já está codificada e a senha serve para reconstruir a mensagem original. Exemplo: "bcd", senha 1, retorna "abc".
# Se a operação de shift passa o final do alfabeto, deve retorna para o início do alfabeto. Exemplo: codificar "xyz", senha 5, retorna "bcd". descodificar "a" senha 5 retorna "w".
# Leia uma tupla (x, m, s):
# x: booleano (True, False) - True se é para codificar a mensagem m e False para descodificar a mensagem m.
# m: String - mensagem
# s: inteiro - senha usada para codificar ou descodificar.

# Input: (True, "abc", 1)
# Output: "bcd"
# Input: (False, "bcd", 1)
# Output: "abc"
# Input: (True, "xyz", 5)
# Output: "bcd"
# Input: (False, "bcd", 5)
# Output: "xyz"

a = eval(input())
x,m,s = a
m = list(m)

import string
alfabeto = list(string.ascii_lowercase) + [' '] # cria uma lista com todas as letras do alfabeto + o caractere " "
index = [alfabeto.index(m[i]) for i in range(len(m))] # cria lista com os índices de cada caractere de 'm' em 'alfabeto'
k = []

def cod(): # função codificadora
    for i in index: # cria uma lista com os índices finais de m (índice em 'index' + senha)
        if i+s >= 27: # caso a soma seja maior que o tamanho da lista 'alfabeto', essa cláusula "recomeça a contagem" antes de fazer a soma
            k.append((i-27)+s)
        else:
            k.append(i+s)
    for x in range(len(m)): # substitui os elementos de m pela sua versão codificada
        m[x] = alfabeto[k[x]]
    return m
    
def dcod(): # função decodificadora
    for i in index: # cria uma lista com os índices finais de m (índice em 'index' - senha)
        if i-s < 0: # caso a subtração seja negativa, essa cláusula força a contagem reversa nos caracteres de alfabeto
            k.append((i+27)-s)
        else:
            k.append(i-s)
    for x in range(len(m)): # substitui os elementos de m pela sua versão decodificada
        m[x] = alfabeto[k[x]]
    return m

# transforma a mensagem em string após passar pelo processo de codificação ou decodificação
if x == True:
    m = cod()
else:
    m = dcod()
r = '' 
for i in m: 
    r += i 
print(r)
