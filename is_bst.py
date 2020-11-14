#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(2*10**9)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def IsBinarySearchTreeHelper(tree, result, i):
    left = tree[i][1]
    right = tree[i][2]
    if left != -1:
        IsBinarySearchTreeHelper(tree, result, left)
    result.append(tree[i][0])
    if right != -1:
        IsBinarySearchTreeHelper(tree, result, right)


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    inorder = []
    if len(tree) == 0:
        return True
    IsBinarySearchTreeHelper(tree, inorder, 0)
    return (inorder == sorted(inorder))


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
