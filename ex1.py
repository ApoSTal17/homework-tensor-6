
# Задание 1

import ast

def code_byte(str_list):
    """Выполняет кодирование списка строк в список байт-кодов

    args:
        str_list - список строк
    returns:
        список байт кодов строк
    """
    byte_list = [i.encode('utf-8') for i in str_list]
    return byte_list

def decode_byte(byte_list):
    """Выполняет декодирование списка байт-кодов в список строк

    args:
        byte_list - список байт-кодов
    returns:
        список строк из списка байт-кодов
    """
    str_list = [i.decode('utf-8') for i in byte_list]
    return str_list


message = '''Введите режим работы программы:
1 - Кодирование списка строк в байт-код
2 - Декодирование байт-кода в список строк
q - выход
>>> '''

while True:
    s = input(message)
    match s:
        case '1':
            coded_seque = code_byte(list(map(str, input('Введите список строк через пробел: ').split())))
            decoded_seque = decode_byte(coded_seque)
            print(f'Список строк в виде байт-кода: {coded_seque}')
            print(f'Обратное преобразование (проверка): {decoded_seque}')
        case '2':
            try:
                message2 = 'Введите список байт-кодов через запятую и пробел, без крайних скобок: '
                str_list = list(map(str, input(message2).split(', ')))
                bytes_list = [ast.literal_eval(i) for i in str_list]
                print(f'Введенный список байтов: {bytes_list}')
                decoded_seque = decode_byte(bytes_list)
                print(f'Декодированный список строк: {decoded_seque}')
            except ValueError:
                print('Неверный формат ввода.')
        case 'q':
            print('До свидания!')
            break
        case _:
            print('Неправильный ввод!')

# Пояснение: стандартный конструктор bytes видимо не умеет преобразовать str с байтовым значением
# внутри в байты, он делает второе кодирование. Библиотека ast приводит такие строки к bytes типу.