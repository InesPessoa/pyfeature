from pyfeature.textcleaning import Cleaner
import unittest

class TestCleaner(unittest.TestCase):

    def test_feature_name_input(self):
        with self.assertRaises(TypeError): Cleaner(5) #testing random variable types
        with self.assertRaises(TypeError): Cleaner("feature", True)
        self.assertEqual(Cleaner("feature").feature_name, "feature")
        self.assertEqual(Cleaner("feature").style, "raw_text") #default value
        self.assertEqual(Cleaner("feature", "regex").style, "regex")
        with self.assertRaises(ValueError): Cleaner("feature", "random")

    def test_numeric(self):
        cleaner = Cleaner("feature", "raw_text")
        self.assertEqual(cleaner.raw_text("2G45 5AAA5"), "2g45 5aaa5")


if __name__ == '__main__':
    unittest.main()
