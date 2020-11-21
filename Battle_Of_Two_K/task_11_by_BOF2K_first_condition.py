from First_order_ODE import *
import numpy as np

try:
    print('_' * 70)
    print('Решение задачи Коши методом Эйлера'.center(70, '-'))

    eg1 = EulerMethod(2, 6, 2, -2, 1)

    print(f'Введённые данные:\na = {eg1.a}; b = {eg1.b}; x0 = {eg1.x_0}; y0 = {eg1.y_0}; h = {eg1.h}\n')
    print(f'-----------Для h1 = {eg1.h}-----------\n')
    eg1.print_()
    z1 = eg1.y_i().pop()
    print(f'Нужно уточнить = {z1}\n')
    eg1.grafik()

    print('+' * 100, '\n')

    eg2 = EulerMethod(2, 6, 2, -2, .5)
    print(f'Введённые данные:\na = {eg2.a}; b = {eg2.b}; x0 = {eg2.x_0}; y0 = {eg2.y_0}; h = {eg2.h}\n')
    print(f'-----------Для h2 = {eg2.h}-----------\n')
    eg2.print_()
    z2 = eg2.y_i().pop()
    print(f'Нужно уточнить = {z2}\n')
    eg2.grafik()

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

    eg3 = EulerMethod(2, 6, 2, -2, .4)
    print(f'Введённые данные:\na = {eg3.a}; b = {eg3.b}; x0 = {eg3.x_0}; y0 = {eg3.y_0}; h = {eg3.h}\n')
    print(f'-----------Для h3 = {eg3.h}-----------\n')
    eg3.print_()
    z3 = eg3.y_i().pop()
    print(f'Нужно уточнить = {z3}\n')
    eg3.grafik()

    print('_______________Уточнение по формуле Рунге_______________\n')

    d_1 = np.array([[z1, 1 ** 1, 1 ** 2], [z2, .5 ** 1, .5 ** 2], [z3, .4 ** 1, .4 ** 2]])
    d_2 = np.array([[1, 1 ** 1, 1 ** 2], [1, .5 ** 1, .5 ** 2], [1, .4 ** 1, .4 ** 2]])

    print(d_1)
    print('----------------------------------------- = Zp')
    print(d_2)
    print('\nВыислим определители:\n')

    D_1 = np.linalg.det(d_1)
    D_2 = np.linalg.det(d_2)

    print(D_1)
    print('-------------------- = Zp')
    print(D_2)

    print(f'\nz_p = {D_1 / D_2}')

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
    print('_____________________________________________________________________')
    print('_______________Решение задачи Коши методом Рунге-Кутты_______________\n')

    eg4 = RungeKuttaMethod(2, 6, 2, -2, 1)
    print('\n-------------------------------------------------------------------------------------------------'
          '--------------------------------------------------------------------')
    eg4.y_i_print()
    eg4.grafik()

    eg5 = RungeKuttaMethod(2, 6, 2, -2, .5)
    print('\n-------------------------------------------------------------------------------------------------'
          '--------------------------------------------------------------------')
    eg5.y_i_print()
    eg5.grafik()

    print('\n_______________Уточнение по формуле Рунге-Ромберга_______________\n')

    R = eg5.h / eg4.h

    z1 = eg4.y_i().pop()
    z2 = eg5.y_i().pop()

    Zpp = z1 + ((z1 - z2) / (R ** 4 - 1))
    print(f'Zpp = {Zpp}\n')

except Exception as error:
    print(error)
input('Нажмите "Enter" чтобы выйти...')
