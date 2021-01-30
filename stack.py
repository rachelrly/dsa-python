class _Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, top):
        self.top = null

    def push(self, item):
        if self.top == None:
            self.top = _Node(item, null)
            return

        node = _Node(item, self.top)
        self.top = node

    def pop(self):
        node = self.top
        self.top = node.next
        return node.value
