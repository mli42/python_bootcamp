from gradient import gradient
import numpy as np
import unittest


def assertEqual(x: np.ndarray, y: np.ndarray):
    np.testing.assert_array_almost_equal(x, y)


class MyTestCase(unittest.TestCase):

    def test_subject(self):
        x = np.array([
            [ -6, -7, -9],
            [ 13, -2, 14],
            [ -7, 14, -1],
            [ -8, -4, 6],
            [ -5, -9, 6],
            [ 1, -5, 11],
            [ 9, -11, 8]])
        y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))

        theta1 = np.array([0, 3, 0.5, -6]).reshape((-1, 1))
        assertEqual(
            gradient(x, y, theta1),
            np.array([[ -33.71428571], [ -37.35714286], [183.14285714], [-393.]])
        )

        theta2 = np.array([0, 0, 0, 0]).reshape((-1, 1))
        assertEqual(
            gradient(x, y, theta2),
            np.array([[ -0.71428571], [ 0.85714286], [23.28571429], [-26.42857143]])
        )


if __name__ == '__main__':
    unittest.main()
