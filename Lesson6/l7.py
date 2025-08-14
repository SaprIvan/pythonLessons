class GeoLocation:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class Ship:
    def __init__(self, name, coordinates = GeoLocation(0,0)):
        self.name = name
        self.coordinates = coordinates

def create_ship():
    ship = Ship(name='Аврора')
    ship.coordinates = GeoLocation(latitude=45.70, longitude=56.30)
    return ship


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    ship = create_ship()
    assert isinstance(ship, Ship), 'Функция create_ship должна возвращать объект типа Ship.'
    assert isinstance(ship.coordinates, GeoLocation), 'Атрибут coordinates класса Ship должен иметь тип GeoLocation.'
    assert hasattr(ship, 'name') and hasattr(ship,
                                             'coordinates'), 'Класс Ship должен содержать атрибуты name и coordinates'
    assert hasattr(ship.coordinates, 'latitude') and hasattr(ship.coordinates,
                                                             'longitude'), 'Класс GeoLocation должен содержать атрибуты latitude и longitude'
    assert not 'name' in Ship.__dict__ and not 'coordinates' in Ship.__dict__, 'Атрибуты класса Ship должны быть динамическими, а не статическими.'
    assert not 'latitude' in GeoLocation.__dict__ and not 'longitude' in GeoLocation.__dict__, 'Атрибуты класса GeoLocation должны быть динамическими, а не статическими.'
    # вывод в терминал результата
    print(
        f'Твой корабль: "{ship.name}". Сейчас он находится по координатам: [широта:{ship.coordinates.latitude}, долгота:{ship.coordinates.longitude}]')