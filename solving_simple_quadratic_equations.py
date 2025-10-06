import math
import re


def regular() ->(list,list,list,list):
    left, right = converts_strings()
    quadratic_regular = r"[+-]?\d+x\^\d+"
    x_regular = r"[+-]?\d+x"
    nums_regular = r"[+-]?\d+"
    # находим квадраты
    quadratic_x_left = re.findall(quadratic_regular, left)
    # удаляем то, что нашли
    left = re.sub(quadratic_regular, '', left)
    # Находим просто х
    x_left = re.findall(x_regular, left)
    #Удаляем просто х
    left = re.sub(x_regular, '', left)
    #Находим числа без переменных
    num_left = re.findall(nums_regular, left)
    # находим квадраты
    quadratic_x_right = re.findall(quadratic_regular, right)
    # удаляем то, что нашли
    right = re.sub(quadratic_regular, '', right)
    #Находим просто х
    x_right = re.findall(x_regular, right)
    #Удаляем просто х
    right = re.sub(x_regular, '', right)
    # Находим числа без переменных
    num_right = re.findall(nums_regular, right)
    print(num_right)
    return quadratic_x_left, num_left, quadratic_x_right, num_right, x_left, x_right

def converts_strings() -> (str, str):
    equations = get_input().strip()
    left, right = equations.split("=")
    return left, right

def get_input() -> (str):
    print('Введите квадратное уравнение ')
    equations = '2x^2+12x-6 = 3x^2+16x-50'
    print(equations)
    return equations

def list_to_string() -> (str, str, str, str, str, str):
    quadratic_x_left, num_left, quadratic_x_right, num_right, x_left, x_right = regular()
    quadratic_x_left = ''.join(quadratic_x_left)
    quadratic_x_right = ''.join(quadratic_x_right)
    num_left = ''.join(num_left)
    print(num_left,'после строки')
    num_right = ''.join(num_right)
    x_left = ''.join(x_left)
    x_right = ''.join(x_right)
    return x_left, x_right, num_left, num_right, quadratic_x_left, quadratic_x_right

def string_to_int():
    x_left, x_right, num_left, num_right, quadratic_x_left, quadratic_x_right = list_to_string()
    print(num_left)
    print(num_right)
    re_coef = r'[+-]?\d+'
    a_left, a_right =(0,0)
    b_left, b_right = (0,0)
    match = re.match(re_coef,x_left)
    if match:
        b_left = int(match.group(0))
    match = re.match (re_coef,x_right)
    if match:
        b_right = int(match.group(0))
    match = re.match (re_coef,quadratic_x_left)
    if match:
        a_left = int(match.group(0))
    match = re.match (re_coef,quadratic_x_right)
    if match:
        a_right = int(match.group(0))
    c_left = int(num_left)
    c_right = int(num_right)
    return a_left, a_right, b_left, b_right, c_left, c_right

def solve():
    a_left, a_right, b_left, b_right, c_left, c_right = string_to_int()
    print(a_left, a_right, b_left, b_right, c_left, c_right)
    a = a_left + (a_right*-1)
    b = b_left + (b_right*-1)
    c = c_left + (c_right*-1)
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    x_1 = 0
    x_2 = 0
    d = b ** 2 - 4 * a * c
    if d > 0:
        print('Дискриминант больше 0 и равен = ', d)
        x_1 = (-b + (math.sqrt(d))) / (2 * a)
        x_2 = (-b - (math.sqrt(d))) / (2 * a)
    elif d == 0:
        print('Дискриминант равен нулю')
        x_1 = (-b) / (2 * a)
    elif d < 0:
        print('Дискриминант меньше нуля, следовательно в уравнении нет корней')
    return x_1, x_2
