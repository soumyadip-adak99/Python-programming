class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.__top = None

    def __isEmpty(self) -> bool:
        return self.__top is None

    def push(self, data):
        new_node = _Node(data)
        new_node.next = self.__top
        self.__top = new_node

    def pop(self):
        if self.__isEmpty():
            print("Stack is empty.")
            return

        popData = self.__top.data
        self.__top = self.__top.next
        return popData

    def peek(self):
        if self.__isEmpty():
            print("Stack is empty.")
            return

        return self.__top.data

    def display(self):
        if self.__isEmpty():
            print("Stack is empty.")
            return

        current_node = self.__top
        while current_node is not None:
            print(f"{current_node.data}", end=" ")
            current_node = current_node.next
        print()
