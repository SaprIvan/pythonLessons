


def get_even_numbers(count):
     digits = [d * 2 for d in range(1,count+1)]
     return digits


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    result = get_even_numbers(1)
    assert result and isinstance(result, list), 'Проверь, что функция get_even_numbers возвращает список элементов'
    expected = [2, 4, 6, 8, 10, 12]
    result = get_even_numbers(6)
    assert get_even_numbers(
        6) == expected, f'В качестве результата выполнения функции для аргумента 6, ожидался список элементов\n{expected}, а был\n{result}'
    expected = [2, 4, 6, 8]
    result = get_even_numbers(4)
    assert get_even_numbers(
        4) == expected, f'В качестве результата выполнения функции для аргумента 6, ожидался список элементов\n{expected}, а был\n{result}'

    # вывод в терминал результата
    print(f'Результат работы программы: \n{result}')