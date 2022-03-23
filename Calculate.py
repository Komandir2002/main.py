print('~Калькулятор~')
while 1:
    try:
        number_1 = int(input('Введите первое число:'))
        number_2 = int(input('Введите второе число:'))
        comand = input('1 - Сложение \n2 - Вычитание'
                       ' \n3 - Деление \n4 - Умножение\n0 - Выход!\nВыберите операцию:')
        if comand == '1':
            result = number_1 + number_2
            print(f'Результат сложения: {result}')
        elif comand == '2':
            result = number_1 - number_2
            print(f'Результат вычитание: {result}')
        elif comand == '3':
            result = number_1 / number_2
            print(f'Результат деление: {result}')
        elif comand == '4':
            result = number_1 * number_2
            print(f'Результат умножения: {result}')
        elif comand == '0':
            break
        else:
            print('Нету такой операции в команде!')
    except ValueError:
        print('Введите только числа!')
    except ZeroDivisionError:
        print('Разделить на ноль нельзя!')
    except Exception:
        print('Что-то пошло не так!')




