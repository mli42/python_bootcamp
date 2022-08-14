from other_losses import mse_, rmse_, mae_, r2score_
import numpy as np
import unittest
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class MyTestCase(unittest.TestCase):

    def test_mse(self):
        x = np.array([0, 15, -9, 7, 12, 3, -21])
        y = np.array([2, 14, -13, 5, 12, 4, -19])

        self.assertAlmostEqual(mse_(x, y), mean_squared_error(x, y))
        self.assertAlmostEqual(rmse_(x, y), mean_squared_error(x, y, squared=False))
        self.assertAlmostEqual(mae_(x, y), mean_absolute_error(x, y))
        self.assertAlmostEqual(r2score_(x, y), r2_score(x, y))


if __name__ == '__main__':
    unittest.main()
