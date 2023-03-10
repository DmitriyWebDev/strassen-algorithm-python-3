import unittest
from ..strassen_with_vanila_python_3 import strassen


class MyTestCase(unittest.TestCase):
    def test_strassen_with_vanila_python_3(self):
        matrix_a = [
            [3, 5, 1, 3],
            [1, 2, 3, 4],
            [4, 5, 6, 8],
            [7, 8, 9, 3]
        ]
        matrix_b = [
            [4, 1, 2, 3],
            [1, 2, 1, 6],
            [2, 4, 6, 2],
            [6, 2, 5, 4]
        ]
        matrix_result = [
            [37, 23, 32, 53],
            [36, 25, 42, 37],
            [81, 54, 89, 86],
            [72, 65, 91, 99]
        ]

        self.assertEqual(strassen(matrix_a, matrix_b), matrix_result)

    def test_case_1(self):
        matrix_a = [
            [3, 5, 1, 3],
            [1, 2, 3, 4],
        ]
        matrix_b = [
            [4, 1, 2, 3],
            [1, 2, 1, 6],
            [2, 4, 6, 2],
            [6, 2, 5, 4]
        ]
        matrix_result = [
            [37, 23, 32, 53],
            [36, 25, 42, 37],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.assertEqual(strassen(matrix_a, matrix_b), matrix_result)

    def test_case_2(self):
        matrix_a = [
            [1],
        ]
        matrix_b = [
            [4, 1, 2],
            [1, 2],
            [],
            [6]
        ]
        matrix_result = [
            [4, 1, 2, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.assertEqual(strassen(matrix_a, matrix_b), matrix_result)


if __name__ == '__main__':
    unittest.main()
