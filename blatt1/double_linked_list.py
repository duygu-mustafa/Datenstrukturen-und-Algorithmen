class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.item)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node("Anchor")
        self.tail = Node("Sentinel")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cur = self.head

    def __repr__(self):
        str_out = str(self.head) if self.head != self.cur else f"({str(self.head)})"
        x = self.head.next
        while x:
            str_out += f", {str(x)}" if self.cur != x else f", ({str(x)})"
            x = x.next
        return str_out


def create():
    return DoublyLinkedList()


def get(list):
    return list.cur.item


def reset(list):
    list.cur = list.head
    return list


def next(list):
    list.cur = list.cur.next
    return list


def prev(list):
    list.cur = list.cur.prev
    return list


def isEmpty(list):
    return list.head.next.item == "Sentinel"


def isLast(list):
    return list.cur.next.item == "Sentinel"


def insert(item, list):
    """ Insert item into list"""
    node = Node(item)
    node.prev = list.cur
    node.next = list.cur.next
    node.prev.next = node
    node.next.prev = node
    return list


def delete(list):
    """Deletes current item from list"""
    if list.cur.prev is not None:
        list.cur.prev.next = list.cur.next
        list.cur.next.prev = list.cur.prev
        list.cur = list.cur.prev
    return list


def length(list):
    """ Returns the count of the elements in the list"""
    length = 0
    init_cur = list.cur
    list.cur = list.head
    while list.cur.next != list.tail:
        length += 1
        next(list)
    list.cur = init_cur
    return length


def join(list, list2):
    """ Joins two lists into a single one. """
    start_cur = list.cur
    list.cur = list.tail.prev
    list2.cur = list2.head.next
    while list2.cur != list2.tail:
        insert(get(list2), list)
        next(list)
        next(list2)
    list.cur = start_cur
    return list


def split(list):
    """ Splits the list into two list at the position of the current pointer. """

    list1 = DoublyLinkedList()
    if list.cur != list.head:
        pointer = list.cur
        list.cur = list.head.next
        while list.cur.prev != pointer:
            if list.cur != list.tail:
                insert(get(list), list1)
            next(list1)
            if list.cur == list.tail:
                break
            next(list)

    list2 = DoublyLinkedList()
    while list.cur != list.tail:
        if list.cur != list.head:
            insert(get(list), list2)
            next(list2)
        next(list)
    list2.cur = list2.head

    return list1, list2


def cycle(list):
    """ Cycles the list by one element forward, such that the last element in the list becomes the first one. """
    init_current = list.cur

    last = list.tail.prev.item

    list.cur = list.tail.prev
    delete(list)

    list.cur = list.head
    insert(last, list)

    list.cur = init_current
    return list


def swap(list):
    """ Swap the current element with the next element in the list. """
    cur_el = list.cur
    next_el = list.cur.next
    nextnext = next_el.next
    prev_el = cur_el.prev

    cur_el.prev.next = next_el
    next_el.next.prev = cur_el
    next_el.next = cur_el
    next_el.prev = prev_el

    cur_el.prev = next_el
    cur_el.next = nextnext
    return list


def reverse(list):
    """ Reverse the order of elements in the list. """
    init_cur = get(list)

    #optimise later
    list.cur = list.head.next

    # # swap(list)
    # while list.cur != list.tail:
    #     temp = list.cur.prev
    #     list.cur.prev = list.cur.next
    #     list.cur.next = temp
    #     list.cur = list.cur.prev

    res_list = DoublyLinkedList()
    while list.cur != list.tail:
        insert(get(list), res_list)
        next(list)

    while get(res_list) != init_cur:
        next(res_list)
    return res_list




# assert_equal(str(list), "(Anchor), 4, 3, 2, 1, Sentinel")
list = insert(1, insert(2, insert(3, insert(4, create()))))
list = cycle(list)
print(list)