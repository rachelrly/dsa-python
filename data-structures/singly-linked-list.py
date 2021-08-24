class _Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __insert_first__(self, item):
        if self.head == None:
            self.head = _Node(item, None)
        else:
            hold = self.head
            self.head = _Node(item, hold)

    def __insert_last__(self, item):
        if self.head == None:
            self.insert_first(item)
        else:
            temp_node = self.head
            while temp_node.next != None:
                temp_node = temp_node.next
            temp_node.next = _Node(item, None)

    def __find__(self, pos):
        node = self.head
        for p in range(0, pos):
            if node.next == None:
                return node
            else:
                node = node.next
        return node

    def __insert_at__(self, item, pos):
        if pos == 0: self.__insert_first__(item)
        else:
            node = self.__find__(pos - 1)
            if node.next == None:
                node.next = _Node(item, None)
            else:
                hold = node.next
                new_node = _Node(item, hold)
                node.next = new_node
                new_node.next = hold

    def __show_ll__(self):
        node = self.head
        while node.next != None:
            print(f'Value: {node.value} Next: {node.next.value}')
            node = node.next
        print(f'Value: {node.value}')

    def reverse(self):
        prev = None
        node = self.head

        while (node != None):
            hold = node.next
            node.next = prev
            prev = node
            node = hold

        self.head = prev
