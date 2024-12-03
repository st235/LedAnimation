from animation.micropyton.abc import ABC, abstractmethod
from animation.micropyton.typing import Optional, Union

from animation.color_context import ColorContext


class Animation(ABC):
    def __init__(self, update_intervals_ms: Optional[Union[float, list[float]]]):
        assert not update_intervals_ms or \
               isinstance(update_intervals_ms, int) or \
               isinstance(update_intervals_ms, float) or \
               isinstance(update_intervals_ms, list), \
            f"update_intervals_ms should be None, int, float, or list of floats but got: {update_intervals_ms}"

        if not update_intervals_ms:
            self.__update_intervals_ms = [0.0]
        elif isinstance(update_intervals_ms, int) or isinstance(update_intervals_ms, float):
            self.__update_intervals_ms = [float(update_intervals_ms)]
        elif len(update_intervals_ms) == 0:
            self.__update_intervals_ms = [0.0]
        else:
            self.__update_intervals_ms = update_intervals_ms

        self.__elapsed_time_ms = 0.0
        self.__next_update_time_ms = 0.0
        self.__current_update_interval_index = 0

    def start(self, context: ColorContext):
        self.__elapsed_time_ms = 0.0
        self.__next_update_time_ms = 0.0
        self.__current_update_interval_index = 0
        self._on_start(context)

    def _on_start(self, context: ColorContext):
        pass

    def update(self, context: ColorContext, dt: float):
        self.__elapsed_time_ms += dt

        if self.__elapsed_time_ms >= self.__next_update_time_ms:
            self.__elapsed_time_ms = 0.0
            self.__next_update_time_ms = self.__update_intervals_ms[self.__current_update_interval_index]
            self.__current_update_interval_index = \
                (self.__current_update_interval_index + 1) % len(self.__update_intervals_ms)
            self._on_update(context=context, dt=dt)

    @abstractmethod
    def _on_update(self, context: ColorContext, dt: float):
        ...

    @property
    def update_intervals_ms(self) -> list[float]:
        return self.__update_intervals_ms
