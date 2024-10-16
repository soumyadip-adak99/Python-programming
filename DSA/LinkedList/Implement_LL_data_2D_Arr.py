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
        
        if self.size is 1:
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
        
        if self.size is 1:
            self.delete_at_first()
            self.size -= 1
            return
        
        mid = self.size // 2
        current_node = self.head
        
        
        
            