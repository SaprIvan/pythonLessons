result = [i for i in range (1,8,2)]

# Оптимизируйте нижеприведенный код, заменив цикл на Comprehension


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert result, 'Результат работы программы должен быть записан в переменную result'
    expected_list = [1, 3, 5, 7]
    assert result == expected_list, f'Ожидалось, что в переменной result будет\n{expected_list}, а был\n{result}'

    # вывод в терминал результата
    print(f'Результат работы программы: \n{result}')