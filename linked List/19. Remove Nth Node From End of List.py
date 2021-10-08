'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #method 2. 1 pass scan. Using 2 pointers
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return
        dummy = ListNode('#', head)
        # step 1. set fast
        fast = dummy
        for _ in range(n): fast = fast.next
        # step 2. move fast and slow till the end.
        slow = dummy
        while fast.next:
            fast = fast.next
            slow = slow.next
        # delete nth node from the end
        slow.next = slow.next.next
        return dummy.next
    
    
    
    '''
    #method 1. 2 pass scan
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return
        # step 1. get the total length of the SLL
        count = 1
        curr = head
        while curr:
            if curr.next: count += 1
            curr = curr.next
        # Step 2. get the nth node from the end
        path_togo = count - n
        #set a dummy head
        dummy = ListNode('#', head)
        node = dummy
        for _ in range(path_togo):
            node = node.next
        node.next = node.next.next
        return dummy.next
    '''
