from animation import _COLOR_DISABLED
from animation.color import Color
from animation.micropyton.typing import Union


class ColorContext:
    def __init__(self, dimensions: Union[int, list[int]]):
        assert isinstance(dimensions, int) or \
               isinstance(dimensions, list)

        if isinstance(dimensions, int):
            self.__dimensions = [dimensions]
        else:
            self.__dimensions = dimensions

        self.__continuous_array_capacity = ColorContext.__get_dimensions_as_continuous_array_length(self.__dimensions)
        self.__raw_array = [_COLOR_DISABLED for _ in range(self.__continuous_array_capacity)]

    def __getitem__(self, item: Union[int, list[int]]) -> Color:
        return self.__raw_array[self.__index_as_continuous_array_offset(item)]

    def __setitem__(self, key: Union[int, list[int]], color: Color):
        self.__raw_array[self.__index_as_continuous_array_offset(key)] = color

    def clear(self, color: Color):
        for i in range(self.__continuous_array_capacity):
            self.__raw_array[i] = color

    def __len__(self) -> int:
        return self.__continuous_array_capacity

    @property
    def dimensions(self) -> Union[int, list[int]]:
        return self.__dimensions

    def __index_as_continuous_array_offset(self, index: Union[int, list[int]]) -> int:
        assert isinstance(index, int) or \
               isinstance(index, list)

        if isinstance(index, int):
            return index
        else:
            # Index and dimensions should be of the same size.
            assert len(index) == len(self.__dimensions)

            offset = 0
            capacity = self.__continuous_array_capacity

            for i in range(len(index)):
                if index[i] >= self.dimensions[i]:
                    raise IndexError()

                capacity = capacity // self.dimensions[i]
                offset += capacity * index[i]

            return offset

    @staticmethod
    def __get_len_of_union_index(index: Union[int, list[int]]) -> int:
        assert isinstance(index, int) or \
               isinstance(index, list)

        if isinstance(index, int):
            return 1
        else:
            return len(index)

    @staticmethod
    def __get_dimensions_as_continuous_array_length(dimensions: list[int]) -> int:
        length = 1
        for dimension in dimensions:
            length *= dimension
        return length
