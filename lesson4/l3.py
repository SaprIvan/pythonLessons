text = '''
Знает лишь время,
Сколько дорог мне пройти,
Чтоб достичь счастья.

Падающий цветок
Вернулся вдруг на ветку
Оказалось: бабочка!

О, с какой тоской
Птица из клетки глядит
На полет мотылька!
'''
# Место для вашей реализации
poems = []
tmp = []
tmp.append(text.split("."))

for i in range(len(text)):
    poem = text.split(".")
    if text[i] == "." and text[i+1] == "\n":
        continue
print(len(poems))


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert poems, 'Результат парсинга должен быть в переменной poems'
    assert len(poems) == 3, f'Переменная poems должна содержать в себе 3 элемента. Сейчас в poems лежит:\n{poems}'
    assert not [item for item in poems if not isinstance(item,
                                                         list)], f'Все элементы списка poems должны иметь тип list. Сейчас в poems лежит:\n{poems}'
    assert not [item for item in poems if
                not len(item) == 3], f'Все элементы списка poems должны иметь длину 3. Сейчас в poems лежит:\n{poems}'
    # вывод в терминал результата
    print(f'Результат работы программы:\n{poems}')