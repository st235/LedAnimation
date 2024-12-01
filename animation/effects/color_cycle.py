import random

from animation.animation import Animation
from animation.color import Color
from animation.color_context import ColorContext


class ColorCycle(Animation):
    def __init__(self, colors: list[Color], single_cycle_ms: float):
        super().__init__(single_cycle_ms=single_cycle_ms)
        self.__colors = colors

    def _on_update(self, context: ColorContext):
        context.fill(color=random.choice(self.__colors))
