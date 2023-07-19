#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle

class TestRectangleConstructor(unittest.TestCase):
    """testing class constructor ."""
    def test_constructor_with_valid_arguments(self):
        # Test valid arguments
        r1 = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1)

    def test_constructor_with_defaults(self):
        # Test constructor with default values
        r2 = Rectangle(5, 5)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertIsNotNone(r2.id)

    def test_constructor_with_negative_width(self):
        # Test constructor with negative width (should raise ValueError)
        with self.assertRaises(ValueError):
            r3 = Rectangle(-5, 10)

    def test_constructor_with_zero_height(self):
        # Test constructor with zero height (should raise ValueError)
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 0)

    def test_constructor_with_non_integer_x_coordinate(self):
        # Test constructor with non-integer x-coordinate (should raise TypeError)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 5, "invalid_x")

    def test_constructor_with_non_integer_y_coordinate(self):
        # Test constructor with non-integer y-coordinate (should raise TypeError)
        with self.assertRaises(TypeError):
            r6 = Rectangle(5, 5, 1, "invalid_y")

    def test_constructor_with_non_integer_width(self):
        # Test constructor with non-integer width (should raise TypeError)
        with self.assertRaises(TypeError):
            r7 = Rectangle("invalid_width", 5)

    def test_constructor_with_non_integer_height(self):
        # Test constructor with non-integer height (should raise TypeError)
        with self.assertRaises(TypeError):
            r8 = Rectangle(5, "invalid_height")
            
    def test_constructor_with_valid_arguments(self):
        # Test valid arguments
        r1 = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1)

    # ... (previous test functions)

    def test_constructor_with_max_values(self):
        # Test constructor with maximum allowed values
        r9 = Rectangle(1000000, 1000000, 99999, 99999, 999999)
        self.assertEqual(r9.width, 1000000)
        self.assertEqual(r9.height, 1000000)
        self.assertEqual(r9.x, 99999)
        self.assertEqual(r9.y, 99999)
        self.assertEqual(r9.id, 999999)

    def test_constructor_with_negative_height(self):
        # Test constructor with negative height (should raise ValueError)
        with self.assertRaises(ValueError):
            r10 = Rectangle(10, -5)

    def test_constructor_with_negative_x_coordinate(self):
        # Test constructor with negative x-coordinate (should raise ValueError)
        with self.assertRaises(ValueError):
            r11 = Rectangle(5, 5, -2)

    def test_constructor_with_negative_y_coordinate(self):
        # Test constructor with negative y-coordinate (should raise ValueError)
        with self.assertRaises(ValueError):
            r12 = Rectangle(5, 5, 1, -3)



class TestRectangleWidth(unittest.TestCase):
    def test_get_width(self):
        # Test getting the width property
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)

    def test_set_valid_width(self):
        # Test setting a valid width
        r2 = Rectangle(5, 5)
        r2.width = 15
        self.assertEqual(r2.width, 15)

    def test_set_invalid_width_non_integer(self):
        # Test setting an invalid width with a non-integer value (should raise TypeError)
        r3 = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            r3.width = "invalid_width"

    def test_set_invalid_width_negative(self):
        # Test setting an invalid width with a negative value (should raise ValueError)
        r4 = Rectangle(5, 5)
        with self.assertRaises(ValueError):
            r4.width = -10

    def test_set_invalid_width_zero(self):
        # Test setting an invalid width with a zero value (should raise ValueError)
        r5 = Rectangle(5, 5)
        with self.assertRaises(ValueError):
            r5.width = 0
            
    
class TestRectangleHeight(unittest.TestCase):
    def test_get_height(self):
        # Test getting the height property
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.height, 20)

    def test_set_valid_height(self):
        # Test setting a valid height
        r2 = Rectangle(5, 5)
        r2.height = 15
        self.assertEqual(r2.height, 15)

    def test_set_invalid_height_non_integer(self):
        # Test setting an invalid height with a non-integer value (should raise TypeError)
        r3 = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            r3.height = "invalid_height"

    def test_set_invalid_height_negative(self):
        # Test setting an invalid height with a negative value (should raise ValueError)
        r4 = Rectangle(5, 5)
        with self.assertRaises(ValueError):
            r4.height = -10

    def test_set_invalid_height_zero(self):
        # Test setting an invalid height with a zero value (should raise ValueError)
        r5 = Rectangle(5, 5)
        with self.assertRaises(ValueError):
            r5.height = 0   


class TestRectangleY(unittest.TestCase):
    def test_get_y(self):
        # Test getting the y property
        r1 = Rectangle(10, 20, 5, 10)
        self.assertEqual(r1.y, 10)

    def test_set_valid_y(self):
        # Test setting a valid y-coordinate
        r2 = Rectangle(5, 5)
        r2.y = 15
        self.assertEqual(r2.y, 15)

    def test_set_invalid_y_non_integer(self):
        # Test setting an invalid y-coordinate with a non-integer value (should raise TypeError)
        r3 = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            r3.y = "invalid_y"

    def test_set_invalid_y_negative(self):
        # Test setting an invalid y-coordinate with a negative value (should raise ValueError)
        r4 = Rectangle(5, 5)
        with self.assertRaises(ValueError):
            r4.y = -10


            
class TestRectangleX(unittest.TestCase):
    def test_get_x(self):
        # Test getting the x property
        r1 = Rectangle(10, 20, 5, 10)
        self.assertEqual(r1.x, 5)

    def test_set_valid_x(self):
        # Test setting a valid x-coordinate
        r2 = Rectangle(5, 5)
        r2.x = 15
        self.assertEqual(r2.x, 15)

    def test_set_invalid_x_non_integer(self):
        # Test setting an invalid x-coordinate with a non-integer value (should raise TypeError)
        r3 = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            r3.x = "invalid_x"

    def test_set_invalid_x_negative(self):
        # Test setting an invalid x-coordinate with a negative value (should raise ValueError)
        r4 = Rectangle(5, 5)
        with self.assertRaises(ValueError):
            r4.x = -10
