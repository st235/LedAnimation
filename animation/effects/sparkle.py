import random

from animation.animation import Animation
from animation.color import Color, lerp
from animation.color_context import ColorContext


class Sparkle(Animation):
    def __init__(self,
                 sparkling_colors: list[Color],
                 background_color: Color,
                 min_spawning_interval_ms: float,
                 sparkle_min_fade_duration_ms: float,
                 sparkle_max_fade_duration_ms: float):
        # Request update every possible time.
        super().__init__(single_cycle_ms=None)

        assert len(sparkling_colors) > 0
        assert sparkle_min_fade_duration_ms <= sparkle_max_fade_duration_ms

        self.__sparkling_colors = sparkling_colors
        self.__background_color = background_color
        self.__min_spawning_interval_ms = min_spawning_interval_ms
        self.__sparkle_min_fade_duration_ms = sparkle_min_fade_duration_ms
        self.__sparkle_max_fade_duration_ms = sparkle_max_fade_duration_ms

        self.__elapsed_since_last_spawn_ms = 0

    def _on_start(self, context: ColorContext):
        context.clear(self.__background_color)

        self.__selected_colors = [None for _ in range(len(context))]
        self.__current_durations_ms = [0 for _ in range(len(context))]
        self.__threshold_durations_ms = [0 for _ in range(len(context))]

    def _on_update(self, context: ColorContext, dt: float):
        threshold_probability = 1 / len(context)
        self.__elapsed_since_last_spawn_ms += dt

        for i in range(len(context)):
            selected_color = self.__selected_colors[i]

            if selected_color:
                elapsed_since_beginning_ms = self.__current_durations_ms[i]
                max_duration_ms = self.__threshold_durations_ms[i]
                # Inverse as elapsed_since_beginning_ms is decreasing.
                progress = 1.0 - elapsed_since_beginning_ms / max_duration_ms

                context[i] = lerp(start=selected_color, end=self.__background_color, progress=progress)

                # Decrease progress.
                self.__current_durations_ms[i] -= dt
                if self.__current_durations_ms[i] <= 0:
                    self.__selected_colors[i] = None
                    self.__current_durations_ms[i] = 0
                    self.__threshold_durations_ms[i] = 0

            elif self.__elapsed_since_last_spawn_ms > self.__min_spawning_interval_ms and \
                    random.uniform(0, 1) < threshold_probability:
                self.__elapsed_since_last_spawn_ms = 0

                self.__selected_colors[i] = random.choice(self.__sparkling_colors)
                self.__threshold_durations_ms[i] = random.uniform(self.__sparkle_min_fade_duration_ms, self.__sparkle_max_fade_duration_ms)
                self.__current_durations_ms[i] = self.__threshold_durations_ms[i]
