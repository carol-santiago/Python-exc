#OBI2018 Senior: Garamana

P = input()
A = input()

r = 0
for char in A:
    if char == '*' or char in P:
        r += 1

if r == len(P):
    print('S')
else:
    print('N')
