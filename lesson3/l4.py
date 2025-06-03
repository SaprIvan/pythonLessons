# Место для вашей реализации

ship_collection = {
    "1": [
        "Орлан",
        "ERIE",
        "HASHIDATE",
        "HERMELIN",
    ],
    "2": [
        "НОВИК",
        "СТОРОЖЕВОЙ",
        "DRESDEN",
        "V-25",
        "CHESTER",

    ],
    "3": [
        "КНЯЗЬ СУВОРОВ",
        "БОГАТЫРЬ",
        "ДЕРЗКИЙ",
        "S. CAROLINA",
    ],
}

ship_lvl = input()

message = f'Найдены следующие корабли с уровнем {ship_lvl}: {ship_collection[ship_lvl]}\n'
print(message)

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert ship_collection is not None, 'Данные по кораблям должны хранится в переменной ship_collection'
    assert isinstance(ship_collection,
                      dict), 'Лучше всего, на данном этапе обучения, использовать словарь для хранения связанной информации.'
    import re

    pattern = r'Найдены следующие корабли с уровнем ([\s\S]+): ([\s\S]+).'
    match = re.findall(pattern, message)
    assert match, 'Проверь корректность сообщения.'

    # вывод в терминал результата
    print(message)