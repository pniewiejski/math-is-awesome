"""
Evaluate the value of a polynomial using the Horner's method.
"""


class Polynomial:
    def __init__(self, coefficients: list):
        self._coefficients = coefficients

    def evaluate_at(self, x: float) -> float:
        result = self._coefficients[0]
        for coefficient in self._coefficients[1:]:
            result = coefficient + result * x

        return result
