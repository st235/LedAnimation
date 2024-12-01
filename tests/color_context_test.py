from animation.color import Color
from animation.color_context import ColorContext

import unittest

class ColorContextTest(unittest.TestCase):

    TEST_COLOR_A = Color(r=14, g=91, b=27)
    TEST_COLOR_B = Color(r=94, g=23, b=61)

    def test_array_has_correct_length_when_created_from_int(self):
        color_context = ColorContext(dimensions=5)
        self.assertEqual(len(color_context), 5)

    def test_array_has_correct_length_when_created_from_list_with_1_element(self):
        color_context = ColorContext(dimensions=[10])
        self.assertEqual(len(color_context), 10)

    def test_array_has_correct_length_when_created_from_list_with_2_element(self):
        color_context = ColorContext(dimensions=[2, 5])
        self.assertEqual(len(color_context), 10)

    def test_array_has_correct_length_when_created_from_list_with_3_element(self):
        color_context = ColorContext(dimensions=[3, 7, 4])
        self.assertEqual(len(color_context), 84)

    def test_array_has_correct_length_when_created_from_list_with_trivial_elements(self):
        color_context = ColorContext(dimensions=[1, 1, 1, 1])
        self.assertEqual(len(color_context), 1)

    def test_adding_and_getting_an_element_from_1d_context_is_consistent(self):
        color_context = ColorContext(dimensions=[10])
        color_context[5] = ColorContextTest.TEST_COLOR_A
        self.assertEqual(color_context[5], ColorContextTest.TEST_COLOR_A)

    def test_getting_an_element_from_1d_context_by_multidimensional_index_throws_assertion_error(self):
        color_context = ColorContext(dimensions=[10])
        with self.assertRaises(AssertionError):
            color_context[[1, 2]]

    def test_adding_and_getting_an_element_from_2d_context_is_consistent(self):
        color_context = ColorContext(dimensions=[5, 2])

        color_context[[0, 1]] = ColorContextTest.TEST_COLOR_A
        color_context[[1, 1]] = ColorContextTest.TEST_COLOR_B

        self.assertEqual(color_context[[0, 1]], ColorContextTest.TEST_COLOR_A)
        self.assertEqual(color_context[[1, 1]], ColorContextTest.TEST_COLOR_B)

    def test_getting_an_element_from_outside_1d_array_bounds_raises_index_error(self):
        color_context = ColorContext(dimensions=[10])
        with self.assertRaises(IndexError):
            color_context[10]

    def test_getting_an_element_from_outside_2d_array_bounds_raises_index_error(self):
        color_context = ColorContext(dimensions=[3, 4])
        with self.assertRaises(IndexError):
            color_context[[2, 4]]

if __name__ == '__main__':
    unittest.main()