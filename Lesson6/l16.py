from Lesson6.l10 import Colors

class BaseItem:
    def __init__(self, name, cost, description):
        self.__name = name
        self.__cost = cost
        self.__description = description

    def __str__(self):
        return f"[{self.__name}][{self.__cost}] {self.__description}"

    def get_info(self):
        return NotImplementedError(f"Метод get_info должен быть реализован у класса: {self.__class__.__name__}")

    @property
    def name(self):
        return self.__name
    @property
    def cost(self):
        return self.__cost
    @property
    def description(self):
        return self.__description

class Armor(BaseItem):
    def __init__(self, name, cost, description, defence):
        super().__init__(name, cost, description)
        self.__defence = defence

    @property
    def defence(self):
        return self.__defence

    def get_info(self):
        return (f'[{self.name}] {self.description}\n'
                f'[Защита]: {Colors.yellow()}{self.defence}{Colors.default()}\n'
                f'[Стоимость]: {Colors.yellow()}{self.cost}{Colors.default()}')

    def get_short_info(self):
        return f'[{name}] Защита: {defence}'

class Weapon(BaseItem):
    def __init__(self, name, cost, description, damage, hit_chance):
        super().__init__(name, cost, description)
        self.__hit_chance = hit_chance
        self.__damage = damage

    @property
    def damage(self):
        return self.__damage
    @property
    def hit_chance(self):
        return self.__hit_chance

    def get_info(self):
        return (f'[{name}]  {description}\n'
            f'[Урон]: {Colors.yellow()}{damage}{Colors.default()}\n'
            f'[Шанс попадания] {Colors.yellow()}{hit_chance}%{Colors.default()}\n'
            f'[Стоимость]: {Colors.yellow()}{cost}{Colors.default()}')

    def get_short_info(self):
        return f'[{name}] Урон: {damage} Шанс попадания: {hit_chance}%'

class Loot(BaseItem):
    def get_info(self):
        return (f'[{name}] {description}\n'
         f'[Стоимость]: {Colors.yellow()}{cost}{Colors.default()}')

