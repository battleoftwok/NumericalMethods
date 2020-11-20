from python_code.methods.boundary_problem.final_diff import final_difference_method
from python_code.staf.sympy_init import *


# =========================================================
# Решение краевой задачи для ОДУ методом конечных разностей
# =========================================================


try:
    # задание
    expression = "2 * y'' - y' + 3 * y= -3 * x * x + 3 * x - 2"

    # отрезок. Оставить None для автоматического определения
    section_corners = None

    # количество отрезков
    number_of_sections = 4
    # шаг (имеет приоритет над количеством отрезков) None чтобы отключить
    step = .2

    # граничные условия
    boundaries_condition = [
        "-7 * y(-3) - 2 * y'(-3) = 6",
        "6 * y(-2) + 2 * y'(-2) = -2"
    ]
    # по необходимости можно дописать букву и соответствующее значение (ручной ввод приоритетней автоматического)
    boundaries = {}

    # ============================================================
    # ВНИМАНИЕ! Пугливым ниже не смотреть! Дальше программный код!
    # ATTENTION!  Not for timid people! Below is the program code!
    # ============================================================
    print('\n' + ' Решение краевой задачи для ОДУ методом конечных разностей '.center(100, '='))
    decision = final_difference_method(expression,
                                       boundaries_condition,
                                       boundaries,
                                       section_corners,
                                       number_of_sections,
                                       step,
                                       level_of_detail=2)
    for step in decision:
        for key in step:
            if 'Матрица' in key:
                step[key].console_display()
            elif isinstance(step[key], float):
                print(f'{key}: {round(step[key], 8)}')
            elif isinstance(step[key], list):
                print(f'{key}: {list(map(lambda val: round(float(val), 8), step[key]))}')
            else:
                print(f'{key}: {step[key]}')

except Exception as error:
    print(error)

input('\nНажмите "Enter" чтобы выйти...')
