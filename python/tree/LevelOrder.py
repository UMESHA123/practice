from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def LevelOrder(root):
    if root is None:
        return 
    
    nodes = deque()
    nodes.append(root)
    
    while len(nodes) != 0:
        node = nodes.popleft()
        print(node.key)
        if node.left != None:
            nodes.append(node.left)
        if node.right != None:
            nodes.append(node.right)
        

def Level1(root):
    if root is None:
        return -1
    
    q = deque()
    q.append(root)
    q.append(None)
    while len(q) > 1:
        cur = q.popleft()
        if cur is None:
            print()
            q.append(None)
            continue
        print(cur.key, end = " ")
        if cur.left is not None:
            q.append(cur.left)
        if cur.right is not None:
            q.append(cur.right)


def Level2(root):
    if root is None:
        return
    q = deque()
    q.append(root)

    while len(q)>0:
        count = len(q)
        for i in range(count):
            cur = q.popleft()
            print(cur.key, end = " ")
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        print()

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(70)
root.left.right.right = Node(80)
root.right.right = Node(60)

LevelOrder(root)
print()
Level1(root)
print()
print()
Level2(root)
print()