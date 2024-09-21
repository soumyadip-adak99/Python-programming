class LL:
    class node:
        def __init__(self,data):
            self.data = data
            self.next = None
            
    def __init__(self):
        self.head = None
        self.size = 0
            
    def add_first(self,data): #add first logic
        new_node = self.node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
        
            
    def add_last(self,data): #add last
        new_node = self.node(data)
        if self.head is None:
            self.head = new_node
            return
        
        self.current_node = self.head
        while self.current_node.next != None:
            self.current_node = self.current_node.next
            
        self.current_node.next = new_node
            