import math

detection_range = 2

circle_vision = math.floor(math.pi * detection_range**2)

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert circle_vision is not None, 'circle_vision не должен быть None'
    assert detection_range is not None, 'detection_range не должен быть None'
    assert circle_vision == 12, 'Подумай еще над решением. Огруглять нужно но наименьшего целого'

    # вывод в терминал результата
    print(circle_vision)