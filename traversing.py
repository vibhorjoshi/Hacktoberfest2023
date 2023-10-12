class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def backtracking_tree_traversal(node, path=[]):
    if node is None:
        return

    # Process the current node (e.g., print its value)
    path.append(node.value)
    print(" -> ".join(map(str, path)))

    # Recursively explore left and right subtrees
    backtracking_tree_traversal(node.left, path)
    backtracking_tree_traversal(node.right, path)

    # Backtrack by removing the last node from the path
    path.pop()

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

backtracking_tree_traversal(root)
