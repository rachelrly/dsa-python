from ll import LinkedList

# def make_list():
#     ll = LinkedList()
#     ll.__insert_first__('one')
#     ll.__insert_last__('two')
#     ll.__insert_last__('three')
#     ll.__insert_last__('four')
#     ll.__insert_last__('five')

#     return ll


def reverse_list(ll, prev=None, node=None):
    #ternary variable declaration in Python
    thisNode = ll.head
    # if node == None else node
    print(thisNode)
    ll.__show_ll__()

    if (thisNode.next == None):
        print('exited at base')
        thisNode.next = prev
        return

    node = thisNode.next
    thisNode.next = prev
    prev = thisNode

    return reverse_list(ll, prev, node)


ll = LinkedList()
ll.__insert_first__('one')
ll.__insert_last__('two')
ll.__insert_last__('three')
ll.__insert_last__('four')
ll.__insert_last__('five')

reverse_list(ll)