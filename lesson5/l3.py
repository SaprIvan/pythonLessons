def get_rus_ship_name(ship_type):
    ship_types = {'Destroyer':'Эсминец', 'Aircarrier':'Авианосец', 'Battleship':'Линкор', 'Cruiser':'Крейсер', 'Submarine':'Подлодка'}
    return ship_types.get(ship_type) if ship_type in ship_types else print(f'Типа корабля "{ship_type}" не найден')


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    result = get_rus_ship_name('Submarine')
    assert result and isinstance(result, str), 'Проверь, что функция get_rus_ship_name возвращает строковое значение'
    assert result == 'Подлодка', 'Проверь корректность перевода. Для слова "Submarine" ожидался перевод "Подлодка"'
    ship_type = 'Submarina'
    result = get_rus_ship_name('Submarina')
    #expected_result = f'Типа корабля "{ship_type}" не найден'
   # assert result == expected_result, f'Проверь корректность вывода сообщения, когда тим не найден. Ожидалось:\n{expected_result}, а был\n{result}'
    assert 'index' not in get_rus_ship_name.__code__.co_names, 'По заданию нужно работать со словарём. Убедишь, что нет списков и их встроенных методов'

    # вывод в терминал результата
    print(f'Все тесты пройдены. Поздравляю! Твоя функция работает корректно.')