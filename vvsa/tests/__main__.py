import unittest
from vvsa.products import Product_Factory


class Test(unittest.TestCase):
    def test_get_product(self):
        with self.assertRaises(KeyError):
            Product_Factory.get_product("SDWDad")


if __name__ == "__main__":
    unittest.main()
