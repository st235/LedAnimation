import plasma
from plasma import plasma2040

from animation.color_context import ColorContext
from animation.color import Color
from animation.led_device import LedDevice


class WS2818ColorStrip(LedDevice):
    def __init__(self, length: int):
        super().__init__(dimensions=[length])

        self.__strip = plasma.WS2812(length, 0, 0, plasma2040.DAT, color_order=plasma.COLOR_ORDER_BGR)
        self.__strip.start()

    def present(self, context: ColorContext):
        assert self.device_dimensions == context.dimensions

        dimensions = self.device_dimensions
        for item in range(dimensions[0]):
            self.__setitem__(item, context[item])

    def fill(self, color: Color):
        dimensions = self.device_dimensions
        for item in range(dimensions[0]):
            self.__setitem__(item, color)

    def __setitem__(self, key: int, color: Color):
        self.__strip.set_rgb(key, color.b, color.g, color.r)
