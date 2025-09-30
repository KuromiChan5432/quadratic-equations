import math

def normalize() -> (int, int, int):
    a,b,c,e,coef = get_input()
    if e != 0:
        c+=e*(-1)
    b+=coef*(-1)
    return a,b,c


def get_input() -> (int,int,int,int,int):
    coef = None
    print('введите коэффициенты для квадратного уравнения')
    print('коэффициент а = ')
    a = int(input())
    print('коэффициент b =')
    b = int(input())
    print('коэффициент c = ')
    c = int(input())
    print('введите число после равно')
    e = int(input())
    print('После равно есть переменная x? введите ответ "Да"/"Нет"')
    ans = input()
    if ans == 'Да':
        print('Введите коэффициент переменной')
        coef = int(input())
    return a,b,c,e,coef


def solve():
    x_1 = 0
    x_2 = 0
    a,b,c = normalize()
    d = b ** 2 - 4 * a * c
    if d > 0:
        print('Дискриминант больше 0 и равен = ', d)
        x_1 = (-b + (math.sqrt(d))) // (2 * a)
        x_2 = (-b - (math.sqrt(d))) // (2 * a)
    elif d == 0:
        print('Дискриминант равен нулю')
        x_1 = (-b) / (2 * a)
    elif d < 0:
        print('Дискриминант меньше нуля, следовательно в уравнении нет корней')
    return x_1, x_2
