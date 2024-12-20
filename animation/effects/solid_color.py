from animation.animation import Animation
from animation.color import Color
from animation.color_context import ColorContext


class SolidColor(Animation):
    def __init__(self, color: Color):
        super().__init__(update_intervals_ms=None)
        self.__color = color

    def _on_update(self, context: ColorContext, dt: float):
        context.clear(self.__color)

