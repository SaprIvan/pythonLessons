numbers = [10, 2, 4, 5, 4, 3]


min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
mult = numbers[min_index]*numbers[max_index]

numbers[min_index] = mult
numbers[max_index] = mult
numbers.sort()

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    expected_list = [3, 4, 4, 5, 20, 20]
    assert numbers == expected_list, f'Ожидался список:\n{expected_list}, а был\n{numbers}'

    # вывод в терминал результата
    print(f'Ваш отсортированный список: {numbers}')