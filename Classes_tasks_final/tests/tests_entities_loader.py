import json
import os

import data
from core.entities_loader import EntitiesLoader
from engine.visual import Colors
from entities.enemy import Enemy
from entities.items import Loot
from entities.player import Player


def get_game_data():
    with open(f'{os.path.dirname(data.__file__)}/game_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def test_initialize():
    entities_loader = EntitiesLoader()
    assert hasattr(entities_loader, '_EntitiesLoader__game_data'), 'Класс EntitiesLoader должен содержать в себе приватный атрибут game_data'
    assert getattr(entities_loader, '_EntitiesLoader__game_data') == get_game_data(), f'При инициализации класса, в приватный атрибут game_data должно было записаться содержимое файла data/game_data.json. Почитайте про библиотеку json'
    del entities_loader


def test_get_random_room_description():
    entities_loader = EntitiesLoader()
    random_room = entities_loader.get_random_room_description()
    assert isinstance(random_room, str), f'Метод get_random_room_description должен возвращать строку, фактически вернул {type(random_room)}'
    assert random_room in entities_loader._EntitiesLoader__game_data['room']['descriptions'], f"Описание комнаты должно быть из __game_data['room']['descriptions']. Полученное описание\n{random_room}"


def test_create_random_player():
    entities_loader = EntitiesLoader()
    player = entities_loader.create_random_player()
    assert isinstance(player, Player), f'Метод create_random_player должен возвращать экземпляр класса Player, фактически вернулся тип {type(player)}'
    assert player.data.name in entities_loader._EntitiesLoader__game_data['player']['names'], f"Метод create_random_player должен брать случайно имя для EntityData из __game_data['player']['names'], фактически получено {player.data.name}"
    assert player.data.description in entities_loader._EntitiesLoader__game_data['player']['descriptions'], f"Метод create_random_player должен брать случайно описание для EntityData из __game_data['player']['descriptions'], фактически получено {player.data.description}"
    assert player.data.death_description in entities_loader._EntitiesLoader__game_data['player']['death_description'], f"Метод create_random_player должен брать случайно описание смерти для EntityData из __game_data['player']['death_description'], фактически получено {player.data.death_description}"
    assert player.data.hp == entities_loader._EntitiesLoader__game_data['player']['hp'], f"Метод create_random_player должен брать количесто HP для EntityData из __game_data['player']['hp'], фактически получено {player.data.hp}"

    assert player.weapon.name == entities_loader._EntitiesLoader__game_data['player']['weapon']['name'], f"Метод create_random_player должен брать название оружия для Weapon из __game_data['player']['weapon']['name'], фактически получено {player.weapon.name}"
    assert player.weapon.description == entities_loader._EntitiesLoader__game_data['player']['weapon']['description'], f"Метод create_random_player должен брать описание оружия для Weapon из __game_data['player']['weapon']['description'], фактически получено {player.weapon.description}"
    assert player.weapon.damage == entities_loader._EntitiesLoader__game_data['player']['weapon']['damage'], f"Метод create_random_player должен брать урон оружия для Weapon из __game_data['player']['weapon']['damage'], фактически получено {player.weapon.damage}"
    assert player.weapon.hit_chance == entities_loader._EntitiesLoader__game_data['player']['weapon']['hit_chance'], f"Метод create_random_player должен брать шанс попадания оружия для Weapon из __game_data['player']['weapon']['hit_chance'], фактически получено {player.weapon.hit_chance}"
    assert player.weapon.cost == entities_loader._EntitiesLoader__game_data['player']['weapon']['cost'], f"Метод create_random_player должен брать стоимость оружия для Weapon из __game_data['player']['weapon']['cost'], фактически получено {player.weapon.cost}"

    assert player.armor.description == entities_loader._EntitiesLoader__game_data['player']['armor']['description'], f"Метод create_random_player должен брать описание брони для Armor из __game_data['player']['armor']['description'], фактически получено {player.armor.description}"
    assert player.armor.name == entities_loader._EntitiesLoader__game_data['player']['armor']['name'], f"Метод create_random_player должен брать название брони для Armor из __game_data['player']['armor']['name'], фактически получено {player.armor.name}"
    assert player.armor.defence == entities_loader._EntitiesLoader__game_data['player']['armor']['defence'], f"Метод create_random_player должен брать защиту брони для Armor из __game_data['player']['armor']['defence'], фактически получено {player.armor.defence}"
    assert player.armor.cost == entities_loader._EntitiesLoader__game_data['player']['armor']['cost'], f"Метод create_random_player должен брать стоимость брони для Armor из __game_data['player']['armor']['cost'], фактически получено {player.armor.cost}"


def test_create_random_enemy():
    entities_loader = EntitiesLoader()
    enemy = entities_loader.create_random_enemy()
    assert isinstance(enemy, Enemy), f'Метод create_random_enemy должен возвращать экземпляр класса Enemy, фактически вернулся тип {type(enemy)}'
    enemies = {v['name']: v for _, v in entities_loader._EntitiesLoader__game_data['enemies'].items()}
    assert enemy.data.name in enemies, "Метод create_random_enemy должен брать случайного противника из __game_data['enemies']"

    current_enemy = enemies[enemy.data.name]
    assert enemy.data.description in current_enemy['description'], f"Метод create_random_enemy должен брать описание для EntityData из описания выбранного противника {current_enemy['name']}, фактически получено {enemy.data.description}"
    assert enemy.data.death_description in current_enemy['death_description'], f"Метод create_random_enemy должен брать описание смерти для EntityData из описания смерти выбранного противника {current_enemy['name']}, фактически получено {enemy.data.death_description}"
    assert enemy.data.hp == current_enemy['hp'], f"Метод create_random_enemy должен брать количесто HP для EntityData из HP выбранного противника {current_enemy['name']}, фактически получено {enemy.data.hp}"

    assert enemy.weapon.name == current_enemy['weapon']['name'], f"Метод create_random_enemy должен брать название оружия для Weapon из данных выбранного противника {current_enemy['name']}, фактически получено {enemy.weapon.name}"
    assert enemy.weapon.description == current_enemy['weapon']['description'], f"Метод create_random_enemy должен брать описание оружия для Weapon из данных выбранного противника {current_enemy['name']}, фактически получено {enemy.weapon.description}"
    assert enemy.weapon.damage == current_enemy['weapon']['damage'], f"Метод create_random_enemy должен брать урон оружия для Weapon из данных выбранного противника {current_enemy['name']}, фактически получено {enemy.weapon.damage}"
    assert enemy.weapon.hit_chance == current_enemy['weapon']['hit_chance'], f"Метод create_random_enemy должен брать шанс попадания оружия для Weapon из данных выбранного противника {current_enemy['name']}, фактически получено {enemy.weapon.hit_chance}"
    assert enemy.weapon.cost == current_enemy['weapon']['cost'], f"Метод create_random_enemy должен брать стоимость оружия для Weapon из данных выбранного противника {current_enemy['name']}, фактически получено {enemy.weapon.cost}"

    assert enemy.armor.description == current_enemy['armor']['description'], f"Метод create_random_enemy должен брать описание брони для Armor из данных выбранного противника {current_enemy['name']}, фактически получено {enemy.armor.description}"
    assert enemy.armor.name == current_enemy['armor']['name'], f"Метод create_random_enemy должен брать название брони для Armor из данных выбранного противника {current_enemy['name']}, фактически получено {enemy.armor.name}"
    assert enemy.armor.defence == current_enemy['armor']['defence'], f"Метод create_random_enemy должен брать защиту брони для Armor из данных выбранного противника {current_enemy['name']}, фактически получено {enemy.armor.defence}"
    assert enemy.armor.cost == current_enemy['armor']['cost'], f"Метод create_random_enemy должен брать стоимость брони для Armor из данных выбранного противника {current_enemy['name']}, фактически получено {enemy.armor.cost}"


def test_create_random_item():
    entities_loader = EntitiesLoader()
    item = entities_loader.create_random_item()
    assert isinstance(item, Loot), f'Метод create_random_item должен возвращать экземпляр класса Loot, фактически вернулся тип {type(item)}'
    items = {v['name']: v for _, v in entities_loader._EntitiesLoader__game_data['items'].items()}
    assert item.name in items, "Метод create_random_item должен брать случайный предмет из __game_data['items']"
    current_item = items[item.name]

    assert item.description == current_item['description'], f"Метод create_random_item должен брать описание брони для Loot из данных выбранного предмета {current_item['name']}, фактически получено {item.description}"
    assert item.cost == current_item['cost'], f"Метод create_random_item должен брать стоимость брони для Loot из данных выбранного предмета {current_item['name']}, фактически получено {item.cost}"


def run_entities_loader_tests():
    print(f'{Colors.yellow}===Тестируем класс EntitiesLoader==={Colors.default}')
    test_initialize()
    test_get_random_room_description()
    test_create_random_player()
    test_create_random_enemy()
    test_create_random_item()
    print(f'{Colors.green}+++Все тесты прошли, класс EntitiesLoader реализован верно.+++{Colors.default}')
    print('====================')