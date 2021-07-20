'''
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        #method 1. iterative
        if left == right:
            return head
        node = ListNode(None, head)
        head_dummy = node
        for i in range(right):
            prev = node
            node = node.next
            if i + 1 == left:
                sub_head = node
                sub_prev = prev
        sub_tail = node
        sub_tail_next = sub_tail.next
        sub_tail.next = None
        p, tail = self._reverseList(sub_head)
        tail.next = sub_tail_next
        sub_prev.next = p
        return head_dummy.next
        
        
    def _reverseList(self, head):
        if not head:
            return head
        node = head
        prev = None
        while node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
        return prev, head
