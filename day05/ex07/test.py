from vec_loss import loss_
import numpy as np
import unittest


class MyTestCase(unittest.TestCase):

    def test_subject_1(self):
        X = np.array([0, 15, -9, 7, 12, 3, -21])
        Y = np.array([2, 14, -13, 5, 12, 4, -19])

        self.assertEqual(loss_(X, Y), 2.142857142857143)
        self.assertEqual(loss_(X, X), 0.0)


if __name__ == '__main__':
    unittest.main()
