import math as m
def func1():
    foo1 = ((m.sin(bar) - m.log10(bar)) / ((7 * bar) ** 0.5)) + ((bar + 4) ** (2 * bar - 8))
    return foo1
bar = float(input('Введіть х '))
foo = func1()
print(foo)