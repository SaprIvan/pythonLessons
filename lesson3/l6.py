data_from_db = ['SSSR1-WW-100500', 'SSSR1-WW-100500', 'SSSR1-WW-100501', 'SSSR1-WW-100505', 'SSSR1-WW-100505',
                'SSSR1-WW-100502', 'SSSR1-WW-100500', 'SSSR1-WW-1005001', 'SSSR1-WW-100501', 'SSSR1-WW-100502',
                'SSSR1-WW-100511', 'SSSR1-WW-100500', 'SSSR1-WW-100505']

data_from_db = set(data_from_db)

result = len(data_from_db)

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert data_from_db is not None and result is not None, 'Переменные data_from_db и result не должны быть None'
    assert isinstance(result, int), f'Тип данных переменной result должен быть int, а был {type(result)}'
    assert result == 6, 'Количество уникальных пользователей другое. Подумай еще над решением.'

    # вывод в терминал результата
    print(result)