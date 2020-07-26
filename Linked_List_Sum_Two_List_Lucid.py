class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:


    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        sum_llist = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_llist.print_list()


llist_1 = LinkedList()
llist_1.append(5)
llist_1.append(6)
llist_1.append(3)

llist_2 = LinkedList()
llist_2.append(8)
llist_2.append(4)
llist_2.append(2)

llist_1.print_list()
print('\n')
llist_2.print_list()
print('\n')
llist_1.sum_two_lists(llist_2)

