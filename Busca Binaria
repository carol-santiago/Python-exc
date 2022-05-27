v,x = eval(input()), int(input())
n = len(v)
def buscabinaria(i,j):
    if i > j: return -1
    m = (i+j)//2
    if v[m] < x: 
        i=m+1
        return buscabinaria(i,j)
    if v[m] > x: 
        j=m-1
        return buscabinaria(i,j)
    if v[m] == x: return m
print(buscabinaria(0,n-1))
