class _Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(item, self):
        self.head = _Node(item, self.head)
    
    def insert_last(item, self):
      if self.head == None:
        insert_first(item, self)
      else:
        temp_node = self.head
        while temp_node.head