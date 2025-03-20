welcome_string = """
Привет "{}"! Добро пожаловать в нашу игру: "{}"!
"""

player = "<Игрок>"
game = 'Мир Кораблей'

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert welcome_string is not None and player is not None and game is not None
    # вывод в терминал результата
    print(welcome_string.format(player, game))