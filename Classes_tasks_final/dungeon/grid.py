from dungeon.cell_entity import Cell
from engine.geometry import Vector2, Direction


class Grid:
    def __init__(self, size_x: int, size_y: int):
        self.size_x = size_x
        self.size_y = size_y
        self.cells = []

    def create_map(self, pattern: list[list[str]]):
        self.cells = pattern.copy()
        for y in range(len(pattern)):
            for x in range(len(pattern[y])):
                cell = self.__create_cell(x, y, pattern[y][x])
                self.cells[y][x] = cell
        self.cells.reverse()

    def __create_cell(self, x, y, cell_type):
        cell = Cell(
            position=Vector2(x, y),
            cell_type=cell_type
        )
        if x > 0:
            cell.set_neighbour(Direction.W, cell=self.cells[y][x - 1])
        if y > 0:
            cell.set_neighbour(Direction.S, cell=self.cells[y - 1][x])
            if x > 0:
                cell.set_neighbour(Direction.SW, cell=self.cells[y - 1][x - 1])
            if x < self.size_x - 1:
                cell.set_neighbour(Direction.SE, cell=self.cells[y - 1][x + 1])

        return cell
