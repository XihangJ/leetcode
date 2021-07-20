'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #method1. using slo and fast pointers find common node as tail, delete tail -> tail.next
    #calculate len1 and len2, find the first common node. set tail -> tail.next 
    #O(n), S(1)
    def detectCycle(self, head: ListNode) -> ListNode:
        node1 = head
        node2 = head
        count1 = 1
        flag = True
        while node1 and node2.next and flag:
            node1 = node1.next
            node2 = node2.next.next
            count1 += 1
            if node1 and node2 and node1 == node2:
                tail = node1
                flag = False
                break
            elif (not node2) or (not node2.next):
                return None
        if flag: return
        if tail == head: return head
        
        tail_next = tail.next
        tail.next = None
        node = tail_next
        count2 = 1
        while node.next:
            node = node.next
            count2 += 1
        
        
        tail.next = tail_next
        tmp_node1 = head
        tmp_node2 = tail_next
        if count1 > count2:
            for i in range(count1 - count2):
                tmp_node1 = tmp_node1.next
        elif count2 > count1:
            for i in range(count2 - count1):
                tmp_node2 = tmp_node2.next 
        
        while tmp_node1:
            if tmp_node1 and tmp_node2 and tmp_node1 == tmp_node2:
                return tmp_node1
            tmp_node1 = tmp_node1.next
            tmp_node2 = tmp_node2.next
        
