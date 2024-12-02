from animation.animation import Animation
from animation.color_context import ColorContext
from animation.led_device_mapper import LedDeviceMapper
from animation.time_utils import time_ms

class AnimationPlayer:
    def __init__(self):
        self.__is_started = False
        self.__animations: list[tuple[Animation, ColorContext, LedDeviceMapper]] = []
        self.__last_cycle_start_time_ms = 0

    def add_animation(self,
                      animation: Animation,
                      device_mapper: LedDeviceMapper):
        self.__animations.append((animation,  ColorContext(dimensions=device_mapper.device_dimensions), device_mapper))

    def start(self):
        self.__is_started = True
        for (animation, color_context, _) in self.__animations:
            animation.start(color_context)

    def advance_one_step(self):
        assert self.__is_started, \
            "Cannot start without calling #start() explicitly"

        current_time_ms = time_ms()
        dt = current_time_ms - self.__last_cycle_start_time_ms
        self.__last_cycle_start_time_ms = current_time_ms

        for (animation, color_context, device_mapper) in self.__animations:
            animation.update(context=color_context, dt=dt)
            device_mapper.present(context=color_context)

