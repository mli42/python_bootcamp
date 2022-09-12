from polynomial_model import add_polynomial_features
import numpy as np
import unittest


def assertEqual(x: np.ndarray, y: np.ndarray, decimal: int = 6):
    np.testing.assert_array_almost_equal(x, y, decimal=decimal)


class MyTestCase(unittest.TestCase):

    def test_subject(self):
        x = np.arange(1,6).reshape(-1, 1)

        assertEqual(
            add_polynomial_features(x, 3),
            np.array([
                [1,   1,   1],
                [2,   4,   8],
                [3,   9,  27],
                [4,  16,  64],
                [5,  25, 125]])
        )

        assertEqual(
            add_polynomial_features(x, 6),
            np.array([
                [    1,     1,     1,     1,     1,     1],
                [    2,     4,     8,    16,    32,    64],
                [    3,     9,    27,    81,   243,   729],
                [    4,    16,    64,   256,  1024,  4096],
                [    5,    25,   125,   625,  3125, 15625]])
        )


if __name__ == '__main__':
    unittest.main()
