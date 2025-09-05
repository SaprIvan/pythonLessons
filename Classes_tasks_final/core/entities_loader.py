import json
import data
import os
from random import choice, randint

from entities import entity_data
from entities.enemy import Enemy
from entities.entity_data import EntityData
from entities.items import Armor, Weapon, Loot
from entities.player import Player


# Место для реализации класса EntitiesLoader:
class EntitiesLoader:
    def __load_game_data(self, filename):
        with open(filename, encoding="utf-8") as json_file:
            return json.load(json_file)


    def __init__(self, filename="data/game_data.json"):
        self.__game_data = self.__load_game_data(filename)

    def get_random_room_description(self):
        return choice(self.__game_data['room']['descriptions'])

    def create_random_player(self):
        armor = Armor(**self.__game_data['player']['armor'])
        weapon = Weapon(**self.__game_data['player']['weapon'])
        entity_data = EntityData(name = choice(self.__game_data['player']['names']),
                                 description = choice(self.__game_data['player']['descriptions']),
                                 hp = self.__game_data['player']['hp'],
                                 death_description=choice(self.__game_data['player']['death_description']))
        return Player(armor, weapon, entity_data)

    def create_random_enemy(self):
        rand_enemy = self.__game_data['enemies']['enemy_'+str(randint(1, 4))]
        armor = Armor(**rand_enemy['armor'])
        weapon = Weapon(**rand_enemy['weapon'])
        entity_data = EntityData(name = rand_enemy['name'],
                                 description=rand_enemy['description'],
                                 hp=rand_enemy['hp'],
                                 death_description=rand_enemy['death_description'])
        return Enemy(armor, weapon, entity_data)

    def create_random_item(self):
        rand_item = self.__game_data['items']['item_'+str(randint(1, 8))]
        return Loot(**rand_item)