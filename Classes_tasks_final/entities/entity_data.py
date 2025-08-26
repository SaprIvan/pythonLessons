# Место для реализации класса EntityData
class EntityData: #name, description, hp, health и death_description
    def __init__(self, name, description, hp, death_description):
        self.__name = name
        self.__description = description
        self.__health = self.__hp = hp
        self.__death_description = death_description

    @property
    def name(self):
        return self.__name
    @property
    def description(self):
        return self.__description
    @property
    def health(self):
        return self.__health
    @property
    def death_description(self):
        return self.__death_description
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        self.__hp = int(round(value, 0))
