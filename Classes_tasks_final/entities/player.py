from dungeon.cell_entity import Cell
from engine.events import entity_events
from engine.visual import CellType, Colors
from entities.entity import Entity, EntityItemTypeError
from entities.entity_data import EntityData
from entities.inventory import Inventory
from entities.items import Weapon, Armor


class Player(Entity):
    def __init__(self, armor: Armor, weapon: Weapon, data: EntityData):
        # Место для дополнения класса Player атрибутами и вызовом инициализатора родительского класса
        __tag = "Player"
        super().__init__(__tag, data, weapon, armor)
        self._hp_bar.bar_color = Colors.green
        self.__location = None
        self.__inventory = Inventory()
        entity_events.Change_Armor += self.change_armor
        entity_events.Change_Weapon += self.change_weapon

    # Место для дополнения класса Player свойствами
    @property
    def location(self):
        return self.__location

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

    @property
    def inventory(self):
        return self.__inventory

    def move(self, cell: Cell):
        self.__location = cell

    def die(self):
        self._is_dead = True

    def change_weapon(self, weapon: Weapon):
        if isinstance(weapon, Weapon):
            self.__inventory.add_item(self.weapon)
            self.weapon = weapon
        else:
            raise EntityItemTypeError

    def change_armor(self, armor: Armor):
        if isinstance(armor, Armor):
            self.__inventory.add_item(self.armor)
            self.armor = armor
        else:
            raise EntityItemTypeError

    def lift_item(self):
        if hasattr(self.__location, "item") and self.__location.item is not None:
            self.__inventory.add_item(self.__location.item)
            entity_events.Lift_Item(self.__location.item)
            self.__location.item = None

    def looting_dead_enemy(self):
        if hasattr(self.__location, "entity") and self.__location.entity is not None and self.__location.entity.is_dead:
            self.__inventory.add_item(self.__location.entity.armor)
            self.__inventory.add_item(self.__location.entity.weapon)
            self.__location.entity.weapon = None
            self.__location.entity.armor = None
            entity_events.Lift_Item(self.__location.entity.weapon)
            entity_events.Lift_Item(self.__location.entity.armor)
