import math
import re

def extract_regular(regular_expr: str,  string: str) -> (list, str):
    extracted = re.findall(regular_expr, string)
    new_string = re.sub(regular_expr, '', string)
    return extracted, new_string


def regular() ->(list,list,list,list):
    left, right = converts_strings()
    quadratic_regular = r"[+-]?\d*x\^\d+"
    x_regular = r"[+-]?\d+x"
    nums_regular = r"[+-]?\d+"

    answer = []

    for part in [left, right]:
        # находим квадраты
        # и удаляем то, что нашли
        quadratic_x, part = extract_regular(quadratic_regular, part)
        # Находим просто х и удаляем
        x, part = extract_regular(x_regular, part)
        #Находим числа без переменных
        num = re.findall(nums_regular, part)
        answer.extend([quadratic_x, x, num])
    return answer

def converts_strings() -> (str, str):
    equations = get_input().strip()
    left, right = equations.split("=")
    reg_c = r'[+-]?\[^^]\d+[^a-zA-Z]'
    print(re.search(reg_c, left))
    if re.findall(reg_c, left) == []:
        left += '+0'
        print(re.findall(reg_c, left))
        return left, right
    else:
        return left, right

def get_input() -> (str):
    # global stored_equation
    # stored_equation = equation
    print('введите уравенение')
    stored_equation = input()
    return stored_equation

def summarize() -> (int,int,int):
    quadratic_x_left, x_left, num_left, quadratic_x_right, x_right, num_right = regular()
    quadratic_x = []
    x = []
    for i in quadratic_x_left:
        coef = i.split("x")[0]
        if coef == "":
            coef = "1"
            quadratic_x.append(int(coef))
        elif coef == "-":
            coef = "-1"
            quadratic_x.append(int(coef))
        else:
            quadratic_x.append(int(coef))
    for i in quadratic_x_right:
        coef = i.split("x")[0]
        if coef == "":
            coef = "1"
            quadratic_x.append(int(coef))
        elif coef == "-":
            coef = "-1"
            quadratic_x.append(int(coef))
        else:
            quadratic_x.append(int(coef))
    for i in x_left:
        coef = i.split("x")[0]
        if coef == "":
            coef = "1"
            x.append(int(coef))
        elif coef == "-":
            coef = "-1"
            x.append(int(coef))
        else:
            x.append(int(coef))
    for i in x_right:
        coef = i.split("x")[0]
        if coef == "":
            coef = "1"
            x.append(int(coef))
        elif coef == "-":
            coef = "-1"
            x.append(int(coef))
        else:
            x.append(int(coef))
    for i in num_left:
        if len(num_left) == 0:
            coef = "0"
            coef += coef.join(i)
            num_left.append(int(coef))
    for i in num_right:
        if len(num_right) == 0:
            coef = "0"
            coef += coef.join(i)
            num_right.append(int(coef))
    sum_quadro = sum(quadratic_x)
    sum_x = sum(x)
    print(num_left, num_right)
    num_left_int = int(num_left[0])
    num_right_int = int(num_right[0])
    num_sum = num_left_int+num_right_int
    num_sum = int(num_sum)
    return sum_quadro,sum_x, num_sum
    # пройтись по каждому из этих списков
    # для каждого элемента списка выделить коэффициент слева от x (через .split('x'))
    # преобразовать коэффициент к float
    # сложить все значения элементов этого списка

    # в итоге вернуть посчитанные коэф. нормализованного уравнения (ax^2 + bx + c = 0)

def solve():
    sum_quadro,sum_x, num_sum = summarize()
    a = sum_quadro
    b = sum_x
    c = num_sum
    x_1 = 0
    x_2 = 0
    d = b ** 2 - 4 * a * c
    if d > 0:
        print('Дискриминант больше 0 и равен = ', d)
        x_1 = (-b - (math.sqrt(d))) / (2 * a)
        x_2 = (-b + (math.sqrt(d))) / (2 * a)
        x_1 = round(x_1, 2)
        x_2 = round(x_2,2)
    elif d == 0:
        print('Дискриминант равен нулю')
        x_1 = (-b) / (2 * a)
        x_1 = round(x_1,2)
    elif d < 0:
        print('Дискриминант меньше нуля, следовательно в уравнении нет корней')
    return x_1, x_2
