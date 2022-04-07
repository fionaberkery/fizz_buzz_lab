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

    def test_any_multiple_of_3_and_5_is_fizzbuzz(self):
        self.assertEqual("fizz buzz", fizz_buzz(15))
        self.assertEqual("fizz buzz", fizz_buzz(30))
        self.assertEqual("fizz buzz", fizz_buzz(45))
        self.assertEqual("fizz buzz", fizz_buzz(60))

    def test_any_nunmber_not_divisible_by_3_nor_5(self):
        self.assertEqual("7", fizz_buzz(7))
        self.assertEqual("11", fizz_buzz(11))
        self.assertEqual("23", fizz_buzz(23))
        self.assertEqual("41", fizz_buzz(41))