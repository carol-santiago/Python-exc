#OBI2018 Senior: figurinhas da copa

(n,c,m) = eval(input())
xi = eval(input())
yi = eval(input())

r = 0
for i in xi:
    if i in yi:
        r += 1

print(c-r)
