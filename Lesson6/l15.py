class BaseItem:
    def __init__(self, name, cost, description):
        self.__name = name
        self.__cost = cost
        self.__description = description

    def __str__(self):
        return f"[{self.__name}][{self.__cost}] {self.__description}"

    @property
    def name(self):
        return self.__name
    @property
    def cost(self):
        return self.__cost
    @property
    def description(self):
        return self.__description

class Armor(BaseItem):
    def __init__(self, name, cost, description, defence):
        super().__init__(name, cost, description)
        self.__defence = defence

    @property
    def defence(self):
        return self.__defence


class Weapon(BaseItem):
    def __init__(self, name, cost, description, damage, hit_chance):
        super().__init__(name, cost, description)
        self.__hit_chance = hit_chance
        self.__damage = damage

    @property
    def damage(self):
        return self.__damage
    @property
    def hit_chance(self):
        return self.__hit_chance


class Loot(BaseItem):
    pass


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    light_armor = Armor(name=name,cost=cost, description=description, defence=defence)
    override_str = str(light_armor)
    expect_str = f'[{name}][{cost}] {description}'
    assert override_str == expect_str, f'Переопределенный магический метод __str__ должен возвращать строку: {expect_str}, а вернул {override_str}'
    assert (isinstance(getattr(BaseItem, 'name'), property)
            and isinstance(getattr(BaseItem, 'description'), property)
            and isinstance(getattr(BaseItem, 'cost'), property)), \
        f'У класса BaseItem должны быть реализованы свойства name, cost и description.'
    assert (hasattr(light_armor, '_BaseItem__name')
            and hasattr(light_armor, '_BaseItem__description')
            and hasattr(light_armor, '_BaseItem__cost')), \
        f'Атрибуты cost, name и description у класса BaseItem должны быть приватными. '
    assert hasattr(light_armor, '_Armor__defence') and isinstance(getattr(Armor, 'defence'), property), \
        f'У класса Armory должны быть реализованы приватное поле defence и соосвойство defence'
    assert light_armor.name == name and light_armor.description == description and light_armor.cost == cost and light_armor.defence == defence, \
        f'Проверьте, что в классах BaseItem и Armor свойства возвращают значение, из соответствующего им, приватного атрибута'

    name, description = 'Опасная дубина', 'Крепкая сосновая ветка с вбитым ржавым гвоздем на конце.'
    cost, damage, hit_chance = 4, 5, 75
    club = Weapon(name=name,cost=cost, description=description, damage=damage, hit_chance=hit_chance)
    assert (hasattr(club, '_Weapon__damage') and isinstance(getattr(Weapon, 'damage'), property)
            and hasattr(club, '_Weapon__hit_chance') and isinstance(getattr(Weapon, 'hit_chance'), property)), \
        f'У класса Weapon должны быть реализованы приватные поля damage, hit_chance и соосвойства damage, hit_chance'
    assert club.name == name and club.description == description and club.cost == cost and club.damage == damage and club.hit_chance == hit_chance, \
        f'Проверьте, что в классах BaseItem и Weapon свойства возвращают значение, из соответствующего им, приватного атрибута'

    name, description = 'Грязный амулет', 'Почерневший серебряный амулет с пустым гнездом под драгоценный камень.'
    cost = 3
    amulet = Loot(name=name, description=description, cost=cost)
    assert amulet.name == name and amulet.description == description and amulet.cost == cost, \
        f'Проверьте, что в классe BaseItem свойства возвращают значение, из соответствующего им, приватного атрибута'

    # вывод в терминал результата
    print(f'Все тесты прошли, класс реализован верно.')
    print(light_armor)
    print(club)
    print(amulet)