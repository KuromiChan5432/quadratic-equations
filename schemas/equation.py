from pydantic import BaseModel


class EquationInput(BaseModel):    #тут мы делаем так, чтобы сайтик понял, что пользователь вводит строку
    equation: str