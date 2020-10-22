from python_code.methods.interpol.cspline import cspline


# ===============================
# Интерполяция сплайнами c-spline
# ===============================


x_list = [0, 1, 3, 6, 10]  # значения строки x
y_list = [2, 4, 6, 7,  3]  # значения строки y


# ============================================================
# ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
# ATTENTION!  Not for timid people! Below is the program code!
# ============================================================


try:
    decision = cspline(x_list, y_list, level_of_detail=2)
    for step in decision:
        step_info = ''
        for info in step:
            if 'Матрица' in info:
                print(f'{info}:')
                step[info].console_display()
            elif 'Python' in info:
                function = step[info]
            else:
                if isinstance(step[info], (tuple, list)):
                    list_str = ' Список многочленов '.center(100, '=') + '\n'
                    for pol in step[info]:
                        list_str += str(pol) + '\n'
                    step_info += list_str
                elif isinstance(step[info], float):
                    step_info += f'{info}: {round(step[info], 8)}\n'
                else:
                    step_info += f'{info}: {step[info]}\n'
        print(step_info)

    print(" Значения в серединах отрезков ".center(100, '='))
    section_centers = [x_list[no] + (x_list[no + 1] - x_list[no]) / 2 for no in range(len(x_list) - 1)]
    for center in section_centers:
        print(f'S({center}) = {function(center)}')
    # section_centers = x_list
    # for center in section_centers:
    #     print(f'S({center}) = {function(center)}')

except Exception as error:
    print(error)

input('\nНажмите "Enter" чтобы выйти...')