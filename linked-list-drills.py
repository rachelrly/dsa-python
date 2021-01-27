from ll import LinkedList

test = LinkedList()

test.__insert_first__('testing1')

test.__insert_last__('testing2')
test.__insert_last__('testing3')
test.__insert_last__('testing4')
test.__insert_last__('testing5')

test.__insert_at__('testing3NEW', 0)

test.__show_ll__()
