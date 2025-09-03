from time import sleep

from dataclasses import dataclass, field
from engine.events import animation_events


# Место для реализации классов TextAnimation и AnimationController
@dataclass
class TextAnimation:
    states: list[any] = field(default_factory=list)
    attempts: int = 1
    interval: float = 3.0

    def play(self):
        animation_events.Start(self.states, self.attempts, self.interval)

class AnimationController:
    def __init__(self):
        animation_events.Start += self.animation

    def animation(self, states: list[any], attempts: int, interval: float):
        for attempt in range(attempts):
            for state in states:
                print(state, end="")
                sleep(interval)
                print("\r", end="")
        print(end="\n")



animator = AnimationController()