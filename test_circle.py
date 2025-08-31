import unittest
from circle import Circle

class TestCircle(unittest.TestCase):

    def test_constructor(self):
        c = Circle(5)
        self.assertIsInstance(c, Circle)
        self.assertEqual(c.getRadius(), 5)

    def test_get_radius(self):
        c = Circle(5)
        self.assertEqual(c.getRadius(), 5)
        self.assertNotEqual(c.getRadius(), 10)

    def test_set_radius_positive(self):
        c = Circle(5)
        result = c.setRadius(10)
        self.assertTrue(result)
        self.assertEqual(c.getRadius(), 10)

    def test_set_radius_negative(self):
        c = Circle(5)
        result = c.setRadius(-3)
        self.assertFalse(result)
        self.assertEqual(c.getRadius(), 5)
    
    def test_SetRadius_zero(self):
        c = Circle(5)
        result = c.setRadius(0)
        self.assertTrue(result)
        self.assertEqual(c.getRadius(), 0)

    def test_get_area(self):
        c = Circle(3)
        expected_area = 3.141592653589793 * 3 * 3
        self.assertAlmostEqual(c.getArea(), expected_area)

    def test_get_circumference(self):
        c = Circle(4)
        expected_circumference = 2 * 3.141592653589793 * 4
        self.assertAlmostEqual(c.getCircumference(), expected_circumference)