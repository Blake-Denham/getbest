import unittest
import getbest
import os

file_path = os.path.dirname(__file__)

class Test(unittest.TestCase):
    def setup(self):
        self.test_data =os.path.join(file_path, "bestdat0.csv")

    def test(self):
        num_col,mark_col = getbest.getCols(self.test_data)
        self.assertEqual(num_col[1], 160001)
        self.assertEqual(mark_col[1], 72) 


if __name__ == '__main__':
    unittest.main()
