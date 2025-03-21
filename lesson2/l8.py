# Место для вашей реализации
message = input()


format_message = ''

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert format_message, 'Переменная format_message не должна быть пустой'
    import re

    pattern = r'(\+[-]+\+)\n(\|[\s\S]+\|)\n(\+[-]+\+)'
    match_result = re.findall(pattern, format_message)
    assert match_result, f'Проверь корректность символов в сообщении. Твоё сообщение:\n{format_message}'
    _message = match_result[0][1].replace('|', '')
    assert _message.startswith(' ') and _message.endswith(' '), 'Не забудь про пробелы с краёв. Сейчас их нет.'
    horizont_signs_count = len(match_result[0][0].replace('+', ''))
    expected_signs_count = len(message) + 2
    assert horizont_signs_count == expected_signs_count, f'Количество символов "-" сверху: {horizont_signs_count}. Ожидалось, что будет: {expected_signs_count}. Не забудь про пробелы с краёв. Твоё сообщение:\n{format_message}'
    horizont_signs_count = len(match_result[0][2].replace('+', ''))
    assert horizont_signs_count == expected_signs_count, f'Количество символов "-" снизу: {horizont_signs_count}. Ожидалось, что будет: {expected_signs_count}. Не забудь про пробелы с краёв. Твоё сообщение:\n{format_message}'

    # вывод в терминал результата
    print(format_message)