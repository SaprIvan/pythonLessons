from engine.visual import Colors

class HealthBar:
    __remaining_health_symbol = '█'
    __lost_health_symbol = '_'
    __bars_count = 20

    def __init__(self, max_health, bar_color):
        self.bar_color = bar_color
        self.max_health = max_health

    def draw(self, hp):
        __health = ''
        __health_lost = ''
        remaining_health_bars = int(round(hp/self.max_health*self.__bars_count,0))
        for _ in range(self.__bars_count):
            if len(__health) < remaining_health_bars:
                __health+=self.__remaining_health_symbol
            else:
                __health_lost += self.__lost_health_symbol
        return f"|{self.bar_color}{ __health}{__health_lost}{Colors.default}|"
