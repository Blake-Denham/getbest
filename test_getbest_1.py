import unittest
import getbest
import os

file_path = os.path.dirname(__file__)

class Test(unittest.TestCase):
    def setup(self):
        self.test_data =open(os.path.join(file_path, "bestdat0.csv"))

    def test(self):
        f = self.test_data
        num_col,mark_col = getbest.getCols(self.test_data)
        best_idx, best = findTop(,num_col,mark_col)
        self.assertEqual(best, 90)


if __name__ == '__main__':
    unittest.main()
