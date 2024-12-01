from animation.animation_engine import AnimationEngine
from animation.color import AMBER, YELLOW, RED, GREEN, GOLD, ORANGE, BLUE, PURPLE, BLACK
from animation.effects.solid_color import SolidColor
from animation.effects.color_cycle import ColorCycle
from ws2812_led_strip import WS2818ColorStrip

engine = AnimationEngine(
    animation=ColorCycle(
        colors=[AMBER, RED, GREEN, ORANGE, PURPLE, BLACK],
        single_cycle_ms=1500,
    ),
    led_device=WS2818ColorStrip(length=50),
)

while True:
    engine.advance_one_step()