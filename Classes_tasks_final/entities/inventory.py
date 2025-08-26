from entities.items import BaseItem


# Место для реализации класса Inventory
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

    @property
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