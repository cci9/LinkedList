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

    def move_tail_to_head(self):

        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last

llist_1 = LinkedList()
llist_1.append('A')
llist_1.append('B')
llist_1.append('C')
llist_1.append('D')
llist_1.print_list()
print('\n')

llist_1.move_tail_to_head()
llist_1.print_list()
