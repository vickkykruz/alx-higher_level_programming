import unittest
import json
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

        def test_base_id_args(self):
            """ This is a test case that test more args """

            with self.assertRaises(TypeError):
                ba1 = Base(1, 4)

        def test_base_to_json_string(self):
            """ This is a method that test the to_json_string """

            list_dic = [
                    {"id": 1, "height": 5, "width": 4, "x": 0, "y": 0},
                    {"id": 2, "height": 15, "width": 5, "x": 2, "y": 0}
                ]

            b_json = Base.to_json_string(list_dic)
            self.assertEqual(b_json, json.dumps(list_dic))
            self.assertTrue(type(b_json) is str)
            self.assertEqual(Base.to_json_string(None), "[]")


