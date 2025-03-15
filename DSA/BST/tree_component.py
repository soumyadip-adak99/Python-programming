class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Build_tree:
    def __init__(self):
        self.idx = -1

    def build_tree(self, nodes):
        self.idx += 1

        if self.idx >= len(nodes) or nodes[self.idx] == -1:
            return None

        new_node = Node(nodes[self.idx])
        new_node.left = self.build_tree(nodes)
        new_node.right = self.build_tree(nodes)

        return new_node
