class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)

