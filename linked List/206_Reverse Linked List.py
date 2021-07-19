#Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        #method 3. store and create
        if not head or not head.next:
            return head
        temp_list = []
        node = head
        while node:
            temp_list.append(node.val)
            node = node.next
        new_head = ListNode(temp_list.pop(), None)
        new_node = new_head
        while temp_list:
            new_node.next = ListNode(temp_list.pop(), None)
            new_node = new_node.next
        return new_head
        '''
        
        #2. Recursion
        if (not head) or (not head.next):
            return head
        
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return node
        
        
        '''
        #method 1. iterative
        if not head:
            return head
        node = head
        prev = None
        while node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
        return prev
        '''    
