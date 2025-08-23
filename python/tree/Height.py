class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
def height(root, level):
    if root is None:
        return level
    return max(height(root.left, level + 1), height(root.right, level + 1))

def height2(root):
    if root == None:
        return 0
    return max(height2(root.left), height2(root.right))+1

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(70)
root.left.right.right = Node(80)
root.right.right = Node(60)

res = height(root, 0)
print(res)

res2 = height2(root)
print(res2)