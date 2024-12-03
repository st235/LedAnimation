from animation.micropyton.typing import Union

from animation.animation import Animation
from animation.color import Color, lerp
from animation.color_context import ColorContext


class GradientCycle(Animation):
    def __init__(self, colors: list[Color], single_transition_duration_ms: Union[float, list[float]]):
        # Request update every possible time.
        super().__init__(update_intervals_ms=None)

        if isinstance(single_transition_duration_ms, int) or isinstance(single_transition_duration_ms, float):
            self.__single_transition_durations_ms = [float(single_transition_duration_ms)]
        else:
            self.__single_transition_durations_ms = single_transition_duration_ms

        assert len(colors) > 0
        self.__colors = colors

        self.__selected_color_index = 0
        self.__current_transition_duration_index = 0
        self.__current_time_ms = 0.0

    def _on_start(self, context: ColorContext):
        self.__selected_color_index = 0
        self.__current_transition_duration_index = 0
        self.__current_time_ms = 0.0

    def _on_update(self, context: ColorContext, dt: float):
        current_transition_time_ms = self.__single_transition_durations_ms[self.__current_transition_duration_index]

        current_color = self.__colors[self.__selected_color_index]
        next_color = self.__colors[(self.__selected_color_index + 1) % len(self.__colors)]
        context.clear(lerp(start=current_color,
                           end=next_color,
                           progress=self.__current_time_ms / current_transition_time_ms))

        self.__current_time_ms += dt
        if self.__current_time_ms > current_transition_time_ms:
            self.__current_time_ms = 0.0
            self.__selected_color_index = (self.__selected_color_index + 1) % len(self.__colors)
            self.__current_transition_duration_index = \
                (self.__current_transition_duration_index + 1) % len(self.__single_transition_durations_ms)
