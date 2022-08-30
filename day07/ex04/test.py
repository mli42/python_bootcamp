from fit import fit_
from prediction import predict_
import numpy as np
import unittest


def assertEqual(x: np.ndarray, y: np.ndarray):
    np.testing.assert_array_almost_equal(x, y, decimal=2)


class MyTestCase(unittest.TestCase):

    def test_subject(self):
        x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
        y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
        theta = np.array([[42.], [1.], [1.], [1.]])

        theta2 = fit_(x, y, theta, alpha = 0.0005, max_iter=42000)
        assertEqual(
            theta2,
            np.array([[41.99],[0.97], [0.77], [-1.20]])
        )

        assertEqual(
            predict_(x, theta2),
            np.array([[19.5992], [-2.8003], [-25.1999], [-47.5996]])
        )


if __name__ == '__main__':
    unittest.main()
