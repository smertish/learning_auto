def multiply(a, b):
    result = a * b
    print(f'Результатом умножения {a} и {b} будет {result}')


def div(a, b):
    try:
        result = a / b
        print(f'Результатом деления {a} на {b} будет {result}')
    except ZeroDivisionError:
        print('На 0 делить нельзя')


def summ(a, b):
    result = a + b
    print(f'Результатом сложения {a} и {b} будет {result}')


def sub(a, b):
    result = a - b
    print(f'Разность чисел {a} и {b} равна {result}')
