

class Counter:
    count = 0

    def increment(self):
        self.count+=1

counter = Counter()
counter.count = 0
counter.increment()


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert counter.count == 1, f'Метод increment должен увеличивать значение count на 1, а увеличил на {counter.count - Counter.count}'
    assert isinstance(counter, Counter), 'Переменная counter должна иметь тип Counter'
    assert hasattr(counter, 'count') and hasattr(counter, 'increment'), 'Класс Counter должен содержать атрибут count и метод increment'
    assert 'count' in Counter.__dict__, 'Атрибут класса Counter должен быть статическим, а не динамическим.'

    # вывод в терминал результата
    print(f'Твой класс {counter.__class__.__name__} содержит атрибут со значением {counter.count}')