from animation.animation import Animation
from animation.color import Color, lerp
from animation.color_context import ColorContext


class Snake(Animation):
    def __init__(self,
                 snake_color: Color,
                 background_color: Color,
                 snake_size: int,
                 snake_moving_speed_ms: float,
                 interpolate_snake_segments: bool = True):
        # Request update every possible time.
        super().__init__(single_cycle_ms=snake_moving_speed_ms)

        assert snake_size >= 1

        self.__snake_color = snake_color
        self.__background_color = background_color

        self.__snake_size = snake_size
        self.__snake_moving_speed_ms = snake_moving_speed_ms
        self.__interpolate_snake_segments = interpolate_snake_segments

    def _on_start(self, context: ColorContext):
        assert self.__snake_size <= len(context)

        self.__snake_head_position = self.__snake_size

    def _on_update(self, context: ColorContext, dt: float):
        context.clear(self.__background_color)

        # Plus 1 to make the last partition visible if interpolated.
        snake_partition = 1 / (self.__snake_size + 1)
        for i in range(self.__snake_size):
            snake_segment_position = (self.__snake_head_position - i) % len(context)

            if self.__interpolate_snake_segments:
                context[snake_segment_position] = lerp(start=self.__snake_color, end=self.__background_color, progress=i * snake_partition)
            else:
                context[snake_segment_position] = self.__snake_color

        self.__snake_head_position = (self.__snake_head_position + 1) % len(context)


