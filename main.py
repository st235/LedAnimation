import plasma
from plasma import plasma2040

from animation.animation_player import AnimationPlayer
from animation.color import AMBER, YELLOW, RED, GREEN, GOLD, ORANGE, BLUE, PURPLE, BLACK, WHITE, OLD_LACE
from animation.effects.solid_color import SolidColor
from animation.effects.color_cycle import ColorCycle
from animation.effects.fade import Fade
from animation.effects.gradient_cycle import GradientCycle
from animation.effects.blink import Blink
from animation.effects.snake import Snake
from animation.effects.progress import Progress
from animation.effects.sparkle import Sparkle
from ws2812_led_strip_mapper import WS2818ColorStripMapper

strip = plasma.WS2812(50, 0, 0, plasma2040.DAT, color_order=plasma.COLOR_ORDER_BGR)
strip.start()

player = AnimationPlayer()

player.add_animation(
    animation=Fade(
        color=AMBER,
        fade_duration_ms=1000,
    ),
    device_mapper=WS2818ColorStripMapper(
        strip=strip,
        mapped_indexes=[i for i in range(50) if i % 2 == 0]
    ),
)

player.add_animation(
    animation=Sparkle(
        background_color=BLUE,
        sparkling_colors=[WHITE, OLD_LACE],
        min_spawning_interval_ms=200,
        sparkle_min_fade_duration_ms=1000,
        sparkle_max_fade_duration_ms=2000,
    ),
    device_mapper=WS2818ColorStripMapper(
        strip=strip,
        mapped_indexes=[i for i in range(50) if i % 2 != 0]
    ),
)

player.start()

while True:
    player.advance_one_step()