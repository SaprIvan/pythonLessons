
from dataclasses import dataclass, field
from time import sleep
from typing import Callable


@dataclass
class TextAnimation:
    states: list[any] = field(default_factory=list)
    attempts: int = 1
    interval: float = 3.0

    def play(self):
        animation_events.Start(self.states, self.attempts, self.interval)

class AnimationController:
    def __init__(self):
        animation_events.Start += self.animation

    def animation(self, states: list[any], attempts: int, interval: float):
        for attempt in range(attempts):
            for state in states:
                print(state, end="")
                sleep(interval)
                print("\r", end="")
        print(end="\n")



# Вспомогательные классы
class Event:
    def __init__(self):
        self.__handlers = []

    def __iadd__(self, predicate: Callable):
        self.__handlers.append(predicate)
        return self

    def __isub__(self, predicate: Callable):
        self.__handlers.remove(predicate)
        return self

    def __call__(self, *args, **kwargs):
        for handler in self.__handlers:
            handler(*args, **kwargs)
        return self


class AnimationEvents:
    def __init__(self):
        self.Start = Event()


animation_events = AnimationEvents()

# Место для вашей реализации


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    animator = AnimationController()
    dataclass_fields = getattr(TextAnimation, '__dataclass_fields__', None)
    dataclass_params = getattr(TextAnimation, '__dataclass_params__', None)
    assert dataclass_fields and dataclass_params, f'TextAnimation должен быть классом данных (@dataclass), а не обычным классом.'
    animation = TextAnimation()
    assert hasattr(animation, 'states'), 'Класс данных TextAnimation должен иметь поле states'
    assert hasattr(animation, 'attempts'), 'Класс данных TextAnimation должен иметь поле attempts'
    assert hasattr(animation, 'interval'), 'Класс данных TextAnimation должен иметь поле interval'
    assert animation.states == [], ('При создании экземпляра класса TextAnimation, поле states должно иметь пустой список.'
                                    ' Не забудьте использовать field(default_factory=коллекция) для значений по умолчанию для коллекций.')
    assert animation.interval == 3.0, f'При создании экземпляра класса TextAnimation, поле interval должно иметь значение 3.0, а было {animation.interval}'
    assert animation.attempts == 1, f'При создании экземпляра класса TextAnimation, поле attempts должно иметь значение 1, а было {animation.attempts}'

    animation = TextAnimation(states=['a', 'aa', 'aaa'], interval=0.0, attempts=1)
    from contextlib import redirect_stdout
    import io
    f = io.StringIO()
    with redirect_stdout(f):
        animation.play()
    actual_printed_str = f.getvalue()
    expected_printed_str = 'a\raa\raaa\r\n'
    assert actual_printed_str == expected_printed_str, \
        (f"Ожидалось, что при переданном в TextAnimation states=['a', 'aa', 'aaa'], метод animation класса AnimationController, "
         f"выведет на экран\n{expected_printed_str}, а было\n{actual_printed_str}")

    calls = []
    def play_mock(states, attempts, interval):
        calls.append((states, attempts, interval))
    animation_events.Start += play_mock
    animation = TextAnimation(states=[''], interval=0.1)
    animation.play()
    animation_events.Start -= play_mock
    expected = ([''], 1, 0.1,)
    assert calls == [expected], (f'Метод play у класса TextAnimation должен был вызвать '
                                 f'animation_events.Start с аргументами states, attempts, interval. Для states=[""], '
                                 f'interval=0.1 и attempts=1, ожидалось, что в событие передастся {expected}, а передалось {calls[0]}')
    # вывод в терминал результата
    print(f'Все тесты прошли, классы реализованы верно.')
    print('Проигрываем анимацию загрузки:')
    loader = [
        '[Загрузка] _____________________[0/100%]',
        '[Загрузка] ███__________________[17/100%]',
        '[Загрузка] █████████____________[35/100%]',
        '[Загрузка] ████████████_________[51/100%]',
        '[Загрузка] █████████████████____[80/100%]',
        '[Загрузка] █████████████████████[100/100%]',
    ]
    animation = TextAnimation(states=loader, attempts=1, interval=0.5)
    animation.play()