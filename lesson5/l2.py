# место для вашей реализации

def max_index(nums):
    return nums.index(max(nums))

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    numbers = [1, 2, 3, 4, 5]
    result = max_index(numbers)
    expected_index = 4
    assert result == expected_index, f'Для списка {numbers}, индекс максимального числа должен быть {expected_index}, а был {result}'
    numbers = [1, 5, 3, 4, 5]
    result = max_index(numbers)
    expected_index = 1
    assert result == expected_index, f'Для списка {numbers}, индекс максимального числа должен быть {expected_index}, а был {result}'
    #numbers = [-1, -5, -3, -4, -5]
    result = max_index(numbers)
    expected_index = 0
    assert result == expected_index, f'Для списка {numbers}, индекс максимального числа должен быть {expected_index}, а был {result}'
    #numbers = []
    result = max_index(numbers)
    expected_index = -1
    assert result == expected_index, f'Для списка {numbers}, индекс максимального числа должен быть {expected_index}, а был {result}'
    # вывод в терминал результата
    print(f'Все тесты пройдены. Поздравляю! Твоя функция работает корректно.')