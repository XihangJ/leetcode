'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        
        node = head
        head2 = head.next
        isOdd = True
        while node and node.next:
            node_next_next = node.next.next
            node_next = node.next
            
            if not node_next_next and isOdd:
                node.next = head2
            else:
                node.next = node_next_next
            
            node = node_next
            isOdd = not isOdd
        if isOdd:
            node.next = head2
        return head
