import unittest

from data_structures.linked_list.list_item import ListItem
from data_structures.linked_list.singly_linked_list import LinkedList


class LinkedListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.check_list = ['test1', 'test2', 'test3', 'test4', 'test5']
        self.linked_list = LinkedList([ListItem(x) for x in self.check_list])

    def test_initial(self):
        self.assertEqual(self.linked_list.get(), self.check_list)

    def test_pop(self):
        linked_list_elements = self.linked_list.get()
        linked_list_len = len(self.linked_list)
        self.linked_list.pop()
        linked_list_new_len = len(self.linked_list)
        self.assertEqual(linked_list_len, linked_list_new_len + 1)
        linked_list_new_elems = self.linked_list.get()
        self.assertEqual(linked_list_elements[1:], linked_list_new_elems)

    def test_add(self):
        linked_list_elements = self.linked_list.get()
        linked_list_len = len(self.linked_list)
        first_node = ListItem('test1')
        self.linked_list.add(first_node)
        linked_list_new_len = len(self.linked_list)
        linked_list_new_elements = self.linked_list.get()
        self.assertEqual(linked_list_len, linked_list_new_len - 1)
        linked_list_elements.insert(0, 'test1')
        self.assertEqual(linked_list_elements, linked_list_new_elements)

    def test_push(self):
        linked_list_elements = self.linked_list.get()
        first_node = ListItem('test1')
        self.linked_list.push(first_node)
        linked_list_new_elements = self.linked_list.get()
        linked_list_elements.append('test1')
        self.assertEqual(linked_list_elements, linked_list_new_elements)

    def test_delete_not_first(self):
        linked_list_elements = self.linked_list.get()
        second_node = ListItem('test2')
        self.linked_list.delete(second_node)
        linked_list_new_elements = self.linked_list.get()
        linked_list_elements.remove('test2')
        self.assertEqual(linked_list_elements, linked_list_new_elements)

    def test_delete_first(self):
        linked_list_elements = self.linked_list.get()
        first_node = self.linked_list.get_first_value()
        to_delete = ListItem(first_node)
        self.linked_list.delete(to_delete)
        linked_list_new_elements = self.linked_list.get()
        linked_list_elements.remove(first_node)
        self.assertEqual(linked_list_elements, linked_list_new_elements)


if __name__ == '__main__':
    unittest.main()
