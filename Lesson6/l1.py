class Counter:
    count = 0

counter = Counter()

#counter = None
counter.count = 6


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert isinstance(counter, Counter), 'Переменная counter должна иметь тип Counter'
    assert hasattr(counter, 'count'), 'Класс Counter должен содержать атрибут count'
    assert 'count' in Counter.__dict__, 'Атрибут класса Counter должен быть статическим, а не динамическим.'

    # вывод в терминал результата
    print(f'Твой класс {counter.__class__.__name__} содержит атрибут со значением {counter.count}')