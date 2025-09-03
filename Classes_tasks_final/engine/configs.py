from dataclasses import dataclass
from typing import List


@dataclass
class GameConfig:
    name: str
    pattern: List[List[str]]


    def  __post_init__(self):
        self.map_size_x: int = len(self.pattern)
        self.map_size_y: int = len(self.pattern[0])

    def __str__(self):
        return f'[{self.name}] Размер карты: {self.map_size_x}x{self.map_size_y}'
