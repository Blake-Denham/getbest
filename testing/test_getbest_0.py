import unittest
import os

from src.getbest import getCols, findTop


class GetBestTest(unittest.TestCase):
    # sets up the table before each table
    def setUp(self):
        # opens the csv (the 'correct' way to do it)
        self.data = open(os.path.join('test_data', 'test_bestdat_0.csv'))

    def tearDown(self):
        # you should close files like this
        self.data.close()

    def test_get_col(self):
        col1, col2 = getCols(self.data)
        self.assertEqual(col1, 1)
        self.assertEqual(col2, 2)

    def test_find_top(self):
        # heading_removed flags that the headings of the table have/have not been removed
        student_id, mark = findTop(self.data, 1, 2, headings_removed=False)
        self.assertEqual(student_id, '167381')  # 167381 needs to be a string
        self.assertEqual(mark, 90)  # 90 needs to be an int


if __name__ == '__main__':
    unittest.main()
