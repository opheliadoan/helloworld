# python3

import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrderHelper(self, i):
        if self.left[i] != -1:
            self.inOrderHelper(self.left[i])
        self.result.append(self.key[i])
        if self.right[i] != -1:
            self.inOrderHelper(self.right[i])

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.inOrderHelper(0)
        return self.result

    def preOrderHelper(self, i):
        self.result.append(self.key[i])
        if self.left[i] != -1:
            self.preOrderHelper(self.left[i])
        if self.right[i] != -1:
            self.preOrderHelper(self.right[i])

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.preOrderHelper(0)
        return self.result

    def postOrderHelper(self, i):
        if self.left[i] != -1:
            self.postOrderHelper(self.left[i])
        if self.right[i] != -1:
            self.postOrderHelper(self.right[i])
        self.result.append(self.key[i])

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.postOrderHelper(0)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
