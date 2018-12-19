"""
Task 
A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom.
 You are given a pointer, root, pointing to the root of a binary search tree. 
Complete the levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.

Hint: You'll find a queue helpful in completing this challenge.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a BST: 
The first line contains an integer,  T(the number of test cases). 
The T subsequent lines each contain an integer, data, denoting the value of an element that must be added to the BST.

Output Format

Print the data value of each node in the tree's level-order traversal as a single line of N space-separated integers.
"""

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def InOrder(self,root):
        #Write your code here
        if root:
            self.levelOrder(root.left)
            print(root.data, end =" ")
            self.levelOrder(root.right)

    def PreOrder(self,root):
        #Write your code here
        if root:
            print(root.data, end =" ")
            self.levelOrder(root.left)
            self.levelOrder(root.right)

    def PostOrder(self,root):
        #Write your code here
        if root:
            self.levelOrder(root.left)
            self.levelOrder(root.right)
            print(root.data, end =" ")

    def levelOrder(self,root):
        #Write your code here
        if root:
            q = [root]
            while len(q):
                tree = q[-1]
                q.pop()
                print(tree.data, end=" ")
                if tree.left:
                    q.insert(0,tree.left)
                if tree.right:
                    q.insert(0,tree.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
myTree.InOrder(root)
myTree.PreOrder(root)
myTree.PostOrder(root)
