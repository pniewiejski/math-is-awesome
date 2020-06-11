import unittest

from horners_method.horners_method import Polynomial


class TestPolynomialEvaluation(unittest.TestCase):

    def test_horner_method(self):
        polynomial = Polynomial([2, -6, 2, -1])
        result = polynomial.evaluate_at(3)
        self.assertEqual(5.0, result)


if __name__ == "__main__":
    unittest.main()
