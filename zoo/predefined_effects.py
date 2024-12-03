from zoo.palette import AMBER, YELLOW, GOLD, RED, GREEN, ORANGE, BLUE, PURPLE, BLACK, WHITE, OLD_LACE, CANDLE, SOFT_CANDLE, GREY

from animation.effects.color_cycle import ColorCycle
from animation.effects.fade import Fade
from animation.effects.gradient_cycle import GradientCycle
from animation.effects.sparkle import Sparkle

POLICE_CAR_1 = ColorCycle(
    colors=[RED, BLACK, RED, BLACK, RED, BLACK, BLUE, BLACK, BLUE, BLACK, BLUE, BLACK],
    update_intervals_ms=150,
)
POLICE_CAR_2 = ColorCycle(
    colors=[RED, BLACK, RED, BLACK, RED, BLACK, RED, BLACK, BLUE, BLACK, BLUE, BLACK, BLUE, BLACK, BLUE, BLACK],
    update_intervals_ms=250,
)

EMERGENCY_CAR_1 = ColorCycle(
    colors=[BLUE, BLACK, BLUE, BLACK, BLUE, BLACK, OLD_LACE, BLACK, OLD_LACE, BLACK, OLD_LACE, BLACK],
    update_intervals_ms=300,
)

FIRE_CAR_1 = ColorCycle(
    colors=[AMBER, BLACK, AMBER, BLACK, AMBER, BLACK, OLD_LACE, BLACK, OLD_LACE, BLACK, OLD_LACE, BLACK],
    update_intervals_ms=300,
)

LIGHTNING = ColorCycle(
    colors=[WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK],
    update_intervals_ms=[100, 50, 100, 1500, 1000, 400, 350, 1000],
)

RAINBOW = GradientCycle(
    colors=[RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE],
    single_transition_duration_ms=5000,
)

TV = ColorCycle(
    colors=[WHITE, OLD_LACE],
    update_intervals_ms=2000,
)

CANDLE = GradientCycle(
    colors=[SOFT_CANDLE, CANDLE],
    single_transition_duration_ms=[2000, 5000],
)

BROKEN_BULB = ColorCycle(
    colors=[WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK],
    update_intervals_ms=[50, 50, 50, 50, 100, 50, 50, 500, 400, 100, 200, 200, 200, 1500, 2000, 3000],
)

PULSE = Fade(
    color=OLD_LACE,
    fade_durations_ms=4000,
)

SNOWFLAKES = Sparkle(
    sparkling_colors=[WHITE, OLD_LACE],
    background_color=BLACK,
    min_spawning_interval_ms=700,
    sparkle_min_fade_duration_ms=2000,
    sparkle_max_fade_duration_ms=5000,
)

SPARKLES = Sparkle(
    sparkling_colors=[GOLD, YELLOW],
    background_color=GREY,
    min_spawning_interval_ms=0,
    sparkle_min_fade_duration_ms=150,
    sparkle_max_fade_duration_ms=250,
)
