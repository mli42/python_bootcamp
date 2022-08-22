from my_linear_regression import MyLinearRegression as MyLR
import numpy as np
import unittest


def assertEqual(x: np.ndarray, y: np.ndarray):
    np.testing.assert_array_almost_equal(x, y)


class MyTestCase(unittest.TestCase):

    def test_subject_1(self):
        x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
        y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])

        lr1 = MyLR(np.array([[2], [0.7]]))

        # Example 0.0:
        y_hat = lr1.predict_(x)

        assertEqual(
            y_hat,
            np.array([
                [10.74695094],
                [17.05055804],
                [24.08691674],
                [36.24020866],
                [42.25621131]])
        )

        # Example 0.1:
        assertEqual(
            lr1.loss_elem_(y, y_hat),
            np.array([
                [71.04586738],
                [36.46864549],
                [46.99622165],
                [10.89755341],
                [29.9371111 ]])
        )

        # Example 0.2:
        self.assertAlmostEqual(lr1.loss_(y, y_hat), 195.34539903032385)

    def test_subject_2(self):
        x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
        y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])

        lr2 = MyLR(np.array([[1], [1]]), 5e-8, 1500000)

        # Example 1.0:
        lr2.fit_(x, y)

        assertEqual(
            lr2.thetas,
            np.array([
                [1.40709365],
                [1.1150909 ]])
        )

        # Example 1.1:
        y_hat = lr2.predict_(x)

        assertEqual(
            y_hat,
            np.array([
                [15.3408728 ],
                [25.38243697],
                [36.59126492],
                [55.95130097],
                [65.53471499]])
        )

        # Example 1.2:
        assertEqual(
            lr2.loss_elem_(y, y_hat),
            np.array([
                [48.66660486],
                [11.58827842],
                [ 8.4167116 ],
                [ 8.59691972],
                [ 3.57144835]])
        )

        # Example 1.3:
        self.assertAlmostEqual(lr2.loss_(y, y_hat), 80.83996294128525)


if __name__ == '__main__':
    unittest.main()
