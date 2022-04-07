import unittest

from fizz_buzz import *

class TestFizzBuzz(unittest.TestCase):
    # @unittest.skip("")
    def test_3_is_fizz(self):
        self.assertEqual("fizz", fizz_buzz(3))

    def test_any_multiple_of_3_is_fizz(self):
        self.assertEqual("fizz", fizz_buzz(6))
        self.assertEqual("fizz", fizz_buzz(18))
        self.assertEqual("fizz", fizz_buzz(12))
        self.assertEqual("fizz", fizz_buzz(9))
        self.assertNotEqual("fizz", fizz_buzz(8))
    
    def test_5_is_buzz(self):
        self.assertEqual("buzz", fizz_buzz(5))
    
    def test_any_multiple_of_5_buzz(self):
        self.assertEqual("buzz", fizz_buzz(10))
        # self.assertEqual("buzz", fizz_buzz(15))
        self.assertEqual("buzz", fizz_buzz(20))
        self.assertEqual("buzz", fizz_buzz(25))