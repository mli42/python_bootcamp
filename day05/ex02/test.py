from prediction import simple_predict
import numpy as np
import unittest


def assertEqual(x, y):
    np.testing.assert_array_equal(x, y)


class MyTestCase(unittest.TestCase):

    def test_subject(self):
        x = np.arange(1,6)

        theta1 = np.array([5, 0])
        theta2 = np.array([0, 1])
        theta3 = np.array([5, 3])
        theta4 = np.array([-3, 1])

        assertEqual(simple_predict(x, theta1), np.array([5., 5., 5., 5., 5.]))
        assertEqual(simple_predict(x, theta2), np.array([1., 2., 3., 4., 5.]))
        assertEqual(simple_predict(x, theta3), np.array([ 8., 11., 14., 17., 20.]))
        assertEqual(simple_predict(x, theta4), np.array([-2., -1.,  0.,  1.,  2.]))

        assertEqual(simple_predict(np.array([[1, 2, 3], [4, 5, 6]]), theta4), None)


if __name__ == '__main__':
    unittest.main()
