from solving_simple_quadratic_equations import solve

if __name__ == '__main__':
    x_1, x_2 = solve()
    if x_1 != 0 and x_2 != 0:
        print(f'Корни уравнения равны {x_1} {x_2}')
    elif x_1 != 0 and x_2 == 0:
        print(f'Корень уравнения равен {x_1}')
    elif x_1 == 0 and x_2 == 0:
        print('Корней нет')
