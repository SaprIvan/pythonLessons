class Colors:
    __green = "\033[38;05;82m"
    __red = "\033[38;05;197m"
    __default = "\033[0m"

    @classmethod
    def green(cls):
        return cls.__green

    @classmethod
    def red(cls):
        return cls.__red

    @classmethod
    def default(cls):
        return cls.__default

class HealthBar:
    __remaining_health_symbol = '█'
    __lost_health_symbol = '_'
    __bars_count = 20

    def __init__(self, max_health, bar_color):
        self.bar_color = bar_color
        self.max_health = max_health

    def draw(self, hp):
        __health = ''
        __health_lost = ''
        remaining_health_bars = int(round(hp/self.max_health*self.__bars_count,0))
        for _ in range(self.__bars_count):
            if len(__health) < remaining_health_bars:
                __health+=self.__remaining_health_symbol
            else:
                __health_lost += self.__lost_health_symbol
        return f"|{self.bar_color}{ __health}{__health_lost}{Colors.default()}|"


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    import inspect
    assert inspect.ismethod(Colors.default) and inspect.ismethod(Colors.red) and inspect.ismethod(Colors.green), 'Геттеры default, green и red должны быть классовыми методами'
    assert not Colors().__dict__, 'Класс Colors не должен иметь динамические атрибуты'
    assert hasattr(Colors, '_Colors__default') and hasattr(Colors, '_Colors__red') and hasattr(Colors, '_Colors__green'), 'Атрибуты цветов в классе Colors должны быть приватными'

    assert (hasattr(HealthBar, '_HealthBar__remaining_health_symbol')
            and hasattr(HealthBar, '_HealthBar__lost_health_symbol')
            and hasattr(HealthBar, '_HealthBar__bars_count')), 'Атрибуты содержащие символ оставшегося HP, символ потерянного HP и количество bar в классе HealthBar, должны быть приватными'
    hb_dinamic_attrs = HealthBar(max_health=1, bar_color='').__dict__
    assert 'bar_color' in hb_dinamic_attrs and 'max_health' in hb_dinamic_attrs, 'Атрибуты класса HealthBar: bar_color и max_health, должны быть динамическими.'

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
    assert end_color == Colors.default(), f'После окраски HealthBar цвет нужно возвращать к дефолтному. Ожидался цвет {Colors.default()}█{Colors.default()}, а был {end_color}█{Colors.default()}'
    assert bar_color == color_for_test, f'Цвет окраски HealthBar должен задаваться при создании экземпляра класса. Ожидался цвет {color_for_test}█{Colors.default()}, а был {bar_color}█{Colors.default()}'
    expect_hp = 16
    actual_hp = len([item for item in bars if item == '█'])
    assert actual_hp == expect_hp, f'При уровне HP: {current_hp}, ожидалось, что количество █ будет {expect_hp}, а было {actual_hp}. Проверьте корректность расчетов'
    expect_lost_hp = 4
    actual_lost_hp = len([item for item in bars if item == '_'])
    assert actual_lost_hp == expect_lost_hp, f'При уровне HP: {current_hp}, ожидалось, что количество _ будет {expect_lost_hp}, а было {actual_lost_hp}. Проверьте корректность расчетов'

    # вывод в терминал результата
    print(f'Все тесты прошли, классы реализованы верно.')
    print(f'Игрок:\n{HealthBar(20, Colors.green()).draw(20)}')
    print(f'Противник:\n{HealthBar(20, Colors.red()).draw(14)}')