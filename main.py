from any_func import func

value_to_stop = 1
while value_to_stop == 1:
    try:
        num_1 = int(input('\nВведите первое число: '))
    except ValueError:
        print("Введено не числовое значение. Программа умерла")
        break
    try:
        num_2 = int(input('Введите второе число: '))
    except ValueError:
        print("Введено не числовое значение. Программа умерла")
        break
    print(
        f'\nВведите одну из арифметических операций, которую хотите провести между числом {num_1} и {num_2}. Для вызова'
        f' меню доступных арифметических операций между числами введите команду "/help" и нажмите "Enter"')
    while True:
        operation = input()
        if operation == "/help":
            print("+, -, *, /")
        elif operation == "+":
            func.summ(num_1, num_2)
            break
        elif operation == "-":
            func.sub(num_1, num_2)
            break
        elif operation == "*":
            func.multiply(num_1, num_2)
            break
        elif operation == "/":
            func.div(num_1, num_2)
            break
        else:
            print('Введено некорректное значение. Повторите ввод')
    print("Для выхода из программы введите любое значение. Для повтора введите '1'")
    value_to_stop = int(input())
