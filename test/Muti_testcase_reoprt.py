import unittest

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def setUp(self):
        print("do something before test.Prepare environment.")

    def tearDown(self):
        print("do something after test.Clean up.")

    def test_1_add(self):
        """Test method add(a, b)"""
        print("add")
        self.assertEqual(3, (1+2))
        self.assertNotEqual(3, (2+2))

    def test_2_minus(self):
        print("minus")
        """Test method minus(a, b)"""
        self.assertEqual(1, (3-2))

    def test_3_multi(self):
        print("multi")
        """Test method multi(a, b)"""
        self.assertEqual(6, (2*3))

    @unittest.skip("I don't want to run this case.")
    def test_4_divide(self):
        print("divide")
        """Test method divide(a, b)"""
        self.assertEqual(2, (6/3))
        self.assertEqual(2.55, (5/2))

if __name__ == '__main__':
    unittest.main()