from ll import LinkedList

llist = LinkedList()
llist.__insert_first__('one')
llist.__insert_last__('two')
llist.__insert_last__('three')
llist.__insert_last__('four')
llist.__insert_last__('five')

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


def find_list_center(ll):
    node = ll.head
    fast_pointer = ll.head

    while (fast_pointer.next != None):
        node = node.next
        fast_pointer = node.next.next

    return node


#find_list_center(llist)