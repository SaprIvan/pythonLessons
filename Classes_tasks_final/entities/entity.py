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
            if isinstance(value, Armor) or isinstance(value, None):
                self.__armor = value
            else:
                raise EntityItemTypeError()

        @weapon.setter
        def weapon(self, value):
            if isinstance(value, Weapon) or isinstance(value, None):
                self.__weapon = value
            else:
                raise EntityItemTypeError()

        @property
        def current_hp(self):
            return self._hp_bar.draw(self.__data.hp)

        def  __calculate_damage (targer: Entity):
            if self.__weapon.hit_chance >= randint(0, 100) and self.weapon.damage > targer.armor.defence:
                hit = True
            else: return 0
            return self.weapon - targer.__armor.defence