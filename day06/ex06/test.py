from minmax import minmax
import numpy as np
import unittest


def assertEqual(x: np.ndarray, y: np.ndarray):
    np.testing.assert_array_almost_equal(x, y)


class MyTestCase(unittest.TestCase):

    def test_subject_1(self):
        # Example 1:
        X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((-1, 1))
        assertEqual(
            minmax(X),
            np.array([0.58333333, 1. , 0.33333333, 0.77777778, 0.91666667, 0.66666667, 0. ])
        )


    def test_subject_2(self):
        # Example 2:
        Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
        assertEqual(
            minmax(Y),
            np.array([0.63636364, 1. , 0.18181818, 0.72727273, 0.93939394, 0.6969697 , 0. ])
        )


if __name__ == '__main__':
    unittest.main()
