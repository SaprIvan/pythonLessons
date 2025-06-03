numbers = [10, 2, 4, 5, 4, 3]

min_index = numbers.index(min(numbers))  # 1 (число 2)
max_index = numbers.index(max(numbers))  # 0 (число 10)

numbers[min_index] = min(numbers) * max(numbers)  # numbers[1] = 2*10 = 20
numbers[max_index] = min(numbers) * max(numbers)  # numbers[0] = 2*10 = 20

numbers.sort()
print(numbers)

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    expected_list = [3, 4, 4, 5, 20, 20]
    assert numbers == expected_list, f'Ожидался список:\n{expected_list}, а был\n{numbers}'

    # вывод в терминал результата
    print(f'Ваш отсортированный список: {numbers}')