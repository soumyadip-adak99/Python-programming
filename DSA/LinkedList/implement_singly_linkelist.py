class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        
    def add_items_beginning(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return  
        
        new_node.next = self.head
        self.head = new_node
        
    def add_items_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return  
            
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            
        current_node.next = new_node
        
    def remove_items_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
        
        self.head = self.head.next
        
    def remove_items_end(self):
        if self.head is None:
            print("List is empty.") 
            return
        
        if self.head.next is None:
            self.head = None
            return

        second_last_node = self.head
        last_node = self.head.next
        
        while last_node.next is not None:
            second_last_node = last_node 
            last_node = last_node.next  
            
        second_last_node.next = None
            
    def print_link_list(self):
        if self.head is None:
            print("List is empty.") 
            return
        
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next  
            
if __name__ == "__main__":
    obj = LL()
