from vec_gradient import simple_gradient
import numpy as np
import unittest


def assertEqual(x: np.ndarray, y: np.ndarray):
    np.testing.assert_array_almost_equal(x, y)


class MyTestCase(unittest.TestCase):

    def test_subject(self):
        x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
        y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))

        theta1 = np.array([2, 0.7]).reshape((-1, 1))
        assertEqual(simple_gradient(x, y, theta1), np.array([[-19.0342574], [-586.66875564]]))

        theta2 = np.array([1, -0.4]).reshape((-1, 1))
        assertEqual(simple_gradient(x, y, theta2), np.array([[-57.86823748], [-2230.12297889]]))


if __name__ == '__main__':
    unittest.main()
