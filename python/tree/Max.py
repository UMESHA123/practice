class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def Max(root):
    if root is None:
        return -1
    return max(root.key, Max(root.left), Max(root.right))

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(70)
root.left.right.right = Node(80)
root.right.right = Node(60)

res = Max(root)
print(res)