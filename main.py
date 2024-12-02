from animation.animation_player import AnimationPlayer
from animation.color import AMBER, YELLOW, RED, GREEN, GOLD, ORANGE, BLUE, PURPLE, BLACK, WHITE, OLD_LACE
from animation.effects.solid_color import SolidColor
from animation.effects.color_cycle import ColorCycle
from animation.effects.fade import Fade
from animation.effects.gradient_cycle import GradientCycle
from animation.effects.blink import Blink
from animation.effects.sparkle import Sparkle
from ws2812_led_strip import WS2818ColorStrip

engine = AnimationPlayer(
    animation=Sparkle(
        sparkling_colors=[GOLD, YELLOW],
        background_color=OLD_LACE,
        min_spawning_interval_ms=2000,
        sparkle_min_fade_duration_ms=5000,
        sparkle_max_fade_duration_ms=8000,
    ),
    led_device=WS2818ColorStrip(length=50),
)

while True:
    engine.advance_one_step()