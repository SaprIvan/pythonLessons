from engine.visual import Colors
from entities.inventory import Inventory
from entities.items import Armor, Weapon


def test_initialize():
    inventory = Inventory()
    assert hasattr(inventory, '_Inventory__items'), 'Атрибут __items у класса Inventory, должен быть приватным.'
    assert len(getattr(inventory, '_Inventory__items')) == 0, 'При создании экземпляра класса Inventory, список предметов должен быть пустым'


def test_add_remove_item():
    inventory = Inventory()

    inventory.add_item('Item')
    assert inventory.items_count == 0, f'Добавлять в инвентарь можно только предметы типа BaseItem'

    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    light_armor = Armor(name=name,cost=cost, description=description, defence=defence)
    inventory.add_item(light_armor)
    name, description = 'Опасная дубина', 'Крепкая сосновая ветка с вбитым ржавым гвоздем на конце.'
    cost, damage, hit_chance = 4, 5, 75
    club = Weapon(name=name,cost=cost, description=description, damage=damage, hit_chance=hit_chance)
    inventory.add_item(club)
    assert len(getattr(inventory, '_Inventory__items')) == 2, 'После использования метода add_item, количество предметов в списке items не увеличелось.'
    removed_light_armor = inventory.remove_item(light_armor)
    assert len(getattr(inventory, '_Inventory__items')) == 1, 'После использования метода remove_item, количество предметов в списке items не уменьшилось.'
    assert removed_light_armor == light_armor, f'Метод remove_item класса Inventory, должен возвращать удаляемый объект. Почитайте про метод списков "pop".'

def test_draw_items():
    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    light_armor = Armor(name=name,cost=cost, description=description, defence=defence)
    inventory = Inventory()
    inventory.add_item(light_armor)

    name, description = 'Опасная дубина', 'Крепкая сосновая ветка с вбитым ржавым гвоздем на конце.'
    cost, damage, hit_chance = 4, 5, 75
    club = Weapon(name=name,cost=cost, description=description, damage=damage, hit_chance=hit_chance)
    inventory.add_item(club)
    expected_msg = f'-------------------\n{light_armor.get_info()}\n--------------------------------------\n{club.get_info()}\n-------------------'
    assert inventory.draw_all_items() == expected_msg, \
        f'Ожидалось, что метод draw_all_items у класса Inventory сформирует строку:\n{expected_msg}, а сформировал:\n{inventory.draw_all_items()}'


def test_items_count():
    inventory = Inventory()
    assert inventory.items_count == 0, \
        f'Свойство items_count у класса Inventory, при пустом списке __items, должен был вернуть 0, а вернул {inventory.items_count}'
    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    light_armor = Armor(name=name,cost=cost, description=description, defence=defence)
    inventory = Inventory()
    inventory.add_item(light_armor)
    assert inventory.items_count == 1, \
        f'После добавления элемента в пустой инвентарь с помощью метода add_item, свойство items_count должно было вернуть 1, а вернуло {inventory.items_count}'


def test_calculate_items_costs():
    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    light_armor = Armor(name=name,cost=cost, description=description, defence=defence)
    inventory = Inventory()
    inventory.add_item(light_armor)
    inventory.add_item(light_armor)
    inventory.add_item(light_armor)

    assert inventory.calculate_items_costs() == 30, \
        (f'При добавлении в пустой инвентарь трех предметов стоимостью 10 каждый, метод calculate_items_costs класса '
         f'Inventory должен был вернуть 30, а вернул {inventory.calculate_items_costs()}')


def run_inventory_tests():
    print(f'{Colors.yellow}===Тестируем класс Inventory==={Colors.default}')
    test_initialize()
    test_add_remove_item()
    test_draw_items()
    test_items_count()
    test_calculate_items_costs()
    print(f'{Colors.green}+++Все тесты прошли, класс Inventory реализован верно.+++{Colors.default}')
    print('====================')

if __name__ == '__main__':
    run_inventory_tests()