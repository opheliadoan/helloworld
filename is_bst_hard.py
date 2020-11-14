#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(2*10**9)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def IsBinarySearchTreeHelper(tree, i):
    left = tree[i][1]
    right = tree[i][2]
    if left != -1:
        if tree[left][0] >= tree[i][0]:
            return False
        return IsBinarySearchTreeHelper(tree, left)
    if right != -1:
        if tree[right][0] < tree[i][0]:
            return False
        return IsBinarySearchTreeHelper(tree, right)
    return True


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if len(tree) == 0:
        return True
    return IsBinarySearchTreeHelper(tree, 0)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
