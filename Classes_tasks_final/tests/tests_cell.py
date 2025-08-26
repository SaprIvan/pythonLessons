from dungeon.cell_entity import Cell, CellFillingError
from engine.geometry import Direction, Vector2
from engine.visual import CellType, Colors
from entities.entity import EntityData, Entity
from dungeon.grid import Grid
from entities.items import BaseItem, Armor, Weapon


def test_cell_initialization():
    position = Vector2(0, 0)
    cell = Cell(position=position, cell_type=CellType.wall)
    assert cell.position == position, f"При инициализации класса Cell c 'position={position}', свойство position должно было вернуть {position}, фактически вернуло {cell.position}"
    assert cell.cell_type == CellType.wall, (f"При инициализации класса Cell c 'cell_type={CellType.wall}', "
                                                   f"свойство cell_type должно было вернуть {CellType.wall}, фактически вернуло {cell.cell_type}")
    assert cell.entity is None, f"При инициализации класса Cell, свойство entity должно было вернуть None, фактически вернуло {cell.entity}"
    assert cell.item is None, f"При инициализации класса Cell, свойство item должно было вернуть None, фактически вернуло {cell.item}"
    assert not cell.is_start_cell, f"При инициализации класса Cell с 'cell_type={CellType.wall}', свойство is_start_cell должно было вернуть False, фактически вернуло {cell.is_start_cell}"
    assert not cell.is_end_cell, f"При инициализации класса Cell с 'cell_type={CellType.wall}', свойство is_end_cell должно было вернуть False, фактически вернуло{cell.is_end_cell}"
    assert cell.description == '', f"При инициализации класса Cell, свойство description должно было вернуть пустую строку, фактически вернуло {cell.description}"
    assert cell.neighbours == [], f"При инициализации класса Cell, свойство neighbours должно было вернуть пустой список, фактически вернуло {cell.neighbours}"


def test_cell_private_attributes():
    position = Vector2(0, 0)
    cell = Cell(position=position, cell_type=CellType.wall)
    assert hasattr(cell, '_Cell__position'), "У класса Cell должен быть приватный атрибут __position"
    assert hasattr(cell, '_Cell__cell_type'), "У класса Cell должен быть приватный атрибут __cell_type"
    assert hasattr(cell, '_Cell__entity'), "У класса Cell должен быть приватный атрибут __entity"
    assert hasattr(cell, '_Cell__item'), "У класса Cell должен быть приватный атрибут __item"
    assert hasattr(cell, '_Cell__is_start_cell'), "У класса Cell должен быть приватный атрибут __is_start_cell"
    assert hasattr(cell, '_Cell__is_end_cell'), "У класса Cell должен быть приватный атрибут __is_end_cell"
    assert hasattr(cell, '_Cell__description'), "У класса Cell должен быть приватный атрибут __description"
    assert hasattr(cell, '_Cell__neighbours'), "У класса Cell должен быть приватный атрибут __neighbours"

    assert cell._Cell__position == position, f"При инициализации класса Cell c 'position={position}', приватный атрибут __position должен хранить в себе {position}, фактически было {cell._Cell__position}"
    assert cell._Cell__cell_type == CellType.wall, f"При инициализации класса Cell c 'cell_type={CellType.wall}', приватный атрибут __cell_type должен хранить в себе {CellType.wall}, фактически было {cell._Cell__cell_type}"
    assert cell._Cell__entity is None, f"При инициализации класса Cell, приватный атрибут __entity должен быть None, фактически был {cell._Cell__entity}"
    assert cell._Cell__item is None, f"При инициализации класса Cell, приватный атрибут __item должен быть None, фактически был {cell._Cell__item}"
    assert not cell._Cell__is_start_cell, f"При инициализации класса Cell c 'cell_type={CellType.wall}', приватный атрибут __is_start_cell должен быть False, фактически был {cell._Cell__is_start_cell}"
    assert not cell._Cell__is_end_cell, f"При инициализации класса Cell c 'cell_type={CellType.wall}', приватный атрибут __is_end_cell должен быть False, фактически был {cell._Cell__is_end_cell}"
    assert cell._Cell__description == '', f"При инициализации класса Cell, приватный атрибут __description должен быть пустой строкой, фактически был {cell.description}"
    assert cell._Cell__neighbours == [], f"При инициализации класса Cell, приватный атрибут __neighbours должен быть пустым списком, фактически был {cell.neighbours}"


def test_cell_type_property():
    position = Vector2(0, 0)
    cell = Cell(position, CellType.empty_room)
    cell.cell_type = CellType.wall
    assert cell.cell_type == CellType.wall, (f"При изменении типа ячейки c {CellType.empty_room} на {CellType.wall}, "
                                             f"значение в атрибуте cell_type должно было измениться на {CellType.wall}, но не изменилось. Проверьте сеттер для cell_type")


