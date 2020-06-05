"""
Barnsley fern

https://en.wikipedia.org/wiki/Barnsley_fern
https://en.wikipedia.org/wiki/Affine_transformation
"""

import random
from typing import NewType, Callable
from enum import Enum, unique

import numpy as np


@unique
class TransformationType(Enum):
    F1 = "f1"
    F2 = "f2"
    F3 = "f3"
    F4 = "f4"


Transformation = NewType("Transformation", Callable[[TransformationType], TransformationType])

TRANSFORMATION_PARAMETERS = {
    TransformationType.F1: (np.array([[0, 0], [0, 0.16]]), np.array([0, 0])),
    TransformationType.F2: (np.array([[0.85, 0.04], [-0.04, 0.85]]), np.array([0, 1.60])),
    TransformationType.F3: (np.array([[0.2, -0.26], [0.23, 0.22]]), np.array([0, 1.60])),
    TransformationType.F4: (np.array([[-0.15, 0.28], [0.26, 0.24]]), np.array([0, 0.44])),
}


def draw_transformation_type():
    number = random.uniform(0, 1)
    if 0 < number < 0.01:
        # probability 0.01
        return TransformationType.F1
    elif 0.01 <= number < 0.86:
        # probability 0.85
        return TransformationType.F2
    elif 0.86 <= number < 0.93:
        # probability 0.07
        return TransformationType.F3
    else:
        # probability 0.07
        return TransformationType.F4


def transformation(A: np.ndarray, b: np.ndarray, x: np.ndarray) -> np.ndarray:
    return A.dot(x) + b


def get_transformation_strategy(transformation_type: TransformationType) -> Transformation:
    A, b = TRANSFORMATION_PARAMETERS[transformation_type]

    def transformation_impl(x: np.ndarray) -> np.ndarray:
        return transformation(A, b, x)

    return transformation_impl


def generate_transformations(number_of_transformations_to_generate: int) -> Transformation:
    for _ in range(number_of_transformations_to_generate):
        transformation_type = draw_transformation_type()
        yield get_transformation_strategy(transformation_type)


def barnsley_fern(number_of_points: int) -> np.ndarray:
    point = np.array([0, 0])  # initial point (x, y) = (0, 0)

    for transformation_impl in generate_transformations(number_of_points):
        transformed = transformation_impl(point)
        yield point
        point = transformed


if __name__ == "__main__":
    import matplotlib.pyplot as plt


    def subplot(number_of_points, axies):
        calculated_points = np.array(list(barnsley_fern(number_of_points))).transpose()
        x = calculated_points[0][:]
        y = calculated_points[1][:]

        axies.set_aspect("equal", "box")
        plt.scatter(x, y, s=0.01, c="g")
        plt.title(f"No. of points: {number_of_points}")


    fig = plt.figure()

    ax = fig.add_subplot(131)
    subplot(8000, ax)

    ax = fig.add_subplot(132)
    subplot(80000, ax)

    ax = fig.add_subplot(133)
    subplot(800000, ax)

    plt.show()
