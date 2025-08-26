from dungeon.cell_entity import Cell
from engine.events import entity_events
from engine.geometry import Vector2
from engine.visual import Colors, CellType
from entities.entity import EntityItemTypeError, Entity
from entities.entity_data import EntityData
from entities.inventory import Inventory
from entities.items import Weapon, Armor, Loot
from entities.player import Player


def get_armor():
    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    return Armor(name=name, cost=cost, description=description, defence=defence)


def get_weapon():
    name, description = 'Опасная дубина', 'Крепкая сосновая ветка с вбитым ржавым гвоздем на конце.'
    cost, damage, hit_chance = 4, 5, 75
    return Weapon(name=name,cost=cost, description=description, damage=damage, hit_chance=hit_chance)


def get_entity_data():
    name, hp = 'Герман из Ливии', 10
    description = 'Вам за 50 лет, по местным меркам - глубокая старость. Но несбывшиеся мечты молодости толкают вас на авантюры.'
    death_description = 'Ваша кончина была быстрой. Вы даже не поняли, как погибли.'
    return EntityData(name=name, description=description, hp=hp, death_description=death_description)


def test_initialize():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    player = Player(armor=armor, weapon=weapon, data=data)

    assert hasattr(player, '_Entity__tag'), "Класс Player должен наследоваться от Entity"
    assert hasattr(player, '_Player__location'), 'Класс Player должен иметь приватный атрибут __location'
    assert hasattr(player, '_Player__inventory'), 'Класс Player должен иметь приватный атрибут __inventory'

    assert isinstance(getattr(Player, 'tag'), property), 'Для класса Player должно быть доступно свойство tag родительского класса Entity'
    assert isinstance(getattr(Player, 'data'), property), 'Для класса Player должно быть доступно свойство data родительского класса Entity'
    assert isinstance(getattr(Player, 'is_dead'), property), 'Для класса Player должно быть доступно свойство is_dead родительского класса Entity'
    assert isinstance(getattr(Player, 'weapon'), property), 'Для класса Player должно быть доступно свойство weapon родительского класса Entity'
    assert isinstance(getattr(Player, 'armor'), property), 'Для класса Player должно быть доступно свойство armor родительского класса Entity'
    assert isinstance(getattr(Player, 'current_hp'), property), 'Для класса Player должно быть доступно свойство current_hp родительского класса Entity'
    assert isinstance(getattr(Player, 'inventory'), property), 'Для класса Player должно быть реализовано свойство inventory'
    assert isinstance(getattr(Player, 'location'), property), 'Для класса Player должно быть реализовано свойство location'

    assert player.tag == 'Player', f"При инициализации класса Player, свойство tag должно было вернуть 'Player', фактически вернуло '{player.tag}'"
    assert player.data == data, f"При инициализации класса Player с аргументами 'armor={armor}', 'weapon={weapon}', 'data={data}', свойство data должно было вернуть '{data}', фактически вернуло {player.data}"
    assert not player.is_dead, f"При инициализации класса Player свойство is_dead должно было вернуть False, фактически вернуло {player.is_dead}"
    assert player.weapon == weapon, f"При инициализации класса Player с аргументами 'armor={armor}', 'weapon={weapon}', 'data={data}', свойство weapon должно было вернуть '{weapon}', фактически вернуло {player.weapon}"
    assert player.armor == armor, f"При инициализации класса Player с аргументами 'armor={armor}', 'weapon={weapon}', 'data={data}', свойство armor должно было вернуть '{armor}', фактически вернуло {player.armor}"
    assert player._hp_bar.bar_color == Colors.green, f'Для bar_color класса HealthBar, который хранится в атрибуте _hp_bar класса Entity, при создании класса Player должен был быть установлен цвет {Colors.green}ЦВЕТ{Colors.default}, фактически был {player._hp_bar.bar_color}ЦВЕТ{Colors.default}'
    assert player._Player__location is None, f'При создании экземпляра класса Player, атрибут __location должен быть None, фактически был {player._Player__location}'
    assert isinstance(player._Player__inventory, Inventory), f'При создании экземпляра класса Player, атрибут __inventory должен быть типом Inventory, фактически был {type(player._Player__inventory)}'


