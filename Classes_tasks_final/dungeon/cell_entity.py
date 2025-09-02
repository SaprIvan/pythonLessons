from typing import Optional

from engine.geometry import Direction, Vector2
from engine.visual import CellType
from entities.entity import Entity
from entities.items import BaseItem


# Место для реализации классов CellFillingError и Cell
class CellFillingError(Exception):
    def __str__(self):
        return "Возникла ошибка наполнения ячейки сущностями. Проверьте, что передается верный тип данных."


class Cell:
    def __init__(self, position: Vector2, cell_type: str):
        self.__position = position
        self.__cell_type = cell_type
        self.__entity = None
        self.__item = None
        self.__is_start_cell = self.__cell_type == CellType.start
        self.__is_end_cell = self.__cell_type == CellType.end
        self.__description = ""
        self.__neighbours = []

    @property
    def position(self):
        return self.__position

    @property
    def cell_type(self):
        return self.__cell_type

    @property
    def entity(self):
        return self.__entity

    @property
    def item(self):
        return self.__item

    @property
    def is_start_cell(self):
        return self.__is_start_cell

    @property
    def is_end_cell(self):
        return self.__is_end_cell

    @property
    def description(self):
        return self.__description

    @property
    def neighbours(self):
        return self.__neighbours

    @cell_type.setter
    def cell_type(self, cell_type):
        if isinstance(cell_type, str):
            self.__cell_type = cell_type
        else:
            raise CellFillingError

    @entity.setter
    def entity(self, entity):
        if isinstance(entity, Entity):
            self.__entity = entity
        else:
            raise CellFillingError

    @item.setter
    def item(self, item):
        if isinstance(item, BaseItem) or item is None:
            self.__item = item
        else:
            raise CellFillingError

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self.__description = description
        else:
            raise CellFillingError

    @neighbours.setter
    def neighbours(self, neighbours):
        if isinstance(neighbours, list) and len(neighbours) == 8:
            self.__neighbours = neighbours
        else:
            raise CellFillingError

    def get_neighbour(self, index):
        return self.__neighbours[index]

    def set_neighbour(self, direction: int, cell: "Cell"):
        if len(self.__neighbours) == 0:
            for _ in range(0,8):
                self.__neighbours.append(None)
            self.__neighbours[direction] = cell
        if len(cell.neighbours) == 0:
            for _ in range(0, 8):
                cell.neighbours.append(None)
            opp = Direction.opposite(direction)
            cell.__neighbours[opp] = self


    def __repr__(self):
        return self.__cell_type