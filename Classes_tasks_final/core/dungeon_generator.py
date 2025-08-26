from dungeon.grid import Grid
from engine.configs import GameConfig
from core.entities_loader import EntitiesLoader
from engine.visual import CellType


class DungeonGenerator:
    def __init__(self, config: GameConfig):
        self.__entities_loader = EntitiesLoader()
        self.__grid = Grid(config.map_size_x, config.map_size_y)
        self.__player = None
        self.__init_map(config)
        self.__init_entities()

    @property
    def grid(self):
        return self.__grid

    @property
    def player(self):
        return self.__player

    def draw_map(self):
        board = f'{"====" * len(self.grid.cells[0])}='
        print(board)
        for line in self.grid.cells:
            print(f'{line}')
        print(board)
        print(f'Вход: {CellType.start}\n'
              f'Выход: {CellType.end}\n'
              f'Стена: {CellType.wall}\n'
              f'Монстр: {CellType.enemy}\n'
              f'Лут: {CellType.item}\n'
              f'Персонаж: {CellType.player}')
        print(board)

    def __init_map(self, config: GameConfig):
        self.grid.create_map(config.pattern)

    def __init_entities(self) -> None:
        self.__player = self.__entities_loader.create_random_player()
        for line in self.grid.cells:
            for cell in line:
                cell.description = self.__entities_loader.get_random_room_description()
                if cell.cell_type == CellType.enemy:
                    cell.entity = self.__entities_loader.create_random_enemy()
                if cell.cell_type == CellType.item:
                    cell.item = self.__entities_loader.create_random_item()
                if cell.is_start_cell:
                    self.__player.move(cell)