def test_player_die():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    player = Player(armor=armor, weapon=weapon, data=data)
    player.die()
    assert player.is_dead, 'После вызова метода die класса Player, атрибут is_dead должен был измениться на True.'


def test_player_move():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    player = Player(armor=armor, weapon=weapon, data=data)
    cell = Cell(position=Vector2(0, 0), cell_type=CellType.player)
    player.move(cell)
    assert player.location == cell, f'После вызова метода move, ожидалось, что location класса Player измениться на {cell}, фактически было {player.location}'


def test_player_change_armor():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    player = Player(armor=armor, weapon=weapon, data=data)
    assert player.inventory.items_count == 0, f'При создании класса Player, количество предметов в инвентаре должно быть 0, фактически было {player.inventory.items_count}'
    new_armor = Armor(name='Мифриловая броня', description='Это броню не пробить', cost=1000, defence=100500)
    player.inventory.add_item(new_armor)
    assert player.inventory.items_count == 1, f'При добавлении предмета в пустой инвентарь класса Player, количество предметов в инвентаре должно быть 1, фактически было {player.inventory.items_count}'
    assert player.inventory.items[-1] == new_armor, f'При добавлении предмета {new_armor} в пустой инвентарь класса Player, ожидалось, что предметр в инвентаре будет {new_armor}, фактически был {player.inventory.items[-1]}'
    player.change_armor(new_armor)
    assert player.armor == new_armor, f'После изменения брони на {new_armor} у игрока, ожидалось, что в атрибуте armor будет {new_armor}, фактически было {player.armor}'
    assert player.inventory.items[-1] == armor, f'После изменения брони на {new_armor} у игрока, ожидалось, что старая броня окажется в инвентаре.'


def test_player_change_armor_to_weapon():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    player = Player(armor=armor, weapon=weapon, data=data)
    new_weapon = Weapon(name='Сокрушитель нечести', description='Идеально подходит для уничтожения нечисти', cost=1000, damage=100, hit_chance=100)
    player.inventory.add_item(new_weapon)
    try:
        player.change_armor(new_weapon)
        assert True, 'Метод change_armor класса Player, должен заменять только предметы с типом Armor'
    except EntityItemTypeError:
        pass


def test_player_change_weapon():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    player = Player(armor=armor, weapon=weapon, data=data)
    assert player.inventory.items_count == 0, f'При создании класса Player, количество предметов в инвентаре должно быть 0, фактически было {player.inventory.items_count}'
    new_weapon = Weapon(name='Сокрушитель нечести', description='Идеально подходит для уничтожения нечисти', cost=1000, damage=100, hit_chance=100)
    player.inventory.add_item(new_weapon)
    assert player.inventory.items_count == 1, f'При добавлении предмета в пустой инвентарь класса Player, количество предметов в инвентаре должно быть 1, фактически было {player.inventory.items_count}'
    assert player.inventory.items[-1] == new_weapon, f'При добавлении предмета {new_weapon} в пустой инвентарь класса Player, ожидалось, что предметр в инвентаре будет {new_weapon}, фактически был {player.inventory.items[-1]}'
    player.change_weapon(new_weapon)
    assert player.armor == new_weapon, f'После изменения брони на {new_weapon} у игрока, ожидалось, что в атрибуте armor будет {new_weapon}, фактически было {player.armor}'
    assert player.inventory.items[-1] == armor, f'После изменения брони на {new_weapon} у игрока, ожидалось, что старая броня окажется в инвентаре.'


def test_player_change_weapon_to_armor():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    player = Player(armor=armor, weapon=weapon, data=data)
    new_armor = Armor(name='Мифриловая броня', description='Это броню не пробить', cost=1000, defence=100500)
    player.inventory.add_item(new_armor)
    try:
        player.change_weapon(new_armor)
        assert True, 'Метод change_weapon класса Player, должен заменять только предметы с типом Weapon'
    except EntityItemTypeError:
        pass


