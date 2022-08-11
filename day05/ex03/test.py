from tools import add_intercept
import numpy as np
import unittest


def assertEqual(x, y):
    np.testing.assert_array_equal(x, y)


class MyTestCase(unittest.TestCase):

    def test_subject(self):
        y1 = np.array([
            [1., 1.],
            [1., 2.],
            [1., 3.],
            [1., 4.],
            [1., 5.]])

        y2 = np.array([
            [1., 1., 2., 3.],
            [1., 4., 5., 6.],
            [1., 7., 8., 9.]])

        assertEqual(add_intercept(np.arange(1, 6, dtype=float)), y1)
        assertEqual(add_intercept(np.arange(1, 10, dtype=float).reshape((3, 3))), y2)


if __name__ == '__main__':
    unittest.main()
