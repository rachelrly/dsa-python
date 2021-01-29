from ll import LinkedList

llist = LinkedList()
llist.__insert_first__('one')
llist.__insert_last__('two')
llist.__insert_last__('three')
llist.__insert_last__('four')
llist.__insert_last__('five')


# alternate solution
def three_from_end(llist):
    reverse_ll = llist.reverse()
    node = reverse_ll.head

    for node in range(0, 3):
        node = node.next

    return node


def find_list_center(ll):
    prev = None
    node = ll.head
    i = 0

    while (node.next != None):
        hold = node.next
        node.next = prev
        prev = node
        node = hold
        i += 1

    j = i // 2  # half way through list

    for n in range(0, j):
        node = node.next

    print(node.value)
    return node


find_list_center(llist)