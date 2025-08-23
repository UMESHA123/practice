class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def VerticalTraversal(root, index, res):
    if root is None:
        return 
    if index not in res:
        res[index] = [root.key]
    else:
        res = res[index].append(root.key)
    VerticalTraversal(root.left, index-1, res)
    VerticalTraversal(root.right, index+1, res)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(70)
root.right.right.left = Node(80)
root.right.right.right = Node(90)

res = {}

VerticalTraversal(root, 0, res)
print(res)