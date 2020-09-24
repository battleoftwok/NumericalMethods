from python_code.methods.equation.lobachevsky import lobachevsky_solve as lobachevsky_method
from python_code.methods.equation.dichotomy import dichotomy
from python_code.methods.equation.hords import hords
from python_code.methods.equation.iterations import iterations
from python_code.methods.equation.tangent_newton import tangent_newton


def auto_solve(odds, await_delta_order=8, *args, **kwargs):
    try:
        decision = lobachevsky_method(odds, await_delta_order=await_delta_order, *args, **kwargs)
        solution = []
        for step in decision:
            solution = step.get('Решение')
        return solution
    except OverflowError:
        return auto_solve(odds, await_delta_order=await_delta_order - 1, *args, **kwargs)
