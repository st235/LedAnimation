from animation.animation import Animation
from animation.color_context import ColorContext
from animation.led_device import LedDevice
from animation.time_utils import time_ms

class AnimationPlayer:
    def __init__(self,
                 animation: Animation,
                 led_device: LedDevice):
        self.__animation = animation
        self.__color_context = ColorContext(dimensions=led_device.device_dimensions)
        self.__led_device = led_device
        self.__last_cycle_start_time_ms = 0

        # Initialise animation.
        self.__animation.start(context=self.__color_context)

    def advance_one_step(self):
        current_time_ms = time_ms()
        dt = current_time_ms - self.__last_cycle_start_time_ms
        self.__last_cycle_start_time_ms = current_time_ms

        self.__animation.update(context=self.__color_context, dt=dt)

        self.__led_device.present(context=self.__color_context)


    @property
    def animation(self) -> Animation:
        return self.__animation

    @property
    def device(self) -> LedDevice:
        return self.__led_device
