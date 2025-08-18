class Vector2:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    from random import randint
    x, y = randint(1, 100), randint(1, 100)
    vector = Vector2(x, y)
    assert hasattr(vector, '_Vector2__x') and hasattr(vector, '_Vector2__y'), 'Атрибуты "x" и "y" у класса Vector2 должны быть приватными'
    assert isinstance(getattr(Vector2, 'x'), property) and isinstance(getattr(Vector2, 'y'), property), 'Класс Vector2 должен содержать в себе свойства (property) "x" и "y"'
    assert vector.x == x, f'Проверьте, что свойство "x" возвращает значение приватного атрибута "x"'
    assert vector.y == y, f'Проверьте, что свойство "y" возвращает значение приватного атрибута "y"'

    # вывод в терминал результата
    print(f'Все тесты прошли, класс реализован верно.')