from animation.animation import Animation
from animation.color import Color

class ColorCycle(Animation):
    def __init__(self, colors: list[Color], update_cycle_time_ms: float):
        super().__init__(update_cycle_time_ms= update_cycle_time_ms)

        self.__colors = colors

    def update(self):
        ...
