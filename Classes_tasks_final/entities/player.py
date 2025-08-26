from engine.events import entity_events
from engine.visual import CellType, Colors
from entities.entity import Entity, EntityItemTypeError
from entities.entity_data import EntityData
from entities.inventory import Inventory
from entities.items import Weapon, Armor


class Player(Entity):
    def __init__(self, armor: Armor, weapon: Weapon, data: EntityData):
        # Место для дополнения класса Player атрибутами и вызовом инициализатора родительского класса

        entity_events.Change_Armor += self.change_armor
        entity_events.Change_Weapon += self.change_weapon

    # Место для дополнения класса Player свойствами

    @location.setter
    def location(self, value):
        if self.__location:
            if self.__location.entity and self.__location.entity.is_dead:
                self.__location.cell_type = CellType.dead_enemy
            elif self.__location.item:
                self.__location.cell_type = CellType.item
            elif self.__location.is_start_cell:
                self.__location.cell_type = CellType.start
            elif self.__location.is_end_cell:
                self.__location.cell_type = CellType.end
            else:
                self.__location.cell_type = CellType.empty_room
        self.__location = value
        self.__location.cell_type = CellType.player

    # Место для дополнения класса Player методами
