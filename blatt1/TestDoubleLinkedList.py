import unittest

from blatt1.double_linked_list import insert, create, delete, length, join, split, cycle, swap, reverse, next


class TestDoubleLinkedList(unittest.TestCase):
    def test_insert(self):
        list = insert(4, insert(3, insert(2, insert(1, create()))))
        self.assertEqual(str(list), "(Anchor), 4, 3, 2, 1, Sentinel")

    def test_delete(self):
        list = insert(4, insert(3, insert(2, insert(1, create()))))
        list = delete(next(list))
        self.assertEqual(str(list), "(Anchor), 3, 2, 1, Sentinel")

        list = create()
        list = delete(list)
        self.assertEqual(str(list), "(Anchor), Sentinel")

    def test_length(self):
        list = create()
        self.assertEqual(length(list), 0)

        list = insert(4, insert(3, insert(2, insert(1, create()))))
        self.assertEqual(length(list), 4)

    def test_join(self):
        list1 = insert(1, insert(2, insert(3, insert(4, create()))))
        list2 = insert(5, insert(6, insert(7, insert(8, create()))))

        list = join(list1, list2)
        self.assertEqual(str(list), "(Anchor), 1, 2, 3, 4, 5, 6, 7, 8, Sentinel")

    def test_split(self):
        list = insert(1, insert(2, insert(3, insert(4, create()))))
        list1, list2 = split(list)
        self.assertEqual(str(list1), "(Anchor), Sentinel")
        self.assertEqual(str(list2), "(Anchor), 1, 2, 3, 4, Sentinel")

        list = insert(1, insert(2, insert(3, insert(4, create()))))
        list = next(next(list))
        list1, list2 = split(list)
        self.assertEqual(str(list1), "Anchor, 1, (2), Sentinel")
        self.assertEqual(str(list2), "(Anchor), 3, 4, Sentinel")

        list = create()
        list1, list2 = split(list)
        self.assertEqual(str(list1), "(Anchor), Sentinel")
        self.assertEqual(str(list2), "(Anchor), Sentinel")

        list = next(create())
        list1, list2 = split(list)
        self.assertEqual(str(list1), "Anchor, (Sentinel)")
        self.assertEqual(str(list2), "(Anchor), Sentinel")

    def test_cycle(self):
        list = insert(1, insert(2, insert(3, insert(4, create()))))
        list = cycle(list)
        self.assertEqual(str(list), "(Anchor), 4, 1, 2, 3, Sentinel")

    def test_swap(self):
        list = next(insert(1, insert(2, insert(3, insert(4, create())))))
        list = swap(list)
        self.assertEqual(str(list), "Anchor, 2, (1), 3, 4, Sentinel")

    def test_reverse(self):
        list = insert(1, insert(2, insert(3, insert(4, create()))))
        list = reverse(list)
        self.assertEqual(str(list), "(Anchor), 4, 3, 2, 1, Sentinel")


if __name__ == '__main__':
    unittest.main()


