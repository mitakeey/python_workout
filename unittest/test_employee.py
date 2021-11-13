# test case using setup and tear down method
# The setUp() and tearDown() methods allow you to define instructions
# that will be executed before and after each test method.
import unittest
from employee import Employee

import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('SetUp class')

    @classmethod
    def tearDownClass(cls):
        print('TearDown class')


    def setUp(self):
        self.emp_1 = Employee('Samora', 'Mitakeey', 300000)
        self.emp_2 = Employee('Sheila', 'Mumbua', 100000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Samora.Mitakeey@gmail.com')
        self.assertEqual(self.emp_2.email, 'Sheila.Mumbua@gmail.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Mitakeey@gmail.com')
        self.assertEqual(self.emp_2.email, 'Jane.Mumbua@gmail.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Samora.Mitakeey')
        self.assertEqual(self.emp_2.fullname, 'Sheila.Mumbua')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John.Mitakeey')
        self.assertEqual(self.emp_2.fullname, 'Jane.Mumbua')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 315000)
        self.assertEqual(self.emp_2.pay, 105000)

    def test_monthly_schedule(self):
        # within patch we pass what we want to mock
        with patch('employee.requests.get') as mocked_get :
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'success'
            # run our schedule like we are testing
            schedule = self.emp_1.monthly_schedule('May')
            # to make sure get method was called with correct URL since mock object recalls when called
            mocked_get.assert_called_with('http://company.com/Mitakeey/May') # from reponse attribute
            # make sure it returns the correct text
            self.assertEqual(schedule= '_success_')

            #testing a failed reponse

            mocked_get.return_value.ok = False
            # run our schedule like we are testing
            schedule = self.emp_1.monthly_schedule('May')
            # to make sure get method was called with correct URL since mock object recalls when called
            mocked_get.assert_called_with('http://company.com/Mitakeey/May')  # from reponse attribute
            # make sure it returns the correct text
            self.assertEqual(schedule='_Bad Response_')



if __name__ == '__main__':
    unittest.main()
