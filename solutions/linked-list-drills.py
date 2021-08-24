from ll import LinkedList
from dll import DoublyLinkedList

# llist = LinkedList()
# llist.__insert_first__('one')
# llist.__insert_last__('two')
# llist.__insert_last__('three')
# llist.__insert_last__('four')
# llist.__insert_last__('five')

dllist = DoublyLinkedList()
dllist.insert_first('five')
dllist.insert_last('four')
dllist.insert_last('three')
dllist.insert_last('two')
dllist.insert_last('one')
dllist.show()


#singly linked list
def three_from_the_end(llist):
    node = llist.head
    while node.next.next.next != None:
        node = node.next
    return node


# alternate solution
def three_from_end_alt(llist):
    reverse_ll = llist.reverse()
    node = reverse_ll.head

    for node in range(0, 3):
        node = node.next

    return node


#singly linked list
def find_list_center(ll):
    node = ll.head
    fast_pointer = ll.head

    while (fast_pointer.next != None):
        node = node.next
        fast_pointer = node.next.next

    return node


def reverse_dll(dll, node=None, prev=None):
    node = dll.head if node == None else node

    if next == None:
        node.next = prev
        prev.prev = node
        dll.head = prev
        return

    hold = node.next
    node.next = prev
    node.prev = node.next
    node = hold
    prev = node.prev

    dll.show()

    reverse_dll(dll, node, prev)


reverse_dll(dllist)

#hold the previous node and
# def __recurse_reverse__(self, node, prev=None):
#     hold = node.next
#     node.next = prev
#     hold.next = node
#     if node.next == None:
#         self.__show_ll__()
#         return

#     self.__recurse_reverse__(hold, node)

# def recurse_reverse(self):
#     return self.__recurse_reverse__(self.head)
