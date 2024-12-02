import plasma

from animation.color_context import ColorContext
from animation.color import Color
from animation.led_device_mapper import LedDeviceMapper


class WS2818ColorStripMapper(LedDeviceMapper):
    def __init__(self,
                 strip: plasma.WS2812,
                 mapped_indexes: list[int]):
        super().__init__(dimensions=[len(mapped_indexes)])

        self.__indexes = mapped_indexes
        self.__strip = strip

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
        self.__strip.set_rgb(self.__indexes[key], color.b, color.g, color.r)
