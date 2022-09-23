import math as m
bar = float(input('Введіть число х:  '))
def f1():
    rez = 2.27 * m.e ** (4*bar+1) + 3
    return rez
def f2():
    rez = 0.64 * bar ** (bar+1)
    return rez
def f3():
    rez = m.log(bar, m.e) * m.fabs(bar - m.e ** bar)
    return rez
y = 0.0
if bar > 7:
    y = f1()
elif 0.5 < bar <= 7:
    y = f2()
else:
    y = f3()
print(int(y))