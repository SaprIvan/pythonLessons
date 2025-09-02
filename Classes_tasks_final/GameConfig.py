from dataclasses import dataclass
from typing import List


@dataclass
class GameConfig:
    name: str
    pattern: List[List[str]]


    def  __post_init__(self):
        self.map_size_x: int = len(self.pattern)
        self.map_size_y: int = len(self.pattern[0])

    def __str__(self):
        return f'[{self.name}] Размер карты: {self.map_size_x}x{self.map_size_y}'

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
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

    # вывод в терминал результата
    print(f'Все тесты прошли, класс реализован верно.')