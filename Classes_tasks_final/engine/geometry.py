class Vector2:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


class __Direction:
    def __init__(self):
        self.__N = 0
        self.__NE = 1
        self.__E = 2
        self.__SE = 3
        self.__S = 4
        self.__SW = 5
        self.__W = 6
        self.__NW = 7

    @property
    def N(self):
        return self.__N

    @property
    def NE(self):
        return self.__NE

    @property
    def E(self):
        return self.__E

    @property
    def SE(self):
        return self.__SE

    @property
    def S(self):
        return self.__S

    @property
    def SW(self):
        return self.__SW

    @property
    def W(self):
        return self.__W

    @property
    def NW(self):
        return self.__NW

    @staticmethod
    def opposite(direction: int) -> int:
        return direction + 4 if direction < 4 else direction - 4

    def direction_from_int(self, direction: int):
        directions = {
            self.N: 'Север',
            self.NE: 'Северо-Восток',
            self.E: 'Восток',
            self.SE: 'Юго-Восток',
            self.S: 'Юг',
            self.SW: 'Юго-Запад',
            self.W: 'Запад',
            self.NW: 'Северо-Запад',
        }
        return directions[direction]

    def direction_from_string(self, direction: str) -> int:
        directions = {
            'Север': self.N,
            'Северо-Восток': self.NE,
            'Восток': self.E,
            'Юго-Восток': self.SE,
            'Юг': self.S,
            'Юго-Запад': self.SW,
            'Запад': self.W,
            'Северо-Запад': self.NW,
        }
        return directions[direction]


Direction = __Direction()