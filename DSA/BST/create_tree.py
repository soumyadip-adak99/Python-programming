import tree_component

if __name__ == "__main__":
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    tree = tree_component.Build_tree()
    root = tree.build_tree(nodes)
    print(root.value)
