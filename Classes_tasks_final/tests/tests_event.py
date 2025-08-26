from engine.events import Event
from engine.visual import Colors


def test_initialize():
    ev = Event()
    assert hasattr(ev, '_Event__handlers'), f'Класс Event должен иметь динамический приватный атрибут handlers.'
    assert isinstance(getattr(ev, '_Event__handlers'), list), f'Приватный атрибут handlers, класса Event, должен иметь тип list.'
    assert not getattr(ev, '_Event__handlers'), f'Список из приватного атрибута handlers, класса Event, должен быть пустым при создании экземпляра класса.'


def test_add_sub_handler():
    ev = Event()

    def func():
        pass

    ev += func
    assert len(getattr(ev, '_Event__handlers')) == 1, f'После подписка, объект функции не добавился в приватный атрибут handlers, класса Event.'
    ev -= func
    assert not getattr(ev, '_Event__handlers'), f'После отписки, объект функции не удалился из приватного атрибута handlers, класса Event.'
    # вывод в терминал результата


def test_call():
    ev = Event()
    calls = []

    def func_1(value):
        calls.append(value.copy())

    def func_2(value):
        value.reverse()
        calls.append(value)

    ev += func_1
    ev += func_2

    expected_value_1, expected_value_2 = 'value_1', 'value_2'
    ev([expected_value_1, expected_value_2])
    assert calls == [[expected_value_1, expected_value_2], [expected_value_2, expected_value_1]], \
        f'Метод __call__ должен проходится по каждому элементу __handlers и вызывать его с аркументами *args, **kwargs.'

def run_event_tests():
    print(f'{Colors.yellow}===Тестируем класс Event==={Colors.default}')
    test_initialize()
    test_add_sub_handler()
    test_call()
    print(f'{Colors.green}+++Все тесты прошли, класс Event реализован верно.+++{Colors.default}')
    print('====================')