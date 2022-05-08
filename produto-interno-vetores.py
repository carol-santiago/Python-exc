#Implementar o produto interno de dois vetores.
#Ler dois vetores.  (coordenadas são inteiras)
#Imprimir o resultado do produto interno. (inteiro)
#Exemplos:
#Input: [2] [3] Output: 6
#Input: [2,3] [2,3] Output: 13
#Input: [1,1,1,1] [2,2,2,2] Output: 8
#Obs: Faça duas leituras, uma para cada vetor

v1, v2, v = eval(input()), eval(input()), []
for i in range(len(v1)): # acessa o índice de cada elemento
    v.append(v1[i]*v2[i]) # multiplica os elementos do vetor 1 pelos elementos do vetor 2 de mesmo índice
print(sum(v)) # imprime a soma dos produtos
