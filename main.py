from animation.animation_engine import AnimationEngine
from animation.color import AMBER, YELLOW, RED, GREEN, GOLD, ORANGE, BLUE, PURPLE, BLACK
from animation.effects.solid_color import SolidColor
from animation.effects.color_cycle import ColorCycle
from animation.effects.fade import Fade
from animation.effects.gradient_cycle import GradientCycle
from animation.effects.blink import Blink
from ws2812_led_strip import WS2818ColorStrip

engine = AnimationEngine(
    animation=GradientCycle(
        colors=[AMBER, GOLD, GREEN, ORANGE, PURPLE],
        single_transition_duration_ms=5000,
    ),
    led_device=WS2818ColorStrip(length=50),
)

while True:
    engine.advance_one_step()