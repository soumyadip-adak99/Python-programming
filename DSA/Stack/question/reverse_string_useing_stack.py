import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Stack.implementation.Stack import Stack

from Stack.implementation.Stack import Stack

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)

    stack.display()
