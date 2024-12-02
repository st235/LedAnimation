from animation.color import Color, BLACK
from animation.effects.gradient_cycle import GradientCycle


class Fade(GradientCycle):
    def __init__(self, color: Color, fade_duration_ms: float):
        super().__init__(
            colors=[BLACK, color],
            single_transition_duration_ms=fade_duration_ms / 2
        )




