from .env import *


class Node:
    """
    Node instance, red or black
    Must contain children and parent

    """

    def __init__(self, color=RED, value=None, left_child=None, right_child=None, parent=None):
        self.color = color
        self.value = value
        self.parent = parent
        self.left_child = left_child if left_child else Node(color=BLACK, parent=value)
        self.right_child = right_child if right_child else Node(color=BLACK, parent=value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value
