class Ship:
    def __init__(self, name,ship_type, damage):
        self.name = name
        self.ship_type = ship_type
        self.damage = damage

    @classmethod
    def deserialize(cls, data):
        return cls(name=data['name'], ship_type=data['ship_type'], damage=data['damage'])


    def serialize(self):
        return {'name':self.name, 'ship_type':self.ship_type, 'damage':self.damage}

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    from random import randint
    data = {'name': 'Аврора', 'ship_type': 'Крейсер', 'damage': randint(1, 100)}
    ship = Ship.deserialize(data)
    import inspect
    assert inspect.ismethod(Ship.deserialize), 'Метод deserialize должен быть методом класса (@classmethod)'
    assert isinstance(ship, Ship), f'Метод класса deserialize должен создавать экземпляр класса Ship из переданных данных'
    dinamic_attrs = ship.__dict__
    assert 'name' in dinamic_attrs and 'ship_type' in dinamic_attrs and 'damage' in dinamic_attrs,\
        f'Класс Ship должен иметь динамические атрибуты: name, ship_type, damage.'
    assert ship.name == data.get('name') and ship.ship_type == data.get('ship_type') and ship.damage == data.get('damage'), \
        f'Атрибуты должны иметь значения из {data}, а были {ship.__dict__}'
    assert ship.serialize() == data, 'Сериализованные данные должны быть такими же, из которх была десериализаций. Проверьте метод serialize'

    # вывод в терминал результата
    print(f'Все тесты прошли, класс реализован верно.')