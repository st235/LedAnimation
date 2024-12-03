class Color:
    def __init__(self, r: int, g: int, b: int):
        assert Color.__is_color_component(r) and \
            Color.__is_color_component(g) and \
            Color.__is_color_component(b)

        self.__r = r
        self.__g = g
        self.__b = b

    @property
    def r(self) -> int:
        return self.__r

    @property
    def g(self) -> int:
        return self.__g

    @property
    def b(self) -> int:
        return self.__b

    def __eq__(self, other) -> bool:
        if not isinstance(other, Color):
            return False

        return self.__r == other.r and \
            self.__g == other.g and \
            self.__b == other.b

    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def __is_color_component(value: int) -> bool:
        return isinstance(value, int) and 0 <= value <= 255

def _lerp(start: Color, end: Color, progress: float) -> Color:
    if progress < 0:
        progress = 0
    elif progress > 1.0:
        progress = 1.0

    return Color(r=int((end.r - start.r) * progress + start.r),
                 g=int((end.g - start.g) * progress + start.g),
                 b=int((end.b - start.b) * progress + start.b))
