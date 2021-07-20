'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #method 1. get the size of A and B. find their first common node.
    #O(m + n), S(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        sizeA = self.getSize(headA)
        sizeB = self.getSize(headB)
        if sizeA > sizeB:
            for i in range(sizeA - sizeB):
                headA = headA.next
        elif sizeA < sizeB:
            for i in range(sizeB - sizeA):
                headB = headB.next
                
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return
        
        
    def getSize(self, head):
        if not head: return 0
        count = 1
        node = head
        while node.next:
            count += 1
            node = node.next
        return count
