m_bar = 4
m_foo = 7
a_bar = int(input('Введіть х для точки А  '))
a_foo = int(input('Введіть у для точки А  '))
b_bar = int(input('Введіть х для точки В  '))
b_foo = int(input('Введіть у для точки В  '))
c_bar = int(input('Введіть х для точки С  '))
c_foo = int(input('Введіть у для точки С  '))
Bar = ((a_bar - m_bar)**2 + (a_foo - m_foo)**2)**0.5
Bar1 = ((b_bar - m_bar)**2 + (b_foo - m_foo)**2)**0.5
Bar2 = ((c_bar - m_bar)**2 + (c_foo - m_foo)**2)**0.5
if Bar < Bar1:
    if Bar < Bar2:
        print('Найменша відстань від точки А до точки М')
    else:
        print('Найменша відстань від точки С до точки М')
elif Bar1 < Bar:
    if Bar1 < Bar2:
        print('Найменша відстань від точки В до точки М')
    else:
        print('Найменша відстань від точки С до точки М')
elif Bar2 < Bar:
    if Bar2 < Bar1:
        print('Найменша відстань від точки С до точки М')