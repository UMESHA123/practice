class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1

def CheckBalancedTree(root):
    if root is None:
        return True
    return abs(height(root.left)-height(root.right))<=1 and CheckBalancedTree(root.left) and CheckBalancedTree(root.right)

def CheckBalancedTree1(root):
    if root is None:
        return 0
    left = CheckBalancedTree1(root.left)
    if left == -1:
        return -1
    right = CheckBalancedTree1(root.right)
    if right == -1:
        return -1
    if abs(left-right)>1:
        return -1
    return max(left, right)+1

root = Node(3)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(5)
root.left.right = Node(9)
root.right.right = Node(7)
root.right.right.left = Node(6)

res = CheckBalancedTree(root)
if res:
    print("Yes")
else:
    print("No")

r = CheckBalancedTree1(root)
if r == -1:
    print("No")
else:
    print("Yes")