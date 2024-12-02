from animation.animation import Animation
from animation.color import Color, lerp
from animation.color_context import ColorContext


class GradientCycle(Animation):
    def __init__(self, colors: list[Color], single_transition_duration_ms: float):
        # Request update every possible time.
        super().__init__(single_cycle_ms=None)

        assert len(colors) > 0

        self.__current_selection_index = 0
        self.__colors = colors
        self.__single_transition_duration_ms = single_transition_duration_ms

        self.__current_time = 0


    def _on_update(self, context: ColorContext, dt: float):
        current_color = self.__colors[self.__current_selection_index]
        next_color = self.__colors[(self.__current_selection_index + 1) % len(self.__colors)]
        context.clear(lerp(start=current_color,
                           end=next_color,
                           progress=self.__current_time / self.__single_transition_duration_ms))

        self.__current_time += dt
        if self.__current_time > self.__single_transition_duration_ms:
            self.__current_time = 0
            self.__current_selection_index = (self.__current_selection_index + 1) % len(self.__colors)
