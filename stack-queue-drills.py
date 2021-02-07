from stack import Stack

def peek(stack):
  print(stack.top.value) 

def display(stack):
    node = stack.top
    while(node.next != None):
        print(node.value)
        node = node.next
    print(node.value)

s = Stack()

s.push('one')
s.push('two')
s.push('three')
s.push('four')
s.push('five')
