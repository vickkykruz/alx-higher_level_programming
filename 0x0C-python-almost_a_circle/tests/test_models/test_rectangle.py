import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """ This is class RectangleTest that holds the test cases """

    def setUp(self):
        """ This is test method the initalizated the setUp """

        Base.__Base__nb_objects = 0

    def test_rectangle(self):
        """ This is menthod that testes the normal rectangle """

        rect1 = Rectangle(10, 5, 8, 4, 5)

        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 5)
        self.assertEqual(rect1.x, 8)
        self.assertEqual(rect1.y, 4)
        self.assertEqual(rect1.id, 5)

    def test_rectangle2(self):
        """ This is method that teste the normal rectangle """

        rect1 = Rectangle(1, 1)

        rect1.height = 10
        self.assertEqual(rect1.height, 10)
        rect1.width = 5
        self.assertEqual(rect1.width, 5)
        rect1.y = 4
        self.assertEqual(rect1.y, 4)
        rect1.x = 2
        self.assertEqual(rect1.x, 2)

    def test_rect_y(self):
        """ This is method that test rectangle without y """

        rect1 = Rectangle(200, 10, 17)

        self.assertEqual(rect1.width, 200)
        self.assertEqual(rect1.height, 10)
        self.assertEqual(rect1.x, 17)
        self.assertEqual(rect1.y, 0)
        self.assertEqual(rect1.id, 8)

    def test_rect_invalid_x1(self):
        """ This is method that rect1 with wrong input """

        rect4 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 5, 20, True)
        with self.assertRaises(TypeError):
            r2 = Rectangle(200, 17, 10, "s")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 1, 1, [1, 2])
        with self.assertRaises(TypeError):
            rect4.y = "Hello"
        with self.assertRaises(TypeError):
            rect4.y = True

    def test_rect_invalid_y1(self):
        """ This is a method that test wrong y """

        rect4 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 5, 20, -10)
        with self.assertRaises(ValueError):
            r2 = Rectangle(200, 10, 17, -5)
        with self.assertRaises(ValueError):
            rect4.y = -2
