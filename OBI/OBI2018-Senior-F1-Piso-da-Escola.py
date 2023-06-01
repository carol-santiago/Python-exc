#OBI2018 Senior: piso da sala

L = int(input())
C = int(input())
Perimetro = (L*2)+(C*2)
Tipo_1 = C**2 - (C-L)
Tipo_2 = Perimetro-4

print(Tipo_1, Tipo_2)
