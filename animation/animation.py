from animation.color_context import ColorContext
from animation.micropyton.abc import ABC, abstractmethod
from animation.micropyton.typing import Optional


class Animation(ABC):
    def __init__(self, single_cycle_ms: Optional[float]):
        self.__single_cycle_ms = single_cycle_ms

        self.__elapsed_time_ms = 0
        self.__single_cycle_ms = single_cycle_ms if single_cycle_ms else 0

    def update(self, context: ColorContext, dt: float):
        self.__elapsed_time_ms += dt

        if self.__elapsed_time_ms > self.__single_cycle_ms:
            self.__elapsed_time_ms = 0
            self._on_update(context=context, dt=dt)

    @abstractmethod
    def _on_update(self, context: ColorContext, dt: float):
        ...

    @property
    def single_cycle_ms(self) -> Optional[float]:
        return self.__single_cycle_ms