def test_entity_setter():
    position = Vector2(0, 0)
    cell = Cell(position, CellType.empty_room)
    entity_data = EntityData(name="Goblin", hp=50, description="A small, green creature.", death_description="The goblin lies motionless on the ground.")
    entity = Entity(tag="Goblin", armor=Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=10), weapon=Weapon(name="Rusty Sword", description="A slightly rusted sword.", cost=30, damage=10, hit_chance=70), data=entity_data)
    cell.entity = entity
    assert cell.entity == entity, (f"При изменении значения для атрибута entity c None на {entity}, "
                                   f"значение в атрибуте entity должно было измениться на {entity}, но не изменилось. Проверьте сеттер для entity")

    try:
        cell.entity = "Not an entity"
        assert False, "Должно вызвать исключение CellFillingError, при попытке установить значение с типом отличным от Entity для атрибута entity класса Cell"
    except CellFillingError:
        pass


def test_item_setter():
    position = Vector2(0, 0)
    cell = Cell(position, CellType.empty_room)
    item = BaseItem(name="Health Potion", description="Restores 20 HP.", cost=20)
    cell.item = item
    assert cell.item == item, (f"При изменении значения для атрибута item c None на {item}, "
                               f"значение в атрибуте item должно было измениться на {item}, но не изменилось. Проверьте сеттер для item")
    cell.item = None
    assert cell.item is None, ("При изменении значения для атрибута item на None, значение в атрибуте item должно"
                               " было измениться на None, но не изменилось. Проверьте сеттер для item")

    try:
        cell.item = "Not an item"
        assert False, "Должно вызвать исключение CellFillingError, при попытке установить значение с типом отличным от BaseItem или None для атрибута item класса Cell"
    except CellFillingError:
        pass


def test_is_start_cell():
    position = Vector2(0, 0)
    start_cell = Cell(position, CellType.start)
    assert start_cell.is_start_cell, f"При инициализации класса Cell с 'cell_type={CellType.start}', свойство is_start_cell класса Cell должно было вернуть True"
    assert not start_cell.is_end_cell, f"При инициализации класса Cell с 'cell_type={CellType.start}', свойство is_end_cell класса Cell должно было вернуть False"


def test_is_end_cell():
    position = Vector2(0, 0)
    end_cell = Cell(position, CellType.end)
    assert end_cell.is_end_cell, f"При инициализации класса Cell с 'cell_type={CellType.end}', свойство is_end_cell класса Cell должно было вернуть True"
    assert not end_cell.is_start_cell, f"При инициализации класса Cell с 'cell_type={CellType.end}', свойство is_start_cell класса Cell должно было вернуть False"


def test_get_neighbour():
    position = Vector2(0, 0)
    cell = Cell(position, CellType.empty_room)
    cell.neighbours = [Direction.N, Direction.NE, Direction.E, Direction.SE, Direction.S, Direction.SW, Direction.W, Direction.NW]
    for direction in [Direction.N, Direction.NE, Direction.E, Direction.SE, Direction.S, Direction.SW, Direction.W, Direction.NW]:
        assert cell.get_neighbour(direction) == direction, f'Некорректное получение соседа в направлении {direction}, с помощью метода get_neighbour класса Cell'


def test_set_neighbour():
    position = Vector2(0, 0)
    cell = Cell(position, CellType.empty_room)
    neighbour_position = Vector2(x=1, y=0)
    neighbour_cell = Cell(neighbour_position, CellType.empty_room)
    cell.set_neighbour(Direction.E, neighbour_cell)
    assert cell.get_neighbour(Direction.E) == neighbour_cell, f"При установке единственного соседа с востока, сосед на востоке должен быть {neighbour_cell}, фактически был {cell.get_neighbour(Direction.E)}"
    assert len([neighbour for neighbour in cell.neighbours if neighbour is None]) == 7, f'При установке единственного соседа с востока, все остальные соседи в списке должны были быть None. Фактически список соседей: {cell.neighbours}'
    assert neighbour_cell.get_neighbour(Direction.W) == cell, f"Для соседа текущей ячейки с востока, сосед на западе должен быть текущей ячейкой. Посмотрите еще раз на поясняющие картинки из задания."


def test_cell_representation():
    position = Vector2(0, 0)
    cell = Cell(position, CellType.empty_room)
    assert repr(cell) == CellType.empty_room, f"Магические метод __repr__ класса Cell должен возвращать {CellType.empty_room}, фактически вернул {repr(cell)}"


def print_map():
    pattern = [
        ['⏩', '  ', '💎'],
        ['🧱', '⚔️', '🧱'],
        ['⏪', '  ', '🧱']
    ]
    grid = Grid(3, 3)
    grid.create_map(pattern)
    for line in grid.cells:
        print(f'{line}')


def run_cell_tests():
    print(f'{Colors.yellow}===Тестируем класс Cell==={Colors.default}')
    test_cell_initialization()
    test_cell_private_attributes()
    test_cell_type_property()
    test_entity_setter()
    test_item_setter()
    test_is_start_cell()
    test_is_end_cell()
    test_get_neighbour()
    test_set_neighbour()
    test_cell_representation()
    print(f'{Colors.green}+++Все тесты прошли, класс Cell реализован верно.+++{Colors.default}')
    print_map()
    print('====================')
