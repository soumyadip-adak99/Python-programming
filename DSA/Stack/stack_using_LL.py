class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack_Link_list:
    top = None

    @staticmethod
    def push(data):
        new_node = Node(data)
        new_node.next = stack_Link_list.top
        stack_Link_list.top = new_node

    @staticmethod
    def pop():
        if stack_Link_list.top is Node:
            print("This stack is empty.")
            return -1

        pop_value = stack_Link_list.top.data
        stack_Link_list.top = stack_Link_list.top.next

        return pop_value

    @staticmethod
    def peek():
        if stack_Link_list.top is Node:
            print("This stack is empty.")
            return -1

        return stack_Link_list.top.data

    @staticmethod
    def display():
        if stack_Link_list.top is None:
            print("Stack is empty.")
            return

        current_node = stack_Link_list.top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        print()


if __name__ == "__main__":
    stack_Link_list.push(10)
    stack_Link_list.push(20)
    stack_Link_list.push(30)
    stack_Link_list.push(40)

    print(f"Pop-> {stack_Link_list.pop()}")
    print(f"Peek-> {stack_Link_list.peek()}")

    print("Display->")
    stack_Link_list.display()
