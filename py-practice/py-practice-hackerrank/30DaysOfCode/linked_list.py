# Day 15: Linked List - https://www.hackerrank.com/challenges/30-linked-list


class Node:
    '''Create a node'''

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        current = head
        if not current:
            newNode = Node(data)
            return newNode
        current.next = Solution.insert(self, current.next, data)
        return current

'''mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head)'''
