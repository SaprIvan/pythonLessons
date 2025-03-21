promocode = 'SPB:CLAKS-21SKA-ASD34-78-5KET2'

# Место для вашего решения. Не забывайте про дополнительный отступ внутри функции.
region = promocode[0:3]
code = promocode[4::]
code = code.replace("-","")
region_code = code[-7:-5]

message = f"Регион: {region}; Код региона: {region_code}; Промокод: {code}"

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert region is not None and code is not None and region_code is not None, 'Проверь, что из промокода достаются корректно промокод, код региона и регион'
    expected_length = 22
    actual_length = len(code)
    assert actual_length == expected_length, f'Промокод должен иметь длину {expected_length}, а имеет {actual_length}'
    expected_length = 2
    actual_length = len(region_code)
    assert actual_length == expected_length, f'Код региона должен иметь длину {expected_length}, а имеет {actual_length}'
    expected_length = 3
    actual_length = len(region)
    assert actual_length == expected_length, f'Название региона должно иметь длину {expected_length}, а имеет {actual_length}'
    expected_message = 'Регион: SPB; Код региона: 78; Промокод: CLAKS21SKAASD34785KET2'
    assert message == expected_message, f'Ожидалось сообщение\n{expected_message}, а было\n{message}'
    # вывод в терминал результата
    print(message)