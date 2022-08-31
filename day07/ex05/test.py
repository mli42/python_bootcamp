from mylinearregression import MyLinearRegression as MyLR
import numpy as np
import unittest


def assertEqual(x: np.ndarray, y: np.ndarray, decimal: int = 6):
    np.testing.assert_array_almost_equal(x, y, decimal=decimal)


class MyTestCase(unittest.TestCase):

    def test_subject_1(self):
        X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
        Y = np.array([[23.], [48.], [218.]])
        mylr = MyLR(np.array([[1.], [1.], [1.], [1.], [1]]))

        # Example 0.0:
        y_hat = mylr.predict_(X)

        assertEqual(
            y_hat,
            np.array([[8.], [48.], [323.]])
        )

        # Example 0.1:
        assertEqual(
            mylr.loss_elem_(Y, y_hat),
            np.array([[225.], [0.], [11025.]])
        )

        # Example 0.2:
        self.assertAlmostEqual(mylr.loss_(Y, y_hat), 1875.0)

        # Example 3:
        mylr.alpha = 1.6e-4
        mylr.max_iter = 200000
        mylr.fit_(X, Y)

        assertEqual(
            mylr.thetas,
            np.array([[18.188], [2.767], [-0.374], [1.392], [0.017]]),
            3
        )

        # Example 4:
        y_hat = mylr.predict_(X)

        assertEqual(
            y_hat,
            np.array([[23.417], [47.489], [218.065]]),
            3
        )

        # Example 5:
        assertEqual(
            mylr.loss_elem_(Y, y_hat),
            np.array([[0.174], [0.260], [0.004]]),
            3
        )

        # Example 6:
        self.assertAlmostEqual(
            mylr.loss_(Y, y_hat),
            0.0732,
            4
        )


if __name__ == '__main__':
    unittest.main()
