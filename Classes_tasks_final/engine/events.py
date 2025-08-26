# Место для реализации класса Event


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