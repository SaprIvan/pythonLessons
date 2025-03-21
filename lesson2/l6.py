text = "3241-5672-3413-4524-5245-1236"
text = text[3::5]
result = text  # Итоговый результат должен быть записан в переменную result

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert result is not None, 'Итоговый результат должен быть записан в переменную result'
    expected_result = '123456'
    assert expected_result == result, f'Ожидается значение {expected_result}, а было {result}'

    # вывод в терминал результата
    print(f'Ваш пароль: {result}')