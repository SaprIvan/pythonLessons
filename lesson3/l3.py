dictionary = {
    'Иван Иванов': ['WWSD-1', 'WWSD-2', 'WWSD-3'],
    'Петр Петров': ['WWSD-5'],
    'Сергей Сергеев': ['WWSD-4', 'WWSD-6'],
    'Антон Антонов': []
}

tmp_name = input()
tasks = dictionary.get(tmp_name)
message = f'Выбран сотрудник: {tmp_name}. Текущие задачи: {tasks}.'

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert message is not None, 'В переменной message должно хранится сообщение о задачах введенного сотрудника.'
    import re

    if message != 'Введенное имя и фамилия не найдены.':
        pattern = r'Выбран сотрудник: ([\s\S]+). Текущие задачи: ([\s\S]+).'
        match = re.findall(pattern, message)
        assert match, 'Проверь корректность сообщения.'
        assert dictionary.get(match[0][0]) is not None, 'Сотрудник из сообщения отсутствует в словаре.'
        assert str(dictionary.get(match[0][0])) == match[0][
            1], 'Задачи из сообщения не совпадают с задачами сотрудника в словаре.'
    else:
        print(
            'Вы проверили ветвление, когда имя и фамилия не найдены. Теперь проверьте ветвление с валидными именем и фамилией.')
    # вывод в терминал результата
    print(message)