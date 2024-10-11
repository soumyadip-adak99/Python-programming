class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None
        self.size = 0

    def addFirst(self, data): #add first
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addLast(self, data): #add last
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
        self.size += 1

    def delete_first(self): #delete first
        if self.head is None:
            print("This list is empty.")
            return
        self.size -= 1
        self.head = self.head.next

    def delete_last(self): #delete last
        if self.head is None:
            print("This list is empty.")
            return

        self.size -= 1
        if self.head.next is None:
            self.head = None
            return

        second_last_node = self.head
        last_node = self.head.next
        while last_node.next is not None:
            last_node = last_node.next
            second_last_node = second_last_node.next

        second_last_node.next = None


    def get_size(self): #get size
        return self.size

    def print_list(self): #print list
        if self.head is None:
            print("This list is empty.")
            return

        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end= " ")
            curr_node = curr_node.next

if __name__ == "__main__":
    n = Linklist()
    n.addLast(10)
    n.addLast(20)
    n.addLast(30)
    n.delete_last()
    n.delete_first()
    n.print_list()
    print("\nsize->", n.get_size())


























