import plasma
from plasma import plasma2040

from animation.animation_player import AnimationPlayer
from animation.effects.color_cycle import ColorCycle
from zoo.palette import BLUE, RED, BLACK
from ws2812_led_strip_mapper import WS2818ColorStripMapper

strip = plasma.WS2812(50, 0, 0, plasma2040.DAT, color_order=plasma.COLOR_ORDER_BGR)
strip.start()

player = AnimationPlayer()

player.add_animation(
    animation=ColorCycle(
        colors=[BLUE, BLACK, BLUE, BLACK, BLUE, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
        update_intervals_ms=100,
    ),
    device_mapper=WS2818ColorStripMapper(
        strip=strip,
        mapped_indexes=[i for i in range(50) if i % 2 != 0]
    ),
)

player.add_animation(
    animation=ColorCycle(
        colors=[BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED, BLACK, RED, BLACK, RED, BLACK],
        update_intervals_ms=100,
    ),
    device_mapper=WS2818ColorStripMapper(
        strip=strip,
        mapped_indexes=[i for i in range(50) if i % 2 == 0]
    ),
)

player.start()

while True:
    player.advance_one_step()