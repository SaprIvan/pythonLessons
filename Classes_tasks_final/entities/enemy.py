from engine.visual import Colors
from entities.entity import Entity
from entities.entity_data import EntityData
from entities.items import Armor, Weapon


# Место для реализации класса Enemy

class Enemy(Entity):
    def __init__(self, armor: Armor, weapon: Weapon, data: EntityData):
        __tag = "Enemy"
        super().__init__(__tag, data, weapon, armor)
        self._hp_bar.bar_color = Colors.red

    def die(self):
        self._is_dead = True