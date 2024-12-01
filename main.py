from animation.animation_engine import AnimationEngine
from animation.color import AMBER, YELLOW
from animation.effects.solid_color import SolidColor
from ws2812_led_strip import WS2818ColorStrip

engine = AnimationEngine(
    animation=SolidColor(color=YELLOW),
    led_device=WS2818ColorStrip(length=50),
)

while True:
    engine.advance_one_step()