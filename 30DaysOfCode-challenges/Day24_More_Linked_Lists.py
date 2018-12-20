"""
A Node class is provided for you in the editor. A Node object has an integer data field, 'data', 
and a Node instance pointer, 'next', pointing to another node (i.e.: the next node in a list).

A removeDuplicates function is declared in your editor, which takes a pointer to the 'head' node of a linked list as a parameter. 
Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.

Note: The 'head' pointer may be null, indicating that the list is empty. Be sure to reset your 'next' pointer when performing deletions to avoid breaking the list.
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        lists = []
        while head:
            if head.data not in lists:
                lists.append(head.data)
            head = head.next
        head=None
        for i in lists:
            head=self.insert(head,i)

        return head
        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
