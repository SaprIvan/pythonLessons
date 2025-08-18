class BaseItem:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description
    def __str__(self):
        return f"[{self.__name}] {self.__description}"

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    name = 'Легкий кожаный доспех'
    description = 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    light_armor = BaseItem(name=name, description=description)

    assert hasattr(light_armor, '_BaseItem__name') and hasattr(light_armor, '_BaseItem__description'), \
        f'Атрибуты name и description у класса BaseItem должны быть приватными. '
    assert isinstance(getattr(BaseItem, 'name'), property) and isinstance(getattr(BaseItem, 'description'), property), \
        f'У класса BaseItem должны быть реализованы свойства name и description.'
    assert light_armor.name == name and light_armor.description == description, \
        f'Проверьте, что свойства возвращают значение, из соответствующего им, приватного атрибута'
    override_str = str(light_armor)
    expect_str = f'[{name}] {description}'
    assert override_str == expect_str, f'Переопределенный магический метод __str__ должен возвращать строку: {expect_str}, а вернул {override_str}'

    # вывод в терминал результата
    print(f'Все тесты прошли, класс реализован верно.')
    print(light_armor)