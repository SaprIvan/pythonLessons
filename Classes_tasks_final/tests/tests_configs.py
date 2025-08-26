from engine.configs import GameConfig
from engine.visual import Colors


def test_initialize():
    pattern = [
        ['⏩', '  ', '💎'],
        ['🧱', '⚔️', '🧱'],
        ['⏪', '  ', '🧱']
    ]
    SMALL_MAP = GameConfig(
        name='МАЛЕНЬКАЯ',
        pattern=pattern
    )

    dataclass_fields = getattr(GameConfig, '__dataclass_fields__', None)
    dataclass_params = getattr(GameConfig, '__dataclass_params__', None)
    assert dataclass_fields and dataclass_params, f'GameConfig должен быть классом данных (@dataclass), а не обычным классом.'

    assert SMALL_MAP.name == "МАЛЕНЬКАЯ", f"Название должно быть 'МАЛЕНЬКАЯ', фактически {SMALL_MAP.name}"
    assert SMALL_MAP.pattern == pattern, f"Шаблон должен быть {pattern}, фактически {SMALL_MAP.pattern}"
    assert SMALL_MAP.map_size_x == 3, f"Ширина карты должна быть 3, фактически {SMALL_MAP.map_size_x}"
    assert SMALL_MAP.map_size_y == 3, f"Высота карты должна быть 3, фактически {SMALL_MAP.map_size_y}"
    expected_output = "[МАЛЕНЬКАЯ] Размер карты: 3x3"
    assert str(SMALL_MAP) == expected_output, f"Ожидаемый вывод: {expected_output}, фактический вывод: {str(SMALL_MAP)}"


def run_configs_tests():
    print(f'{Colors.yellow}===Тестируем класс GameConfig==={Colors.default}')
    test_initialize()
    print(f'{Colors.green}+++Все тесты прошли, класс GameConfig реализован верно.+++{Colors.default}')
    print('====================')