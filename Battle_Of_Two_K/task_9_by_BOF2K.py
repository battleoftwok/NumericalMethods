try:
    x = [2, 3, 4, 5]
    y = [-2, 2, 0, 3]

    # Ниже программный код!!!

    print('/' * 24)
    print('Вычислим длины отрезков:')
    print('/' * 24)
    print()

    h2 = x[1] - x[0]
    h3 = x[2] - x[1]
    h4 = x[3] - x[2]

    print(f'h2 = {h2}')
    print(f'h3 = {h3}')
    print(f'h4 = {h4}\n')

    print('/' * 44)
    print('Вычислим правые части Yi и запишем систему ')
    print('/' * 44)
    print()

    Y2 = (y[2] - y[1]) / h3 - (y[1] - y[0]) / h2
    Y3 = (y[3] - y[2]) / h4 - (y[2] - y[1]) / h3

    print('Так как m1 = m4 = 0, сразу упростим систему как:\n')
    print('/')
    print(f'| {(h2 + h3) / 3}*m2 + {h3 / 6}*m3 = {Y2}')
    print(f'| {h3 / 6}*m2 + {(h3 + h4) / 3}*m3 = {Y3}')
    print('|\n')

    print('//////////////////////////////////////')
    print('Вычислим прогоночные коэффициенты:')
    print('//////////////////////////////////////\n')

    P2 = 0
    Q2 = 0
    P3 = (-h3) / (2 * (h2 + h3) + P2 * h2)
    Q3 = (6 * Y2 - h2 * Q2) / (2 * (h3 + h2) + P2 * h2)
    P4 = (-h4) / (2 * (h3 + h4) + P3 * h3)
    Q4 = (6 * Y3 - h3 * Q3) / (2 * (h4 + h3) + P3 * h3)

    print(f'P2 = {P2}')
    print(f'Q2 = {Q2}')
    print('------------------------------')
    print(f'P3 = {P3}')
    print(f'Q3 = {Q3}')
    print('------------------------------')
    print(f'P4 = {P4}')
    print(f'Q4 = {Q4}')

    print('\n//////////////////////////////////////')
    print('Вычислим mi:')
    print('//////////////////////////////////////\n')

    m1 = 0
    m3 = Q4
    m2 = P3 * m3 + P3
    # m2 = -11.6
    # m3 = 11.4
    m4 = 0

    print(f'm1 = {m1}')
    print(f'm2 = {m2}')
    print(f'm3 = {m3}')
    print(f'm4 = {m4}\n')

    print('//////////////////////////////////////////////////////')
    print('Вычислим значение сплайна в середине каждого отрезка:')
    print('//////////////////////////////////////////////////////\n')

    middle_1 = (x[0] + x[1]) / 2
    middle_2 = (x[1] + x[2]) / 2
    middle_3 = (x[2] + x[3]) / 2

    A_2 = m2 * ((middle_1 - x[0]) ** 3) / (6 * h2)
    B_2 = m1 * (x[1] - middle_1) ** 3 / 6 * h2
    C_2 = (y[1] - m2 * (h2 ** 2 / 6)) * ((middle_1 - x[0]) / h2)
    D_2 = (y[0] - m1 * (h2 ** 2 / 6)) * (x[1] - middle_1)

    print(f'S2({middle_1}) = {A_2 + B_2 + C_2 + D_2}')

    A_3 = m3 * ((middle_2 - x[1]) ** 3) / (6 * h3)
    B_3 = m2 * (x[2] - middle_2) ** 3 / 6 * h3
    C_3 = (y[2] - m3 * (h3 ** 2 / 6)) * ((middle_2 - x[1]) / h3)
    D_3 = (y[1] - m2 * (h3 ** 2 / 6)) * (x[2] - middle_2)

    print(f'S3({middle_2}) = {A_3 + B_3 + C_3 + D_3}')

    A_4 = m4 * ((middle_3 - x[2]) ** 3) / (6 * h4)
    B_4 = m3 * (x[3] - middle_3) ** 3 / 6 * h4
    C_4 = (y[3] - m4 * (h4 ** 2 / 6)) * ((middle_3 - x[2]) / h4)
    D_4 = (y[2] - m3 * (h4 ** 2 / 6)) * (x[3] - middle_3)

    print(f'S4({middle_3}) = {A_4 + B_4 + C_4 + D_4}')


except Exception as error:
    print(error)
input('\nНажмите "Enter" чтобы выйти...')