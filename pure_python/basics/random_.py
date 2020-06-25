import random


class Randomizer:
    def __init__(self):
        self._randomizer = random.SystemRandom()

    def get(self):
        return self._randomizer.random()


if __name__ == '__main__':
    for _ in range(5):
        magic_ball = Randomizer()
        print(magic_ball.get())
