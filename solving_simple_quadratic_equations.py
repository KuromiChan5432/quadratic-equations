import math

x1 = 0
x2 = 0
newrav = 0
print('введите коэффициенты для квадратного уравнения')
print('коэффициент а = ')
a = int(input())
print('коэффициент b =')
b = int(input())
print('коэффициент c = ')
c = int(input())
print('введите число после равно')
rav = int(input())
if rav != 0:
    newrav += rav * (-1)
    c = c + newrav
D = b ** 2 - 4 * a * c
if D > 0:
    print('Дискриминант больше 0 и равен = ', D)
    x1 = (-b + (math.sqrt(D))) // (2 * a)
    x2 = (-b - (math.sqrt(D))) // (2 * a)
    print('Корни уравнения равны = ', x1, ' ', x2)
elif D == 0:
    print('Дискриминант равен нулю')
    x1 = (-b) / (2 * a)
    print(x1)
elif D < 0:
    print('Дискриминант меньше нуля, следовательно в уравнении нет корней')
