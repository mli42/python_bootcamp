from matrix import Matrix, Vector
import unittest


class MyTestCase(unittest.TestCase):

    def vector_basics(self):
        v1 = Vector([[1, 2, 3]]) # create a row vector
        v2 = Vector([[1], [2], [3]]) # create a column vec

        self.assertEqual(repr(v1), "Vector([[1, 2, 3]])")
        self.assertEqual(repr(v2), "Vector([[1], [2], [3]])")

        with self.assertRaises(Exception):
            v3 = Vector([[1, 2], [3, 4]]) # return an error


    def test_subject_1(self):
        m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])

        self.assertEqual(repr(m1) , "Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])")
        self.assertEqual(m1.shape , (3, 2))
        self.assertEqual(repr(m1.T()), "Matrix([[0.0, 2.0, 4.0], [1.0, 3.0, 5.0]])")
        self.assertEqual(m1.T().shape , (2, 3))


    def test_subject_2(self):
        m1 = Matrix([[0., 2., 4.], [1., 3., 5.]])

        self.assertEqual(m1.shape, (2, 3))
        self.assertEqual(repr(m1.T()), "Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])")
        self.assertEqual(m1.T().shape, (3, 2))


    def test_subject_3(self):
        m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
                    [0.0, 2.0, 4.0, 6.0]])
        m2 = Matrix([[0.0, 1.0],
                    [2.0, 3.0],
                    [4.0, 5.0],
                    [6.0, 7.0]])

        self.assertEqual(repr(m1 * m2), "Matrix([[28.0, 34.0], [56.0, 68.0]])")

        m1 = Matrix([[0.0, 1.0, 2.0],
                    [0.0, 2.0, 4.0]])
        v1 = Vector([[1], [2], [3]])

        self.assertIn(repr(m1 * v1), ("Matrix([[8], [16]])", "Vector([[8], [16]"))


    def test_subject_4(self):
        v1 = Vector([[1], [2], [3]])
        v2 = Vector([[2], [4], [8]])

        self.assertEqual(repr(v1 + v2), "Vector([[3], [6], [11]])")

if __name__ == '__main__':
    unittest.main()
