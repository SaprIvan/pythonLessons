first_sign = input('Введите первый символ: ')
second_sign = input('Введите второй символ: ')

# место для вашей реализации
if(first_sign > second_sign):
    greatest_sign = first_sign
elif(second_sign > first_sign):
    greatest_sign = second_sign

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert greatest_sign is not None, 'Результат сравнения нужно положить в переменную  greatest_sign.'
    assert isinstance(first_sign, str) and isinstance(second_sign,
                                                      str), 'Переменные first_sign и second_sign должны иметь строковый тип данных'
    assert greatest_sign == max(first_sign,
                                second_sign), 'Неверный алгоритм определения лексикографически большего символа. Подумай еще.'

    # вывод в терминал результата
    print(greatest_sign)