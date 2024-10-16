class Node:
    def __init__(self, data,row, col):
        self.data = [[data[i][j] for j in range(row)] for i in range(col)]
        self.next = None
   
        
class Linkedlist:
    def __init__(self,row,col):
        self.head = None
        self.row = row
        self.col = col
        self.size = 0
        
    def add_at_first(self, data):
        new_node = Node(data, self.row, self.col)
        
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def add_at_mid(self, data):
        new_node = Node(data, self.row, self.col)
        
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        
        if self.size == 1:
            self.head.next = new_node
            self.size += 1
        
        mid = self.size // 2
        current_node = self.head
        
        for i in range(mid - 1):
            current_node = current_node.next
            
        new_node.next = current_node.next
        current_node.next = new_node
        self.size += 1
            

    def add_at_last(self, data):
        new_node = Node(data, self.row, self.col)
        
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
        
        self.size -= 1       
        self.head = self.head.next
        
        
    def delete_at_mid(self):
        if self.head is None:
            print("List is empty.")
            return
        
        mid = self.size // 2
        
        if self.size == 1:
            self.delete_at_first()
            self.size -= 1
            return
        
        mid = self.size // 2
        current_node = self.head

        for i in range(mid - 1):
            current_node = current_node.next

        current_node.next = current_node.next.next

    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        second_last_node = self.head
        last_node = self.head.next

        while last_node.next is not None:
            last_node = last_node.next
            second_last_node = second_last_node.next

        second_last_node.next = None


    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return

        current_node =  self.head
        while current_node is not None:
            print(current_node.data,end="->")
            current_node = current_node.next


if __name__ == "__main__":
    n = Linkedlist(3, 3)

    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [3, 2, 1],
        [6, 5, 4],
        [9, 8, 7]
    ]

    c = [
        [2, 1, 3],
        [5, 4, 6],
        [5, 7, 9]
    ]

    n.add_at_first(a)
    n.add_at_last(b)
    n.add_at_mid(c)

    n.print_list()


        
        
            