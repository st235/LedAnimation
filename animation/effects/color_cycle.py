from animation.animation import Animation
from animation.color import Color
from animation.color_context import ColorContext
from animation.micropyton.typing import Union

class ColorCycle(Animation):
    def __init__(self, colors: list[Color], update_intervals_ms: Union[float, list[float]]):
        super().__init__(update_intervals_ms=update_intervals_ms)
        assert len(colors) > 0
        self.__selected_color_index = 0
        self.__colors = colors

    def __on_start(self, context: ColorContext):
        self.__selected_color_index = 0

    def _on_update(self, context: ColorContext, dt: float):
        context.clear(self.__colors[self.__selected_color_index])
        self.__selected_color_index = (self.__selected_color_index + 1) % len(self.__colors)
