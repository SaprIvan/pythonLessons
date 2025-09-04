# место для вашей реализации
def logger(func):
    def wrapper(self, *args, **kwargs):
        print(f'[{func.__name__}] Вызов функции. Аргументы: ({list(args)})')
        print(f'[{func.__name__}] Результат: { func(self, *args, **kwargs)}')
    return wrapper



# Вспомогательный класс
class Player:
    def __init__(self, name: str):
        self.name = name
    @logger
    def move(self, x, y):
        return f'Персонаж передвинулся в точку [{x},{y}]'
    @logger
    def attack(self, target: str):
        return f'Персонаж атакует {target}'
    @logger
    def die(self):
        return f'Персонаж {self.name} погиб...'


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    from contextlib import redirect_stdout
    import io

    f = io.StringIO()
    with redirect_stdout(f):
        player = Player('Иван')
        player.move(0,1)
        player.attack('Супостат')
        player.die()
    actual_printed_str = f.getvalue()
    expected_printed_str = """\
[move] Вызов функции. Аргументы: ([0, 1])
[move] Результат: Персонаж передвинулся в точку [0,1]
[attack] Вызов функции. Аргументы: (['Супостат'])
[attack] Результат: Персонаж атакует Супостат
[die] Вызов функции. Аргументы: ([])
[die] Результат: Персонаж Иван погиб...
"""
    assert actual_printed_str == expected_printed_str, \
        (f"Ожидалось, что при вызове методов\nplayer.move(0,1)\nplayer.attack('Супостат')\nplayer.die()\nбудет "
         f"сформирован лог:\n{expected_printed_str}\n, а был:\n{actual_printed_str}")
    # вывод в терминал результата
    print(f'Все тесты прошли, декоратор реализован верно.')