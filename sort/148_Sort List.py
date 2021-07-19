'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    #method 3. Bottom up mergeSort. O(nlogn), S(1)
    import math
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: return head
        
        n = self.countSize(head)
        m = int(math.log(n - 1, 2)) + 1
        
        
        dummy = ListNode('#', head)
        for i in range(1, m + 1):
            tail_prev = dummy
            head = dummy.next
            new_head = head
            while new_head:
                size_const = 2 ** i
                size = size_const
                while size > 0:
                    if new_head:
                        tail_curr = new_head
                        new_head = new_head.next
                        size -= 1
                    else:
                        break
                tail_curr.next = None
                part1, part2 = self.splitList(head, size_const)
                old_head, tail = self.mergeList(part1, part2)
                tail_prev.next = old_head
                tail_prev = tail
                head = new_head
        return dummy.next
                    
                    
                
    def splitList(self, head, size):
        if not head: return None, None
        mid = head
        size = size // 2
        while size - 1 > 0:
            if mid:
                mid = mid.next
                size -= 1
            else:
                break
        if mid:
            part2 = mid.next
            mid.next = None
            part1 = head
        else:
            part1 = head
            part2 = None
        return part1, part2
        
        
    def countSize(self, head):
        if not head: return 0
        count = 0
        while head:
            count += 1
            head = head.next
        return count
        
    
    def mergeList(self, l1, l2):
        dummy = ListNode('#', None)
        node = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                node = l1
                l1 = l1.next
            else:
                node.next = l2
                node = l2
                l2 = l2.next
        if l1:
            node.next = l1
            tail = l1
            while tail.next:
                tail = tail.next             
        elif l2:
            node.next = l2
            tail = l2
            while tail.next:
                tail = tail.next
        return dummy.next, tail    
    
    
    '''
    #method 2. Top down MergeSort. O(nlogn), S(logn)
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: 
            return head
        
        mid = self.findMid(head)
        mid_next = mid.next
        mid.next = None
        return self.mergeList(self.sortList(head), self.sortList(mid_next))

    def findMid(self, head):
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def mergeList(self, l1, l2):
        dummy = ListNode('#', None)
        node = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                node = l1
                l1 = l1.next
            else:
                node.next = l2
                node = l2
                l2 = l2.next
        if l1:
            node.next = l1
        elif l2:
            node.next = l2
        return dummy.next
    '''        
    
    
    '''
    #method 1. Naive brute force. exchange nodes. O(n^2). S(1)
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return head
        node1 = head
        dummy = ListNode('#', node1)
        node1_prev = dummy
        while node1:
            node2 = node1.next
            node2_prev = node1
            while node2:
                if node1.val > node2.val:
                    self.exchangeNodes(node1, node2, node1_prev, node2_prev)
                    node1, node2 = node2, node1
                    node2_prev = node2
                    node2 = node2.next
                else:
                    node2_prev = node2
                    node2 = node2.next
                #print(node2_prev.val)
            node1_prev = node1
            node1 = node1.next
        return dummy.next
            
            
            
            
    def exchangeNodes(self, node1, node2, node1_prev, node2_prev):
        if node1.next == node2:
            node2_next = node2.next
            
            node1_prev.next = node2
            node2.next = node1
            node1.next = node2_next
            return
        
        node1_next = node1.next
        node2_next = node2.next
        
        node2.next = node1_next
        node1.next = node2_next
        node2_prev.next = node1
        node1_prev.next = node2
        
        return
    '''
