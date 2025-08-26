from engine.animation import TextAnimation
from engine.events import animation_events
from engine.visual import DefaultAnimation, Colors


def test_text_animation_initialize():
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





def test_text_animation_play():
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


def test_animation():
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


def run_animation_tests():
    print(f'{Colors.yellow}===Тестируем классы TextAnimation и AnimationController==={Colors.default}')
    test_text_animation_initialize()
    test_text_animation_play()
    test_animation()
    print(f'{Colors.green}+++Все тесты прошли, классы TextAnimation и AnimationController реализованы верно.+++{Colors.default}')
    print('Проигрываем анимацию загрузки:')
    animation = TextAnimation(states=DefaultAnimation.loader, interval=0.5, attempts=1)
    animation.play()
    print('====================')