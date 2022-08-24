from z_score import zscore
import numpy as np
import unittest


def assertEqual(x: np.ndarray, y: np.ndarray):
    np.testing.assert_array_almost_equal(x, y)


class MyTestCase(unittest.TestCase):

    def test_subject_1(self):
        # Example 1:
        X = np.array([0, 15, -9, 7, 12, 3, -21])
        assertEqual(
            zscore(X),
            np.array([-0.08620324, 1.2068453 , -0.86203236, 0.51721942, 0.94823559, 0.17240647, -1.89647119])
        )


    def test_subject_2(self):
        # Example 2:
        Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
        assertEqual(
            zscore(Y),
            np.array([
                [0.11267619],
                [1.16432067],
                [-1.20187941],
                [0.37558731],
                [0.98904659],
                [0.28795027],
                [-1.72770165]])
        )


if __name__ == '__main__':
    unittest.main()
