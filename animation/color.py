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

    @staticmethod
    def __is_color_component(value: int) -> bool:
        return isinstance(value, int) and 0 <= value <= 255


RED = Color(255, 0, 0)

YELLOW = Color(255, 150, 0)

ORANGE = Color(255, 40, 0)

GREEN = Color(0, 255, 0)

TEAL = Color(0, 255, 120)

CYAN = Color(0, 255, 255)

BLUE = Color(0, 0, 255)

PURPLE = Color(180, 0, 255)

MAGENTA = Color(255, 0, 20)

WHITE = Color(255, 255, 255)

BLACK = Color(0, 0, 0)

GOLD = Color(255, 222, 30)

PINK = Color(242, 90, 255)

AQUA = Color(50, 255, 255)

JADE = Color(0, 255, 40)

AMBER = Color(255, 100, 0)

OLD_LACE = Color(253, 245, 230)
