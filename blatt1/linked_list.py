class Node:
    """ A single object which holds an item and a pointer to its successor. """
    def __init__(self, item):
        self.item = item
        self.next = None

    def __repr__(self):
        return str(self.item)


class SinglyLinkedList:
    """ A list object which points to the current node element and the head of the list. """
    def __init__(self):
        self.head = Node("Anchor")
        self.cur = self.head

    def __repr__(self):
        str_out = str(self.head) if self.head != self.cur else f"({str(self.head)})"
        x = self.head.next
        while x:
            str_out += f", {str(x)}" if self.cur != x else f", ({str(x)})"
            x = x.next
        return str_out


def create():
    """ Creates an empty list. """
    return SinglyLinkedList()


def get(list):
    """ Returns the object, the pointer is assigned to."""
    return list.cur.item


def reset(list):
    """ Resets the pointer at the head of the list. """
    list.cur = list.head
    return list


def next(list):
    """ Moves the pointer to the next list item. """
    list.cur = list.cur.next
    return list


def isEmpty(list):
    """ Returns `True` if the list is empty. """
    return list.head.next is None


def isLast(list):
    """ Returns `True` if the pointer points to the last element in the list. """
    return list.cur.next is None


def insert(item, list):
    """ Inserts the provided item at the current pointer position of the list element. """
    node = Node(item)
    node.next = list.cur.next
    list.cur.next = node
    return list


def delete(list):
    """ Deletes the item  """
    list.cur.next = list.cur.next.next
    return list
