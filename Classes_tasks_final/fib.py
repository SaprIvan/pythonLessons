def fib(count: int):
    prev, prev2 = 0,1
    for _ in range(count):
       curr = prev + prev2
       prev2 = prev
       prev = curr
       yield curr

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    count = 11
    gen = fib(count)
    fib_numbers = []
    try:
        for i in range(12):
            fib_numbers.append(next(gen))
        assert False, 'Генератор должен выбросить исключение StopIteration, когда мы вышли за границы последовательности.'
    except StopIteration:
        expected_fib_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        assert fib_numbers == expected_fib_numbers, f'Ожидалась последовательность Фибоначчи для 11 элементов:\n{expected_fib_numbers}, а была последовательность: {fib_numbers}'

    # вывод в терминал результата
    print(f'Все тесты прошли, генератор реализован верно.')