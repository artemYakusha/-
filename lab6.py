#6.1
import math as m
a = int(input('Введіть нижню границю: '))
b = int(input('Введіть верхню границю: '))
h = int(input('Введіть значення кроку: '))

for Bar in range(a, b, h):
    foo = m.fabs(m.tan(m.fabs(a)+0.1))
    print(foo)
#6.2
import math as m
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))
spisok = []
spisok1 = []
while a < b:
    foo = m.fabs(m.tan(m.fabs(a)+0.1))
    spisok.append(foo)
    spisok1.append(a)
    a += h
l = len(spisok)
spisok.append(spisok1)

#6.3
Foo = 0
while Foo != len(spisok):
    print(spisok[Foo])
    Foo += 1
Foo1 = 0
while Foo1 != len(spisok1):
    print(spisok1[Foo])
    Foo1 += 1
print(spisok)
spisok3 = []
FOO = 0
for BAR in range(0, l):
    FOO = spisok1[BAR] * spisok[BAR]
    spisok3.append(FOO)
print(spisok3)