from schemas.equation import EquationInput
from solving_simple_quadratic_equations import extract_coef, solve

from fastapi import APIRouter

router = APIRouter(prefix="")

@router.post("/solve")
def answer_fast(input_data: EquationInput):
    equasion = input_data.equation  #тут получаем уравнение
    a,b,c = extract_coef(equasion)
    result = get_solve(a,b,c)
    return {"result": result}

def get_solve(a,b,c):
    x_1, x_2 = solve(a,b,c)
    if x_1 != 0 and x_2 != 0:
        otv = f'Корни уравнения равны {x_1} {x_2}'
        return otv
    elif x_1 != 0 and x_2 == 0:
        otv = f'Корень уравнения равен {x_1}'
        return otv
    elif x_1 == 0 and x_2 == 0:
        otv = 'Корней нет'
        return otv