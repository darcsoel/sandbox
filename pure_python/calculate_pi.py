import random


def calculate_pi(points_count=1000):
    circle_points = 0
    square_points = 0

    for _ in range(points_count):
        point_x = random.uniform(0, 1)
        point_y = random.uniform(0, 1)

        if point_x ** 2 + point_y ** 2 < 1:
            circle_points += 1
        square_points += 1

    return 4 * circle_points / square_points


if __name__ == '__main__':
    print(calculate_pi(3_000_000))
