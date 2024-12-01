from animation.color_context import ColorContext
from animation.micropyton.abc import ABC, abstractmethod
from animation.micropyton.typing import Union


class LedDevice(ABC):
    def __init__(self, dimensions: Union[int, list[int]]):
        assert isinstance(dimensions, int) or \
               isinstance(dimensions, list)

        if isinstance(dimensions, int):
            self.__dimensions = [dimensions]
        else:
            self.__dimensions = dimensions

    @abstractmethod
    def present(self, context: ColorContext):
        ...

    @property
    def device_dimensions(self) -> Union[int, list[int]]:
        return self.__dimensions
