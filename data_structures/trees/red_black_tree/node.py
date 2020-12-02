from .env import RED, BLACK, NIL


class Node:
    """
    Node instance, red or black
    Must contain children and parent

    """

    def __init__(self, color=RED, value=None, left_child=None,
                 right_child=None, parent=None):
        """At start - node always red, recolor on condition"""
        self._check_color(color)

        self.color = color
        self.value = value
        self.parent = parent

        self.left_child = left_child or self.setup_empty_child(value)
        self.right_child = right_child or self.setup_empty_child(value)

    @staticmethod
    def _check_color(color):
        if color in [BLACK, RED]:
            return True
        raise ValueError(f'wrong element color - {color}')

    def setup_empty_child(self, parent):
        return Node(color=BLACK, parent=parent, value=NIL)

    def is_has_children(self):
        return self.left_child == NIL and self.right_child == NIL

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value
