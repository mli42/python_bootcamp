from prediction import predict_
import numpy as np
import unittest


def assertEqual(x, y):
    np.testing.assert_array_almost_equal(x, y)


class MyTestCase(unittest.TestCase):

    def test_subject(self):
        x = np.arange(1,13).reshape((4,-1))

        theta1 = np.array([5, 0, 0, 0]).reshape((-1, 1))
        theta2 = np.array([0, 1, 0, 0]).reshape((-1, 1))
        theta3 = np.array([-1.5, 0.6, 2.3, 1.98]).reshape((-1, 1))
        theta4 = np.array([-3, 1, 2, 3.5]).reshape((-1, 1))

        assertEqual(predict_(x, theta1), np.array([[5.], [5.], [5.], [5.]]))
        assertEqual(predict_(x, theta2), np.array([[ 1.], [ 4.], [ 7.], [10.]]))
        assertEqual(predict_(x, theta3), np.array([[ 9.64], [24.28], [38.92], [53.56]]))
        assertEqual(predict_(x, theta4), np.array([[12.5], [32. ], [51.5], [71. ]]))


if __name__ == '__main__':
    unittest.main()
