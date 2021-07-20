'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    #method 1. slow and fast pointers
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        node1 = head
        node2 = head
        while node1 and node2.next:
            node1 = node1.next
            node2 = node2.next.next
            if node1 and node2 and node1 == node2:
                return True
            elif not node2:
                return False
        return False
