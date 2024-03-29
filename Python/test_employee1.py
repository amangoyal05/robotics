# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

import unittest
from unittest.mock import patch
from employee1 import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):                                    # This code will run before every test
        print('setUp')
        self.emp_1 = Employee('Aman', 'Goyal', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):                                 # This code will run after every test
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Aman.Goyal@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Goyal@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Aman Goyal')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Goyal')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_applyraise(self):
        print('test_applyraise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):                            # Example when we use things that are not in our control. Like accessing data from some other website.
        with patch('employee1.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Goyal/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()