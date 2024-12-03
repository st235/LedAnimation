import random

from animation.animation import Animation
from animation.color import Color
from animation.color_context import ColorContext


class Progress(Animation):
    def __init__(self,
                 progress_colors: list[Color],
                 background_color: Color,
                 progress_speed_ms: float,
                 stop_when_completed: bool = False):
        # Request update every possible time.
        super().__init__(update_intervals_ms=progress_speed_ms)

        assert len(progress_colors) > 0

        self.__progress_colors = progress_colors
        self.__background_color = background_color
        self.__stop_when_completed = stop_when_completed

    def _on_start(self, context: ColorContext):
        context.clear(self.__background_color)
        self.__current_index = 0

    def _on_update(self, context: ColorContext, dt: float):
        if self.__current_index == 0:
            context.clear(self.__background_color)

        context[self.__current_index] = random.choice(self.__progress_colors)

        if not self.__stop_when_completed and self.__current_index == (len(context) - 1):
            self.__current_index = 0
        elif self.__current_index < (len(context) - 1):
            self.__current_index += 1


