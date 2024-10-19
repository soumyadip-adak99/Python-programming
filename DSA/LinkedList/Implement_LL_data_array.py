import numpy as np

class Node:
    def __init__(self, data):
        self.data = np.array(data)
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_at_first(self, data):  # Add items at the first position
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_at_mid(self, data):  # Add items at the middle position
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        mid = self.size // 2
        current_node = self.head

        for i in range(mid - 1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
        self.size += 1

    def add_at_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        self.size += 1

    def delete_at_first(self):
        if self.head is None:
            print("List is empty.")
            return

        self.head = self.head.next
        self.size -= 1

    def delete_at_mid(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.size == 1:
            self.delete_at_first()
            return

        mid = self.size // 2
        current_node = self.head

        for i in range(mid - 1):
            current_node = current_node.next

        current_node.next = current_node.next.next
        self.size -= 1

    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.size == 1:
            self.delete_at_first()
            return

        second_last_node = self.head
        last_node = self.head.next

        while last_node.next is not None:
            last_node = last_node.next
            second_last_node = second_last_node.next

        second_last_node.next = None
        self.size -= 1

    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return

        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

if __name__ == "__main__":
    n = LinkList()

    a = [1, 2, 3]
    b = [3, 2, 1]
    c = [2, 1, 3]

    n.add_at_first(a)
    n.add_at_last(b)
    n.add_at_mid(c)

    n.print_list()
