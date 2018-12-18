"""
Objective 
Today, we're working with Binary Search Trees (BSTs). Check out the Tutorial tab for learning materials and an instructional video!

Task 
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. 
You are given a pointer, 'root', pointing to the root of a binary search tree. 
Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a binary search tree: 
The first line contains an integer, n, denoting the number of nodes in the tree. 
Each of the n subsequent lines contains an integer, data, denoting the value of an element that must be added to the BST.
"""

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

    def getHeight(self,root):
        #Write your code here
        lcount = 0
        rcount = 0
        if root.left:
            lcount += 1 + self.getHeight(root.left)
        if root.right:
            rcount += 1 + self.getHeight(root.right)

        if lcount > rcount:
            return lcount
        elif lcount < rcount:
            return rcount
        else:
            return 0

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
