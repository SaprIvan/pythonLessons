class BaseItem:
    pass

class CellFillingError(Exception):
    def __str__(self):
        return "Возникла ошибка наполнения ячейки сущностями. Проверьте, что передается верный тип данных."

class Cell:
    def __init__(self):
        self.__item = None

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, value):
        if isinstance(value, BaseItem):
            self.__item = value
        else:
            raise CellFillingError


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    cell = Cell()
    assert cell.item is None, 'При создании экземпляра класса Cell, атрибут item должен быть None'
    item = BaseItem()
    cell.item = item
    assert isinstance(item, BaseItem), 'Проверьте корректность работы сеттера. После присвоения значения атрибуту item, значение не присвоилось.'
    try:
        cell = Cell()
        cell.item = 'BaseItem'
        assert cell.item is None, 'Проверьте корректность работы сеттера. Атрибуту item разрешено по заданию присваивать значения, которые имеют тип BaseItem'
    except CellFillingError as e:
        assert str(e) == f'Возникла ошибка наполнения ячейки сущностями. Проверьте, что передается верный тип данных.', \
            f'Проверьте корректность сообщения в кастомной ошибке CellFillingError. Была ошибка "{e}"'

    # вывод в терминал результата
    print(f'Все тесты прошли, класс реализован верно.')