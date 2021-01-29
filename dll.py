class _Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    def insert_first(self, item):
        hold = self.head
        self.head.prev = item
        self.head = _Node(item, hold, None)

    def insert_last(self, item):
        if self.head == None:
            return self.insert_first(item)

        node = self.head
        while node.next != None:
            node = node.next

        node.next = _Node(item, None, node)
