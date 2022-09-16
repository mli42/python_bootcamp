from data_spliter import data_spliter
import numpy as np
import unittest


def assertEqual(x: np.ndarray, y: np.ndarray, decimal: int = 6):
    np.testing.assert_array_almost_equal(x, y, decimal=decimal)


class MyTestCase(unittest.TestCase):

    def test_subject_1(self):
        x1 = np.array([1, 42, 300, 10, 59]).reshape((-1, 1))
        y = np.array([0, 1, 0, 1, 0]).reshape((-1, 1))

        # Example 1:
        ret = data_spliter(x1, y, 0.8)

        self.assertIsInstance(ret, tuple)
        self.assertTrue(all([isinstance(obj, np.ndarray) for obj in ret]))

        self.assertTrue(len(ret[0]) == len(ret[2]))
        self.assertTrue(len(ret[1]) == len(ret[3]))
        self.assertEqual(len(ret[0]), 4)
        self.assertEqual(len(ret[1]), 1)

        assertEqual(
            np.sort(np.concatenate(ret[:2]).flatten()),
            np.sort(x1.flatten())
        )
        assertEqual(
            np.sort(np.concatenate(ret[2:]).flatten()),
            np.sort(y.flatten())
        )

        # Example 2:
        ret = data_spliter(x1, y, 0.5)

        self.assertTrue(len(ret[0]) == len(ret[2]))
        self.assertTrue(len(ret[1]) == len(ret[3]))
        self.assertEqual(len(ret[0]), 2)
        self.assertEqual(len(ret[1]), 3)

        assertEqual(
            np.sort(np.concatenate(ret[:2]).flatten()),
            np.sort(x1.flatten())
        )
        assertEqual(
            np.sort(np.concatenate(ret[2:]).flatten()),
            np.sort(y.flatten())
        )


    def test_subject_2(self):
        x2 = np.array([
            [ 1, 42],
            [300, 10],
            [ 59, 1],
            [300, 59],
            [ 10, 42]])
        y = np.array([0, 1, 0, 1, 0]).reshape((-1, 1))

        # Example 3:
        ret = data_spliter(x2, y, 0.8)

        self.assertTrue(len(ret[0]) == len(ret[2]))
        self.assertTrue(len(ret[1]) == len(ret[3]))
        self.assertEqual(len(ret[0]), 4)
        self.assertEqual(len(ret[1]), 1)

        assertEqual(
            np.sort(np.concatenate(ret[:2]).flatten()),
            np.sort(x2.flatten())
        )
        assertEqual(
            np.sort(np.concatenate(ret[2:]).flatten()),
            np.sort(y.flatten())
        )

        # Example 4:
        ret = data_spliter(x2, y, 0.5)

        self.assertTrue(len(ret[0]) == len(ret[2]))
        self.assertTrue(len(ret[1]) == len(ret[3]))
        self.assertEqual(len(ret[0]), 2)
        self.assertEqual(len(ret[1]), 3)

        assertEqual(
            np.sort(np.concatenate(ret[:2]).flatten()),
            np.sort(x2.flatten())
        )
        assertEqual(
            np.sort(np.concatenate(ret[2:]).flatten()),
            np.sort(y.flatten())
        )


if __name__ == '__main__':
    unittest.main()
