from animation.micropyton.typing import Union

from animation.color import Color, BLACK
from animation.effects.gradient_cycle import GradientCycle


class Fade(GradientCycle):
    def __init__(self, color: Color, fade_durations_ms: Union[float, list[float]]):
        super().__init__(
            colors=[BLACK, color],
            single_transition_duration_ms=fade_durations_ms
        )




