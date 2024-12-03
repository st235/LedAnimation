from animation import _COLOR_DISABLED
from animation.color import Color
from animation.effects.color_cycle import ColorCycle
from animation.micropyton.typing import Union

class Blink(ColorCycle):
    def __init__(self, color: Color, update_intervals_ms: Union[float, list[float]]):
        super().__init__(colors=[color, _COLOR_DISABLED], update_intervals_ms=update_intervals_ms)
