
#1-zadatak for petlja:
suma=0
for i in range(2, 101, 2):
    suma += i
print("Suma (for):", suma)

#1-zadatak while petlja
suma = 0
i = 2
while i <= 100:
    suma += i
    i += 2
print("Suma (while):", suma)

#2-zadatak for pellja
neparni = []
for i in range(1, 20, 2):   # prva 10 neparnih: 1,3,5,…,19
    neparni.append(i)

for broj in reversed(neparni):
    print(broj)

#2-zadatak while petlja
neparni = []
i = 1
while len(neparni) < 10:
    neparni.append(i)
    i += 2

index = len(neparni) - 1
while index >= 0:
    print(neparni[index])
    index -= 1

#3-zadatak for petlja
a, b = 0, 1
for _ in range(1000):   # broj ponavljanja je više nego potrebno
    if a > 1000:
        break
    print(a)
    a, b = b, a + b

#3-zadatak while petlja
a, b = 0, 1
while a <= 1000:
    print(a)
    a, b = b, a + b