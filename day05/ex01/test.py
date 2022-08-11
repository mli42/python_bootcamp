from TinyStatistician import TinyStatistician
import unittest


class MyTestCase(unittest.TestCase):

    def test_subject(self):
        a = [1, 42, 300, 10, 59]

        self.assertEqual(TinyStatistician().mean(a), 82.4)
        self.assertEqual(TinyStatistician().median(a), 42.0)
        self.assertEqual(TinyStatistician().quartile(a), [10.0, 59.0])
        self.assertEqual(TinyStatistician().percentile(a, 10), 4.6)
        self.assertEqual(TinyStatistician().percentile(a, 15), 6.4)
        self.assertEqual(TinyStatistician().percentile(a, 20), 8.2)
        self.assertEqual(TinyStatistician().var(a), 15349.3)
        self.assertEqual(TinyStatistician().std(a), 123.89229193133849)

if __name__ == '__main__':
    unittest.main()
