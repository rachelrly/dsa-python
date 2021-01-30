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
dllist.insert_first('four')
dllist.insert_first('three')
dllist.insert_first('two')
dllist.insert_first('one')
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


def test_dll(dll):
    return


test_dll(dllist)