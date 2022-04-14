import unittest

from blatt1.linked_list import insert, create, delete, next


class TestLinkedList(unittest.TestCase):
    def test_insert(self):
        list = create()
        self.assertEqual(str(list), "(Anchor)")

        list = insert(1, insert(2, insert(3, list)))
        self.assertEqual(str(list), "(Anchor), 1, 2, 3")

    def test_delete(self):
        list = insert(1, insert(2, insert(3, insert(4, create()))))

        list = delete(next(list))
        self.assertEqual(str(list), "Anchor, (1), 3, 4")



