class _Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self, first, last):
        self.first = None
        self.last = None

    def enqueue(self, value):
        node = _Node(value)

        if self.first == None:
          self.first = node

        if self.last !== None:
          self.last.next = node

        self.last = node

    def dequeue(self):
      if self.first == None: return
      node = self.first
      self.first = self.first.next

      if node == self.last:
        self.last = None

      return node.value
