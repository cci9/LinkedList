class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def delete_node(self, node):
        cur = self.head

        while cur:
            if cur == node and cur == self.head:
                # Case 1
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # Case 2
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur == node:
                # Case 3
                if cur.next:
                    nxt = cur.next
                    prv = cur.prev
                    prv.next = nxt
                    nxt.prev = prv
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # Case 4
                else:
                    prv = cur.prev
                    prv.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next


    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.print_list()
dllist.remove_duplicates()
print('\n')
dllist.print_list()
