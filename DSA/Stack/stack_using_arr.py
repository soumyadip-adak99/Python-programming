class stack:
    def __init__(self,size):
        self.size = size
        self.top = -1
        self.arr= [None] *size

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.size -1
    
    def push(self,value):
        if self.is_full():
            print("Stack over flow")
            return

        self.top += 1
        self.arr[self.top] = value
        
        
    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
            return -1

        value = self.arr[self.top]
        self.top -= 1
        return value
    
    def peek(self, pos):
        str_idx = self.top - (pos - 1)

        if str_idx < 0:
            print("Stack underflow.")
            return 0

        return self.arr[str_idx]
        
        
if __name__ == "__main__":
    s = stack(3)
    
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    
    for i in range(1, s.top + 2):
        print(f"Position-> {s.top - i + 1} -> {s.peek(i)}")
        
        