class Inventory:
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    def add_item(self, item):
        if isinstance(item, BaseItem):
            self.__items.append(item)

    def remove_item(self, item):
        if isinstance(item, BaseItem):
            self.__items.remove(item)
        return item

    def items_count(self):
        return len(self.items) if self.__items else 0

    def draw_all_items(self):
        result = ""
        for item in self.__items:
            result += f'-------------------\n{item.get_info()}\n-------------------'
        return result
    def calculate_items_costs(self):
        total_cost = 0
        for item in self.__items:
            total_cost += item.cost
        return total_cost

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    inventory = Inventory()
    assert hasattr(inventory, '_Inventory__items'), 'Атрибут __items у класса Inventory, должен быть приватным.'
    assert len(getattr(inventory, '_Inventory__items')) == 0, 'При создании экземпляра класса Inventory, список предметов должен быть пустым'
    assert inventory.items_count() == 0, \
        f'Свойство items_count у класса Inventory, при пустом списке __items, должен был вернуть 0, а вернул {inventory.items_count}'

    inventory.add_item('Item')
    assert inventory.items_count() == 0, f'Добавлять в инвентарь можно только предметы типа BaseItem'

    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    light_armor = Armor(name=name,cost=cost, description=description, defence=defence)

    expected_msg = (f'[{name}] {description}\n'
                    f'[Защита]: {Colors.yellow()}{defence}{Colors.default()}\n'
                    f'[Стоимость]: {Colors.yellow()}{cost}{Colors.default()}')
    assert light_armor.get_info() == expected_msg, \
        f'Проверьте корректность возвращаемой строки методом get_info у класса Armor. Ожидалось\n: {expected_msg}, а было\n{light_armor.get_info()}'
    expected_msg = f'[{name}] Защита: {defence}'
    assert light_armor.get_short_info() == expected_msg, \
        f'Проверьте корректность возвращаемой строки методом get_short_info у класса Armor. Ожидалось\n: {expected_msg}, а было\n{light_armor.get_short_info()}'

    inventory.add_item(light_armor)
    assert inventory.items_count() == 1, \
        f'После добавления элемента в пустой инвентарь с помощью метода add_item, свойство items_count должно было вернуть 1, а вернуло {inventory.items_count}'
    name, description = 'Опасная дубина', 'Крепкая сосновая ветка с вбитым ржавым гвоздем на конце.'
    cost, damage, hit_chance = 4, 5, 75
    club = Weapon(name=name,cost=cost, description=description, damage=damage, hit_chance=hit_chance)
    expected_msg = (f'[{name}]  {description}\n'
                    f'[Урон]: {Colors.yellow()}{damage}{Colors.default()}\n'
                    f'[Шанс попадания] {Colors.yellow()}{hit_chance}%{Colors.default()}\n'
                    f'[Стоимость]: {Colors.yellow()}{cost}{Colors.default()}')
    assert club.get_info() == expected_msg, \
        f'Проверьте корректность возвращаемой строки методом get_info у класса Weapon. Ожидалось\n: {expected_msg}, а было\n{club.get_info()}'
    expected_msg = f'[{name}] Урон: {damage} Шанс попадания: {hit_chance}%'
    assert club.get_short_info() == expected_msg, \
        f'Проверьте корректность возвращаемой строки методом get_info у класса Weapon. Ожидалось\n: {expected_msg}, а было\n{club.get_short_info()}'

    inventory.add_item(club)
    assert len(getattr(inventory, '_Inventory__items')) == 2, 'После использования метода add_item, количество предметов в списке items не увеличелось.'
    removed_light_armor = inventory.remove_item(light_armor)
    assert len(getattr(inventory, '_Inventory__items')) == 1, 'После использования метода remove_item, количество предметов в списке items не уменьшилось.'
    assert removed_light_armor == light_armor, f'Метод remove_item класса Inventory, должен возвращать удаляемый объект. Почитайте про метод списков "pop".'
    inventory.add_item(light_armor)
    expected_msg = f'-------------------\n{club.get_info()}\n--------------------------------------\n{light_armor.get_info()}\n-------------------'
    assert inventory.draw_all_items() == expected_msg, \
        f'Ожидалось, что метод draw_all_items у класса Inventory сформирует строку:\n{expected_msg}, а сформировал:\n{inventory.draw_all_items()}'
    assert inventory.calculate_items_costs() == 14, \
        (f'При добавлении в пустой инвентарь двух предметов стоимостью 10 и 4, метод calculate_items_costs класса '
         f'Inventory должен был вернуть 14, а вернул {inventory.calculate_items_costs()}')

    class TestClass(BaseItem):
        pass

    test_class = TestClass('', '', 0)
    try:
        test_class.get_info()
        assert 'В случае, когда не переопределен метод get_info в классе наследнике, ожидалось исключение NotImplementedError, но его не было.'
    except NotImplementedError as e:
        message = e.args[0]
        assert message == f'Метод get_info должен быть реализован у класса: {test_class.__class__}', \
            f'Проверьте корретность сообщение об ошибке NotImplementedError в методе get_info класса BaseItem. Сейчас выкидывается сообщение "{message}"'

    name, description = 'Грязный амулет', 'Почерневший серебряный амулет с пустым гнездом под драгоценный камень.'
    cost = 3
    amulet = Loot(name=name, description=description, cost=cost)
    expected_msg = (f'[{name}] {description}\n'
                    f'[Стоимость]: {Colors.yellow()}{cost}{Colors.default()}')
    assert amulet.get_info() == expected_msg, \
        f'Проверьте корректность возвращаемой строки методом get_info у класса Loot. Ожидалось\n: {expected_msg}, а было\n{amulet.get_info()}'

    # вывод в терминал результата
    print(f'Все тесты прошли, классы реализованы верно.')
    print(inventory.draw_all_items())
    print('=============================')