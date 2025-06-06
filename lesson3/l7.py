first_app_users = ['SSSR1-WW-100500', 'SSSR1-WW-100500', 'SSSR1-WW-100501', 'SSSR1-WW-100505', 'SSSR1-WW-100505',
                   'SSSR1-WW-100502', 'SSSR1-WW-100500', 'SSSR1-WW-1005001', 'SSSR1-WW-100501', 'SSSR1-WW-100502',
                   'SSSR1-WW-100511', 'SSSR1-WW-100500', 'SSSR1-WW-100505']
second_app_users = ['SSSR1-WW-100510', 'SSSR1-WW-100511', 'SSSR1-WW-100521', 'SSSR1-WW-100515', 'SSSR1-WW-100502',
                    'SSSR1-WW-100500', 'SSSR1-WW-100521', 'SSSR1-WW-1005011', 'SSSR1-WW-100505', 'SSSR1-WW-100522',
                    'SSSR1-WW-100521', 'SSSR1-WW-100520', 'SSSR1-WW-100525']


result = set(first_app_users) & set(second_app_users)


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert first_app_users is not None and second_app_users is not None and result is not None, 'Переменные first_app_users, second_app_users и result не должны быть None'
    assert isinstance(result,
                      (set, list)), f'Тип данных переменной result должен быть set или list, а был {type(result)}'
    assert len(result) == 4, 'Количество одинаковых пользователей другое. Подумай еще над решением.'

    # вывод в терминал результата
    print(result)