def test_player_lift_item():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    player = Player(armor=armor, weapon=weapon, data=data)
    assert player.inventory.items_count == 0, f'При создании класса Player, количество предметов в инвентаре должно быть 0, фактически было {player.inventory.items_count}'
    cell = Cell(position=Vector2(0, 0), cell_type=CellType.player)
    item = Loot(name='Золотая монета', description='Обычная золотая монета', cost=1)
    cell.item = item
    player.move(cell)

    calls = []
    def lift_mock(item):
        calls.append(item)

    entity_events.Lift_Item += lift_mock
    player.lift_item()
    entity_events.Lift_Item -= lift_mock
    assert player.inventory.items_count == 1, (f'При вызове метода lift_item класса Player, когда location класса Player '
                                               f'содержит в себе Cell с item не None, количество предметов в инвентаре должно было стать 1, фактически было {player.inventory.items_count}')
    assert len(calls) == 1 and item in calls, f'При вызове метода lift_item класса Player, когда location класса Player содержит в себе Cell с item не None, должно было вызваться событие entity_events.Lift_Item(item)'


def test_player_lift_not_item():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    player = Player(armor=armor, weapon=weapon, data=data)
    assert player.inventory.items_count == 0, f'При создании класса Player, количество предметов в инвентаре должно быть 0, фактически было {player.inventory.items_count}'
    cell = Cell(position=Vector2(0, 0), cell_type=CellType.player)
    player.move(cell)

    calls = []
    def lift_mock(item):
        calls.append(item)

    entity_events.Lift_Item += lift_mock
    player.lift_item()
    entity_events.Lift_Item -= lift_mock
    assert player.inventory.items_count == 0, (f'При вызове метода lift_item класса Player, когда location класса Player '
                                               f'содержит в себе Cell с item None, количество предметов в инвентаре должно остаться 0, фактически было {player.inventory.items_count}')
    assert len(calls) == 0, 'Когда метод lift_item вызывается в комнате, в которой нет предмета, событие entity_events.Lift_Item(item) вызываться не должно.'


def test_player_looting_dead_enemy():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    player = Player(armor=armor, weapon=weapon, data=data)
    enemy_armor = Armor(name='Рваные лохмотья', description='Словами не описать...', cost=1, defence=1)
    enemy_weapon = Weapon(name='Камнемолот', description='Палка с камнем', cost=1, damage=4, hit_chance=75)
    enemy = Entity(tag='Enemy', armor=enemy_armor, weapon=enemy_weapon, data=data)
    enemy._is_dead = True
    cell = Cell(position=Vector2(0, 0), cell_type=CellType.player)
    cell.entity = enemy
    player.move(cell)
    assert player.inventory.items_count == 0, f'При создании класса Player, количество предметов в инвентаре должно быть 0, фактически было {player.inventory.items_count}'
    calls = []

    def lift_mock(item):
        calls.append(item)

    entity_events.Lift_Item += lift_mock
    player.looting_dead_enemy()
    entity_events.Lift_Item -= lift_mock
    assert player.inventory.items_count == 2, (f'При вызове метода looting_dead_enemy класса Player, когда location класса '
                                               f'Player - это Cell с entity не None, и при этом entity имеет атрибут is_dead=True, в инвентаре предметов должно было стать 2, фактически было {player.inventory.items_count}')
    assert enemy_armor in player.inventory.items and enemy_weapon in player.inventory.items, \
        f'При вызове метода looting_dead_enemy класса Player, когда location класса Player - это Cell с entity не None, и при этом entity имеет атрибут is_dead=True, в инвентарь должны были добавиться оружие и броня entity. Но не добавились.'
    assert enemy.weapon is None and enemy.armor is None, \
        f'При вызове метода looting_dead_enemy класса Player, когда location класса Player - это Cell с entity не None, и при этом entity имеет атрибут is_dead=True, у entity атрибуты armor и weapon должны были стать None.'
    assert len(calls) == 2, ('При вызове метода looting_dead_enemy класса Player, когда location класса Player - '
                             'это Cell с entity не None, и при этом entity имеет атрибут is_dead=True, должны были вызваться события  entity_events.Lift_Item(weapon) и entity_events.Lift_Item(armor) ')

def run_player_tests():
    print(f'{Colors.yellow}===Тестируем класс Player==={Colors.default}')
    test_initialize()
    test_player_die()
    test_player_move()
    test_player_change_armor()
    test_player_change_armor_to_weapon()
    test_player_change_weapon_to_armor()
    test_player_lift_item()
    test_player_lift_not_item()
    test_player_looting_dead_enemy()
    print(f'{Colors.green}+++Все тесты прошли, класс Player реализован верно.+++{Colors.default}')
    print('====================')