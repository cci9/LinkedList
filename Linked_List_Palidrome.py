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

    def is_palindrome_method1(self):
        s = ''
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    def is_palindrome_method2(self):
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def is_palindrome_method3(self):
        p = self.head
        q = self.head
        prev = []

        i = 0
        while q:
            prev.append(q)
            q = q.next
            i = i + 1
        q = prev[i - 1]

        count = 1
        while count <= i//2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True





llist_1 = LinkedList()
llist_1.append('R')
llist_1.append('A')
llist_1.append('D')
llist_1.append('A')
llist_1.append('R')
llist_1.print_list()
print('\n')
llist_2 = LinkedList()
llist_2.append('A')
llist_2.append('B')
llist_2.append('C')
llist_2.print_list()

print(llist_1.is_palindrome_method1())
print(llist_2.is_palindrome_method1())

print(llist_1.is_palindrome_method2())
print(llist_2.is_palindrome_method2())

print(llist_1.is_palindrome_method3())
print(llist_2.is_palindrome_method3())
