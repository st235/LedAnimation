from animation.animation import Animation
from animation.color import Color
from animation.color_context import ColorContext


class ColorCycle(Animation):
    def __init__(self, colors: list[Color], single_cycle_ms: float):
        super().__init__(single_cycle_ms=single_cycle_ms)
        assert len(colors) > 0
        self.__currently_selected = 0
        self.__colors = colors


    def _on_update(self, context: ColorContext, dt: float):
        context.clear(self.__colors[self.__currently_selected])
        self.__currently_selected = (self.__currently_selected + 1) % len(self.__colors)
