from engine.visual import Colors


# Место для реализации классов BaseItem, Armor, Weapon, Loot
class BaseItem:
    def __init__(self, name, cost, description):
        self.__name = name
        self.__cost = cost
        self.__description = description

    def __str__(self):
        return f"[{self.__name}][{self.__cost}] {self.__description}"

    def get_info(self):
        raise NotImplementedError(f"Метод get_info должен быть реализован у класса: {self.__class__}")

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
                f'[Защита]: {Colors.yellow}{self.defence}{Colors.default}\n'
                f'[Стоимость]: {Colors.yellow}{self.cost}{Colors.default}')

    def get_short_info(self):
        return f'[{self.name}] Защита: {self.defence}'

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
        return (f'[{self.name}]  {self.description}\n'
            f'[Урон]: {Colors.yellow}{self.damage}{Colors.default}\n'
            f'[Шанс попадания] {Colors.yellow}{self.hit_chance}%{Colors.default}\n'
            f'[Стоимость]: {Colors.yellow}{self.cost}{Colors.default}')

    def get_short_info(self):
        return f'[{self.name}] Урон: {self.damage} Шанс попадания: {self.hit_chance}%'

class Loot(BaseItem):
    def get_info(self):
        return (f'[{self.name}] {self.description}\n'
         f'[Стоимость]: {Colors.yellow}{self.cost}{Colors.default}')