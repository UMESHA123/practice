class MyMinHeap:
    def __init__(self):
        self.arr = []
    def parent(self, i):
        return (i-1)//2
    