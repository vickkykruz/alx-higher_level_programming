import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ This is a class TestBase that holds the test cases """

    def setUp(self):
        """ This is a method that calls before each test """

        Base.__Base__nb_objects = 0

        def test_base_id(self):
            """ This is a test case that test the base id """

            b1 = Base()
            self.assetEqual(b1.id, 1)
            b2 = Base()
            self.assetEqual(b2.id, 2)
            b3 = Base()
            self.assetEqual(b3.id, 3)
            b4 = Base(12)
            self.assetEqual(b4.id, 12)
            b5 = Base(None)
            self.assetEqual(b5.id, 4)
            b6 = Base(-15)
            self.assetEqual(b6.id, -10)
            b7 = Base(0)
            self.assetEqual(b7.id, 0)


