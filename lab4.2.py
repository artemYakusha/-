import math as m
bar = float(input('Введіть х '))
print(m.cos(bar) * m.tan(bar) + (m.log(5)*(m.e**bar+4) + 1/((m.fabs(bar) + 0.1)**0.5)))