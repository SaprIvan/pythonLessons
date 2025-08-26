# Место для реализации класса Event
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


class AnimationEvents:
    def __init__(self):
        self.Start = Event()


class GameEvents:
    def __init__(self):
        self.Game_Over = Event()


class EntityEvents:
    def __init__(self):
        self.Attack = Event()
        self.Die = Event()
        self.Lift_Item = Event()
        self.Change_Weapon = Event()
        self.Change_Armor = Event()


animation_events = AnimationEvents()
entity_events = EntityEvents()
game_events = GameEvents()