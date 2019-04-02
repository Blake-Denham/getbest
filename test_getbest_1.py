import unittest
import getbest
import sys



class Test(unittest.TestCase):
    def test(self):
        f=open(sys.argv[1])
        num_col,mark_col = getbest.getCols(f)
        self.assertNotEqual(num_col,mark_col)


if __name__ == '__main__':
    unittest.main()
