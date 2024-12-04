import plasma
from plasma import plasma2040

from animation.animation_player import AnimationPlayer
from animation.effects.fade import Fade
from ws2812_led_strip_mapper import WS2818ColorStripMapper
from zoo.palette import CANDLE

# Initialises hardware.
strip = plasma.WS2812(50, 0, 0, plasma2040.DAT, color_order=plasma.COLOR_ORDER_BGR)
strip.start()

# Controls the animation.
player = AnimationPlayer()

# Adds animation to play.
player.add_animation(
    animation=Fade(
        color=CANDLE,
    ),
    device_mapper=WS2818ColorStripMapper(
        strip=strip,
        mapped_indexes=[i for i in range(50)]
    ),
)

# It is necessary to initialise the player prior advancing the animation loop
# as it sets up the inner animations state, required to work properly.
player.start()

while True:
    # Advances animation cycle one step forward.
    player.advance_one_step()