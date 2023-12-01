# The file written for testing needs to be named test_nameofthefilecontainingthecodebeingtested
# This code will run in cmd. Command to run this file 'python -m unittest file_name.py'
# . in output means the test passed
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):                                     # The method written from testing needs to begin with test_
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)                # Edge case
        self.assertEqual(calc.add(-1, -1), -2)              # Edge case

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-1, 1), -2)
        self.assertEqual(calc.sub(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        self.assertRaises(ValueError, calc.divide, 10, 0)   # For checking the error
        # self.assertRaises(ValueError, calc.divide, 10, 2)

        # Second method to check the exception (better method)
        with self.assertRaises(ValueError):
            calc.divide(10, 2)

if __name__ == '__main__':                                  # This block allows to run this file in the editor itself.
    unittest.main()