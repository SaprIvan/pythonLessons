number = 10

# Место для вашего решения
result = 1
for i in range(1,number+1):
    result *= i

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    expected_factorial = 3628800
    assert result == expected_factorial, f'Ожидался результат {expected_factorial}, а был {result}'

    # вывод в терминал результата
    print(result)