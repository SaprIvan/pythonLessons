ship_collection = {
    "1": {
        "ussr":["Орлан"],
        "usa":["Erie"],
        "japan":["Hashidate"],
        "germany":["Hermelin"]
    },
    "2": {
        "ussr":["НОВИК", "СТОРОЖЕВОЙ"],
        "usa":["CHESTER", "SAMPSON"],
        "japan":["CHIKUMA", "UMIKAZE"]

    },
}

tmp_nation = input()
tmp_lvl= input()

message = f'Найдены следующие корабли нации "{tmp_nation}" с уровнем {tmp_lvl}: {ship_collection.get(tmp_lvl).get(tmp_nation)}'

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert ship_collection is not None, 'Данные по кораблям должны хранится в переменной ship_collection'
    assert isinstance(ship_collection, dict) and isinstance(list(ship_collection.values())[0],
                                                            dict), 'Лучше всего, на данном этапе обучения, использовать словарь для хранения связанной информации.'
    import re

    pattern = r'Найдены следующие корабли нации "([\s\S]+)" с уровнем ([\s\S]+): ([\s\S]+).'
    match = re.findall(pattern, message)
    assert match, 'Проверь корректность сообщения.'

    # вывод в терминал результата
    print(message)