class Node:
    def __init__(self, data):
        self.ch = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def add(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
            return

        new_node.next = self.top
        self.top = new_node

    def remove_data(self):
        if self.top is None:
            print("Stack is empty")
            return '\0'

        remove_val = self.top.ch
        self.top = self.top.next
        return remove_val

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return '\0'

        return self.top.ch

if __name__ == "__main__":
    input_str = input("Enter a string: ")

    stack = Stack()

    for char in input_str:
        stack.add(char)

    while stack.top is not None:
        print(stack.peek(), end='')
        stack.remove_data()
