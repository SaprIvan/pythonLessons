# место для вашей реализации
class Event:
    def __init__(self):
        self.__handlers = []

    def __iadd__(self, func):
        self.__handlers.append(func)
        return self

    def __isub__(self, func):
        self.__handlers.remove(func)
        return self

    def __call__(self, *args, **kwargs):
        for func in self.__handlers:
            func(*args, **kwargs)
        return self


# Пример использования
class Events(object):
    ev_die = Event()    # создается инстанс события. В аргументе ev_die находится экземпляр класса Event

class Entity:
    def __init__(self):
        self.name = 'Герман из Ливии'
        self.hp = 10
        self.health = self.hp

    def taking_damage(self, damage):
        self.hp -= damage
        if damage > self.hp:
            self.hp = 0
        print(f'[{self.name}] получил "{damage}" урона. Здоровье: {self.hp}/{self.health}')
        if self.hp <= 0:
            # За счет переопределенного метода __call__ у класса Event, мы можем вызвать его, как функцию,
            # и передать аргументом экземпляр класса Entity, чтобы использовать его атрибуты при выводе сообщения об окончании игры.
            Events.ev_die(self)    # Вызовем событие, когда hp станет 0 или меньше.


class GameLoop:
    def __init__(self):
        self.is_running = True
        # За счет переопределенного метода __iadd__ в классе Event, мы можем использовать оператор +=.
        # Он добавит объект функции game_over в приватный атрибут handlers класса Event.
        Events.ev_die += self.game_over

    def game_over(self, entity):
        # game_over - это функция, которая должна отработать, когда вызовется событие ev_die.
        # Поскольку, при вызове события, передается экземпляр класса Entity, функция game_over должна иметь аргумент, принимающий этот экземпляр.
        print(f'[{entity.name}] Персонаж умер. Игра окончена...')
        self.is_running = False

    def run(self):
        entity = Entity()
        while self.is_running:
            entity.taking_damage(1)


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert hasattr(Events.ev_die, '_Event__handlers'), f'Класс Event должен иметь динамический приватный атрибут handlers.'
    assert isinstance(getattr(Events.ev_die, '_Event__handlers'), list), f'Приватный атрибут handlers, класса Event, должен иметь тип list.'
    assert not getattr(Events.ev_die, '_Event__handlers'), f'Список из приватного атрибута handlers, класса Event, должен быть пустым при создании экземпляра класса.'

    def func():
        pass

    Events.ev_die += func
    assert len(getattr(Events.ev_die, '_Event__handlers')) == 1, f'После подписка, объект функции не добавился в приватный атрибут handlers, класса Event.'
    Events.ev_die -= func
    assert not getattr(Events.ev_die, '_Event__handlers'), f'После отписки, объект функции не удалился из приватного атрибута handlers, класса Event.'
    # вывод в терминал результата
    print(f'Все тесты прошли, класс реализован верно.')
    game = GameLoop()
    game.run()