from __future__ import annotations
from random import randint

from engine.events import entity_events
from engine.hp_bar import HealthBar
from engine.visual import Colors
from entities.entity_data import EntityData
from entities.items import Armor, Weapon

# Место для реализации классов EntityItemTypeError и Entity
class EntityItemTypeError(Exception):
    pass


class Entity:
    def __init__(self, tag, data, weapon, armor):
        self.__tag = tag
        self.__data = data
        self.__weapon = weapon
        self.__armor = armor
        self._is_dead = False
        self._hp_bar = HealthBar(bar_color=Colors.default, max_health=self.__data.health)

    @property
    def tag(self):
        return self.__tag

    @property
    def data(self):
        return self.__data

    @property
    def weapon(self):
        return self.__weapon

    @property
    def armor(self):
        return self.__armor

    @property
    def is_dead(self):
        return self._is_dead

    @armor.setter
    def armor(self, value):
        if isinstance(value, Armor) or value is None:
            self.__armor = value
        else:
            raise EntityItemTypeError()

    @weapon.setter
    def weapon(self, value):
        if isinstance(value, Weapon) or value is None:
            self.__weapon = value
        else:
            raise EntityItemTypeError()

    @property
    def current_hp(self):
        return self._hp_bar.draw(self.__data.hp)

    def  __calculate_damage (self, target: Entity):
        if self.__weapon.hit_chance >= randint(0, 100) and self.__weapon.damage > target.armor.defence:
            hit = True
        else: return 0
        return self.__weapon.damage - target.__armor.defence

    def attack(self, target: Entity):
        entity_events.Attack(self, target, self.__calculate_damage(target))

    def taking_damage(self, damage: int):
        if damage < self.__data.hp:
            self.__data.hp -= damage
        else:
            self.__data.hp = 0
            entity_events.Die(self)

    def die(self):
        raise NotImplementedError("Method die should be implemented")

    def draw_info(self):
        return (f'\n[{self.__data.name}] {self.current_hp}\n'
                f'{self.__data.description}\n'
                f'=======[В руках]=======\n'
                f'{self.__weapon.get_short_info()}\n'
                f'=======[Надето]=======\n'
                f'{self.__armor.get_short_info()}\n')