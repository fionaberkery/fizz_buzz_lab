import unittest

from fizz_buzz import *

class TestFizzBuzz(unittest.TestCase):
    # @unittest.skip("")
    def test_3_is_fizz(self):
        self.assertEqual("fizz", fizz_buzz(3))