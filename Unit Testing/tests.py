import unittest
from activities import get_sum , get_product

class ActivityTests(unittest.TestCase):
    # method name must starts with test_
    # if method name doesn't start with test_ that wont be run
    def test_total(self):
        self.assertEqual(get_sum(2,3),5)
    
    def test_product(self):
        self.assertEqual(get_product(2,3),6)

if __name__=='__main__':
    unittest.main()