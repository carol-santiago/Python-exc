# exemplo: encontrar os multiplos de >>3<< menores que >>54<<

# output: existem 18 multiplos de 3 menores que 54
# estes são: {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51}

num1, num2 = int(input('encontrar os multiplos de:')), int(input('menores que:'))

multiplos = set()
x = 0
for i in range(num2):
    if i%num1 == 0:
        multiplos.add(i)
        x += 1
print('existem', x, 'multiplos de', num1, 'menores que', num2)
print('estes são:', multiplos)
