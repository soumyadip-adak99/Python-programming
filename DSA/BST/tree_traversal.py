from collections import deque
import tree_component


def inorder(root):  # inorder traversal
    if root is None:
        return

    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


def preorder(root):  # preorder
    if root is None:
        return

    print(f"{root.value}", end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):  # post order
    if root is None:
        return

    postorder(root.left)
    preorder(root.right)
    print(root.value, end=" ")


def levelorder(root):  # lavel order traversal
    if root is None:
        return

    queue = deque([root])
    queue.append(None)

    while queue:
        current_node = queue.popleft()

        if current_node is None:
            print()
            if not queue:
                break
            else:
                queue.append(None)
        else:
            print(current_node.value, end=" ")

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


def level_order_traversal(root):  # lavel order traversal another logic
    result = []

    if root is None:
        return result

    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_lavel = []

        for _ in range(level_size):
            current_node = queue.popleft()

            if current_node:
                current_lavel.append(current_node.value)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)
        result.append(current_lavel)

    return result


if __name__ == "__main__":
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    tree = tree_component.Build_tree()
    root = tree.build_tree(nodes)
    print(level_order_traversal(root))
