import unittest
import calc

class Test_unittest_1(unittest.TestCase):

    def test_add(self): # this method should start with test_ so python would know which methods reps test
        #result = calc.add(10, 5)
        #self.assertEqual(result, 15) # this is the test case that confirms whether the func works
        self.assertEqual(calc.add(10, 5), 15) # second most efficient method

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)

    def test_mul(self):
         self.assertEqual(calc.mul(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        # method 1 contains alot of args
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError): # method 2
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
