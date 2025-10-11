from solving_simple_quadratic_equations import solve, get_input

# from fastapi import FastAPI
#
# from pydantic import BaseModel
#
# app = FastAPI()
#
# @app.get("/")
# def root():       #основной сайт, если никуда не переходить
#     return {"message": "Тут ничего нет"}
#
# class EquationInput(BaseModel):        #тут мы делаем так, чтобы сайтик понял, что пользователь вводит строку
#     equation: str
#
#
# @app.post("/solve")
# def answer_Fast(input_data: EquationInput):
#     equasion = get_input(input_data.equation)  #тут получаем уравнение
#     result = get_solve()
#     return {"result": result}


def get_solve():
    if __name__ == '__main__':
        x_1, x_2 = solve()
        if x_1 != 0 and x_2 != 0:
            otv = f'Корни уравнения равны {x_1} {x_2}'
            return otv
        elif x_1 != 0 and x_2 == 0:
            otv = f'Корень уравнения равен {x_1}'
            return otv
        elif x_1 == 0 and x_2 == 0:
            otv = 'Корней нет'
            return otv