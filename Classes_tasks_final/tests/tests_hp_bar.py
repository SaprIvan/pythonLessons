from engine.hp_bar import HealthBar
from engine.visual import Colors


def test_health_bar_attributes():
    assert (hasattr(HealthBar, '_HealthBar__remaining_health_symbol')
            and hasattr(HealthBar, '_HealthBar__lost_health_symbol')
            and hasattr(HealthBar, '_HealthBar__bars_count')), 'Атрибуты содержащие символ оставшегося HP, символ потерянного HP и количество bar в классе HealthBar, должны быть приватными'
    hb_dinamic_attrs = HealthBar(max_health=1, bar_color='').__dict__
    assert 'bar_color' in hb_dinamic_attrs and 'max_health' in hb_dinamic_attrs, 'Атрибуты класса HealthBar: bar_color и max_health, должны быть динамическими.'


def test_initialize():
    import re
    color_for_test = '\033[38;05;222m'
    max_health = 10
    hb = HealthBar(max_health=max_health, bar_color=color_for_test)
    current_hp = 8
    bar = hb.draw(current_hp)
    pattern = r'^\|([\s\S]+\[[0-9;]+m)(.*)([\s\S]+\[0m)\|'
    result = re.findall(pattern, bar)
    assert result, 'Не удалось распарсить итоговую строку с окрашенным HealthBar. Убедитесь, что строка имеет формат |{Цвет окраски}{символы оставшегося хп}{символы утерянного хп}{Дефолтный цвет}|'
    bar_color, bars, end_color = result[0]
    assert end_color == Colors.default, f'После окраски HealthBar цвет нужно возвращать к дефолтному. Ожидался цвет {Colors.default}█{Colors.default}, а был {end_color}█{Colors.default}'
    assert bar_color == color_for_test, f'Цвет окраски HealthBar должен задаваться при создании экземпляра класса. Ожидался цвет {color_for_test}█{Colors.default}, а был {bar_color}█{Colors.default}'
    expect_hp = 16
    actual_hp = len([item for item in bars if item == '█'])
    assert actual_hp == expect_hp, f'При уровне HP: {current_hp}, ожидалось, что количество █ будет {expect_hp}, а было {actual_hp}. Проверьте корректность расчетов'
    expect_lost_hp = 4
    actual_lost_hp = len([item for item in bars if item == '_'])
    assert actual_lost_hp == expect_lost_hp, f'При уровне HP: {current_hp}, ожидалось, что количество _ будет {expect_lost_hp}, а было {actual_lost_hp}. Проверьте корректность расчетов'

def run_hp_bar_tests():
    print(f'{Colors.yellow}===Тестируем класс HealthBar==={Colors.default}')
    test_health_bar_attributes()
    test_initialize()
    print(f'{Colors.green}+++Все тесты прошли, класс HealthBar реализован верно.+++{Colors.default}')
    print(f'Игрок:\n{HealthBar(max_health=20, bar_color=Colors.green).draw(20)}')
    print(f'Противник:\n{HealthBar(max_health=20, bar_color=Colors.red).draw(14)}')
    print('====================')