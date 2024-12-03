import plasma
from plasma import plasma2040

from animation.animation_player import AnimationPlayer
from animation.effects.fade import Fade
from ws2812_led_strip_mapper import WS2818ColorStripMapper
from zoo.palette import CANDLE

strip = plasma.WS2812(50, 0, 0, plasma2040.DAT, color_order=plasma.COLOR_ORDER_BGR)
strip.start()

player = AnimationPlayer()

player.add_animation(
    animation=Fade(
        color=CANDLE,
        fade_durations_ms=3000,
    ),
    device_mapper=WS2818ColorStripMapper(
        strip=strip,
        mapped_indexes=[i for i in range(50)]
    ),
)

player.start()

while True:
    player.advance_one_step()