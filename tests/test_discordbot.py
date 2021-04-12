import unittest


class Test_Bot(unittest.TestCase):

    def test_addition(self):
        answer = 1 + 0
        expected = 2
        self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()
