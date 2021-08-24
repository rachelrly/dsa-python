class _Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, item):
        hold = self.head
        if hold == None:  # if no head
            self.head = _Node(item, hold, None)
            return

        node = _Node(item)  # make new node
        node.next = self.head  # set next as current head
        self.head.prev = node
        self.head = node  # set current head as node

    def insert_last(self, item):
        if self.head == None:
            return self.insert_first(item)

        node = self.head
        while node.next != None:
            node = node.next

        node.next = _Node(item, None, node)

    def show(self):
        node = self.head
        while node.next != None:
            print(f"Value: {node.value}")

            if node.prev:
                print(f"      Prev: {node.prev.value}")

            if node.next:
                print(f"      Next: {node.next.value}")
            node = node.next
        print(f'Value: {node.value}')
