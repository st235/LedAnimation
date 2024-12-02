from animation.color import Color, BLACK
from animation.effects.color_cycle import ColorCycle

class Blink(ColorCycle):
    def __init__(self, color: Color, single_cycle_ms: float):
        super().__init__(colors=[color, BLACK], single_cycle_ms=single_cycle_ms)
