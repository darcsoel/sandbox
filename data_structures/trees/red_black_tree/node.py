"""Node entity data structure"""

from data_structures.trees.red_black_tree.env import BLACK, NIL, RED


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

    @staticmethod
    def setup_empty_child(parent):
        """Set NIL value for node"""
        return Node(color=BLACK, parent=parent, value=NIL)

    def is_has_children(self):
        """Check if children are diff from NIL"""
        return self.left_child != NIL and self.right_child != NIL

    def is_red(self):
        """Check if node id red"""
        return self.color == RED

    def is_black(self):
        """Check if node id black"""
        return self.color == BLACK

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        if self.color == NIL and self.color == other.color:
            return True

        if self.parent is None or other.parent is None:
            parents_same = self.parent is None and other.parent is None
        else:
            parents_same = self.parent.value == other.parent.value \
                               and self.parent.color == other.parent.color

        node_same = self.value == other.value and self.color == other.color

        return node_same and parents_same
