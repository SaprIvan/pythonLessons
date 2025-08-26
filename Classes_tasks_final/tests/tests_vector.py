from random import randint

from engine.geometry import Vector2
from engine.visual import Colors


def test_vector_initialize():
    x, y = randint(1, 100), randint(1, 100)
    vector = Vector2(x, y)
    assert hasattr(vector, '_Vector2__x') and hasattr(vector, '_Vector2__y'), 'Атрибуты "x" и "y" у класса Vector2 должны быть приватными'
    assert isinstance(getattr(Vector2, 'x'), property) and isinstance(getattr(Vector2, 'y'), property), 'Класс Vector2 должен содержать в себе свойства (property) "x" и "y"'
    assert vector.x == x, f'Проверьте, что свойство "x" возвращает значение приватного атрибута "x"'
    assert vector.y == y, f'Проверьте, что свойство "y" возвращает значение приватного атрибута "y"'


def run_vector_tests():
    print(f'{Colors.yellow}===Тестируем класс Vector2==={Colors.default}')
    test_vector_initialize()
    print(f'{Colors.green}+++Все тесты прошли, класс Vector2 реализован верно.+++{Colors.default}')
    print('====================')