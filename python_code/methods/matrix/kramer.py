def kramer_method(matrix, free_column, level_of_detail=3):
    def det(mat):
        return matrix.determinant.auto_det(mat)

    def calc_col_det(mat, free, col_no_):
        mat = mat.copy()
        mat.pop_column(col_no_)
        mat.insert_column(col_no_, free)
        det_ = det(mat)
        if level_of_detail < 3:
            answer.update({"Матрица с замененным столбцом": mat, "Определитель": det_})
        return det_

    answer = {}
    matrix = matrix.copy()
    main_det = det(matrix)
    if level_of_detail < 3:
        answer.update({'Этап': 'Получены данные', 'Матрица': matrix, 'Общий определитель': main_det})
        yield answer
        answer.pop('Общий определитель', None)
        answer.pop('Этап', None)
        answer.pop('Матрица', None)
    if main_det == 0:
        raise ArithmeticError("Метод крамера не работает с матрицами, определитель которых равен нулю")

    solution = []
    for col_no in range(matrix.columns):
        if level_of_detail < 3:
            answer.update({"Номер столбца замены": col_no})
        solution.append(calc_col_det(matrix, free_column, col_no) / main_det)
        if level_of_detail < 2:
            answer.update({"Решение": f'X{col_no + 1} = det(matrix_{col_no}) / det(matrix) = '
                                      f'{answer["Определитель"]} / {main_det} = {answer["Определитель"] / main_det}'})
        if level_of_detail < 3:
            yield answer
    answer.pop("Номер столбца замены", None)
    answer.pop("Матрица с замененным столбцом", None)
    answer.pop("Определитель", None)
    answer.pop("Решение", None)
    if level_of_detail < 4:
        answer.update({"Решение": solution})
    yield answer