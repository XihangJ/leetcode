'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        dummy = ListNode('$', head)
        prev = dummy
        while head:
            head_next = head.next
            if head.val == val:
                prev.next = head_next
                head = head_next
            else:
                prev = head
                head = head_next
            
        return dummy.next
