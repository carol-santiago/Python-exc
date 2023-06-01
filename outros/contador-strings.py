#Receba uma string e depois imprima numa única linha os seguintes itens:
#Número de caracteres, número de letras, número de números, número de símbolos (tudo que não é letras e nem número) e número de palavras.
#Exemplos:
#Input: "Ninguém sabe de nada!"
#Output: 21 17 0 4 4
#Input: "U2 é uma banda formada em 1976"
#Output: 30 19 5 6 7
#obs: o verificador automatico de código, não está lidando bem quando a string tem alguma letra que começa com \, por exemplo \n. Ele está consideranto o \n como duas letras. Nesse caso, não teste em casa para ver se o seu código está correto.

string = input()
a = len(string)

b = 0
for x in string:
    if x > '@' and x < '[' or x >= 'À':
        b += 1
for x in string:
    if x > '`' and x < '{':
        b += 1

c = 0
for x in string:
    if x >= '0' and x <= '9':
        c += 1

d,z = 0,0
for x in string:
    if x >= ' ' and x < '0' or x >= ':' and x <= '@':
        d += 1
    elif x == "\n":
        z += 1
d = d + z

e, y = 0, 0
for x in string:
    if x == " ":
        e += 1
    elif x == "\n":
        y += 1
        e = e + (y-1)
print(a,b,c,d,e+1)
