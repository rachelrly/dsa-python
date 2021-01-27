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

    def __insert_last__(item, self):
        if self.head == None:
            insert_first(item, None)
        else:
            temp_node = self.head
            while temp_node.next != None:
                temp_node = temp_node.next
            temp_node.next = _Node(item, None)

    def __find__(self, pos):
        node = self.head
        for p in pos:
            if node.next == None:
                return node
            else:
                node = node.next
        return pos

    def __insert_at__(self, item, pos):
        node = find(pos)
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
            print(f'Value: {node.value} node.next: {node.next.value}')
            node = node.next
        print(f'Value: {node.value}')
