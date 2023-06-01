# Link para as instruções: https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/baralho/

sequência = input("sequência do baralho:")

l = []
def div(seq): 
    # divide a sequência em trechos ddN (Ex.: '01C05E' --> ['01C', '05E'])
    if len(seq) < 3: return l
    l.append(seq[0:3])
    return div(seq[3:])

list = div(sequência)

def check(s):
    # checa se existe alguma carta repetida no baralho
    bb = []
    for x in range(len(list)): 
        # filtra apenas as cartas do naipe a ser analisado
        if list[x][2] == s:
            bb += [list[x]]
    for x in bb: # remove uma carta e checa se ainda existe alguma igual a ela 
        bb.remove(x)
        if x in bb: 
            return True
        else:
            return False

def count(i):
    # conta quantas cartas do naipe "i" o baralho contém
    if check(i) == True: return 'erro'
    count = 0
    for x in range(len(list)):
        if list[x][2] == i:
            count += 1
    return count

def out(j):
    # gera a quantidade de cartas faltando para completar o naipe "j"
    if type(count(j)) == int:
        r = 13 - count(j)
        return r
    else:
        return count(j)
    
print(out('C'))
print(out('E'))
print(out('U'))
print(out('P'))
