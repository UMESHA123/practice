class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def KthNode(root, level, k):
    if root is None:
        return level
    if level == k:
        print(root.key)
        return level
    
    return max(KthNode(root.left, level+1, k), KthNode(root.right, level+1, k))

def KthNode1(root, k):
    if root is None:
        return 0
    if k == 0:
        print(root.key)
        
    return max(KthNode1(root.left, k-1), KthNode1(root.right, k-1))+1

def KthNode2(root, k):
    if root is None:
        return 
    if k == 0:
        print(root.key, end=" ")
    
    KthNode2(root.left, k-1)
    KthNode2(root.right, k-1)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(70)

res = KthNode(root, 0, 2)
print(res)
res1 = KthNode1(root, 2)

print()
KthNode2(root, 2)
print()

#           10
#       20        30
#   40      50         70
#
#
#
#