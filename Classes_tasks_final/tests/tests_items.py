from engine.visual import Colors
from entities.items import Armor, BaseItem, Weapon, Loot


def test_base_item_properties():
    assert (isinstance(getattr(BaseItem, 'name'), property)
            and isinstance(getattr(BaseItem, 'description'), property)
            and isinstance(getattr(BaseItem, 'cost'), property)), \
        f'У класса BaseItem должны быть реализованы свойства name, cost и description.'


def test_base_item_get_info():
    name, description = 'Грязный амулет', 'Почерневший серебряный амулет с пустым гнездом под драгоценный камень.'
    cost = 3
    item = BaseItem(name=name, description=description, cost=cost)
    try:
        item.get_info()
        assert False, 'Метод get_info у класса BaseItem должен выкидывать NotImplementedError'
    except NotImplementedError:
        pass


def test_armor_initialize():
    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    light_armor = Armor(name=name,cost=cost, description=description, defence=defence)
    override_str = str(light_armor)
    expect_str = f'[{name}][{cost}] {description}'
    assert override_str == expect_str, f'Переопределенный магический метод __str__ должен возвращать строку: {expect_str}, а вернул {override_str}'
    assert light_armor.name == name and light_armor.description == description and light_armor.cost == cost and light_armor.defence == defence, \
        f'Проверьте, что в классах BaseItem и Armor свойства возвращают значение, из соответствующего им, приватного атрибута'
    assert (hasattr(light_armor, '_BaseItem__name')
            and hasattr(light_armor, '_BaseItem__description')
            and hasattr(light_armor, '_BaseItem__cost')), \
        f'Атрибуты cost, name и description у класса BaseItem должны быть приватными. '
    assert hasattr(light_armor, '_Armor__defence') and isinstance(getattr(Armor, 'defence'), property), \
        f'У класса Armory должны быть реализованы приватное поле defence и соосвойство defence'

def test_armor_get_info():
    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    light_armor = Armor(name=name, cost=cost, description=description, defence=defence)
    expected_msg = (f'[{name}] {description}\n'
                    f'[Защита]: {Colors.yellow}{defence}{Colors.default}\n'
                    f'[Стоимость]: {Colors.yellow}{cost}{Colors.default}')
    assert light_armor.get_info() == expected_msg, \
        f'Проверьте корректность возвращаемой строки методом get_info у класса Armor. Ожидалось\n: {expected_msg}, а было\n{light_armor.get_info()}'


def test_armor_get_short_info():
    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    light_armor = Armor(name=name, cost=cost, description=description, defence=defence)
    expected_msg = f'[{name}] Защита: {defence}'
    assert light_armor.get_short_info() == expected_msg, \
        f'Проверьте корректность возвращаемой строки методом get_short_info у класса Armor. Ожидалось\n: {expected_msg}, а было\n{light_armor.get_short_info()}'


def test_weapon_initialize():
    name, description = 'Опасная дубина', 'Крепкая сосновая ветка с вбитым ржавым гвоздем на конце.'
    cost, damage, hit_chance = 4, 5, 75
    club = Weapon(name=name,cost=cost, description=description, damage=damage, hit_chance=hit_chance)
    assert (hasattr(club, '_Weapon__damage') and isinstance(getattr(Weapon, 'damage'), property)
            and hasattr(club, '_Weapon__hit_chance') and isinstance(getattr(Weapon, 'hit_chance'), property)), \
        f'У класса Weapon должны быть реализованы приватные поля damage, hit_chance и соосвойства damage, hit_chance'
    assert club.name == name and club.description == description and club.cost == cost and club.damage == damage and club.hit_chance == hit_chance, \
        f'Проверьте, что в классах BaseItem и Weapon свойства возвращают значение, из соответствующего им, приватного атрибута'


def test_weapon_get_info():
    name, description = 'Опасная дубина', 'Крепкая сосновая ветка с вбитым ржавым гвоздем на конце.'
    cost, damage, hit_chance = 4, 5, 75
    club = Weapon(name=name,cost=cost, description=description, damage=damage, hit_chance=hit_chance)
    expected_msg = (f'[{name}]  {description}\n'
                    f'[Урон]: {Colors.yellow}{damage}{Colors.default}\n'
                    f'[Шанс попадания] {Colors.yellow}{hit_chance}%{Colors.default}\n'
                    f'[Стоимость]: {Colors.yellow}{cost}{Colors.default}')
    assert club.get_info() == expected_msg, \
        f'Проверьте корректность возвращаемой строки методом get_info у класса Weapon. Ожидалось\n: {expected_msg}, а было\n{club.get_info()}'


def test_weapon_get_short_info():
    name, description = 'Опасная дубина', 'Крепкая сосновая ветка с вбитым ржавым гвоздем на конце.'
    cost, damage, hit_chance = 4, 5, 75
    club = Weapon(name=name,cost=cost, description=description, damage=damage, hit_chance=hit_chance)
    expected_msg = f'[{name}] Урон: {damage} Шанс попадания: {hit_chance}%'
    assert club.get_short_info() == expected_msg, \
        f'Проверьте корректность возвращаемой строки методом get_info у класса Weapon. Ожидалось\n: {expected_msg}, а было\n{club.get_short_info()}'


def test_loot_initialize():
    name, description = 'Грязный амулет', 'Почерневший серебряный амулет с пустым гнездом под драгоценный камень.'
    cost = 3
    amulet = Loot(name=name, description=description, cost=cost)
    assert amulet.name == name and amulet.description == description and amulet.cost == cost, \
        f'Проверьте, что в классe BaseItem свойства возвращают значение, из соответствующего им, приватного атрибута'


def test_loot_get_info():
    name, description = 'Грязный амулет', 'Почерневший серебряный амулет с пустым гнездом под драгоценный камень.'
    cost = 3
    amulet = Loot(name=name, description=description, cost=cost)
    expected_msg = (f'[{name}] {description}\n'
                    f'[Стоимость]: {Colors.yellow}{cost}{Colors.default}')
    assert amulet.get_info() == expected_msg, \
        f'Проверьте корректность возвращаемой строки методом get_info у класса Loot. Ожидалось\n: {expected_msg}, а было\n{amulet.get_info()}'


def run_items_tests():
    print(f'{Colors.yellow}===Тестируем классы BaseItem, Armor, Weapon, Loot==={Colors.default}')
    test_base_item_properties()
    test_base_item_get_info()
    test_armor_initialize()
    test_armor_get_info()
    test_armor_get_short_info()
    test_weapon_initialize()
    test_weapon_get_info()
    test_weapon_get_short_info()
    test_loot_initialize()
    test_loot_get_info()
    print(f'{Colors.green}+++Все тесты прошли, классы BaseItem, Armor, Weapon, Loot реализован верно.+++{Colors.default}')
    print('====================')


if __name__ == '__main__':
    run_items_tests()