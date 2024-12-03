from animation.micropyton.typing import Union

from animation import _COLOR_DISABLED
from animation.color import Color
from animation.effects.gradient_cycle import GradientCycle


class Fade(GradientCycle):
    def __init__(self, color: Color, fade_durations_ms: Union[float, list[float]]):
        super().__init__(
            colors=[_COLOR_DISABLED, color],
            single_transition_duration_ms=fade_durations_ms
        )
