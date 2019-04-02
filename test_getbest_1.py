import unittest
import getbest
import sys



class Test(unittest.TestCase):
    def setup(self):
        self.test_data =open(sys.argv[1])

    def test(self):
        num_col,mark_col = getbest.getCols(self.test_data)
        self.assertEqual(num_col[1], 160001)
        self.assertEqual(mark_col[1], 72) 


if __name__ == '__main__':
    unittest.main()
