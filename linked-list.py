class _Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(item, self):
        if self.head == None:
          self.head = _Node(item, self.head)
        else:
          hold = self.head
          self.head = _Node(item, hold)
    
    def insert_last(item, self):
      if self.head == None:
        insert_first(item, self)
      else:
        temp_node = self.head
        while temp_node.next != None
          temp_node = temp_node.next
        temp_node.next = _Node(item, None)
    
    def find(self, pos):
      node = self.head
      for p in pos:
        if node.next == None:
          return node
        else:
          node = node.next
      return pos

    def insert_at(self, item, pos):
      node = find(pos)
      if node.next == None:
          node.next = _Node(item, None)
      else:
        hold = node.next
        new_node = _Node(item, hold)
        node.next = new_node
        new_node.next = hold
    