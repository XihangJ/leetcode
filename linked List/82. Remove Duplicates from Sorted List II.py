'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        dummy = ListNode('#', head)
        prev = dummy
        left, right = head, head.next
        while right:
            if left.val == right.val:
                while right and left.val == right.val:
                    right = right.next
                prev.next = right
                left = prev.next
                if left: right = left.next
            else:
                prev = left
                left = right
                right = right.next
        return dummy.next
