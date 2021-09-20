# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow, fast = head, head
        
        for x in range(n):
            fast = fast.next
            
        if fast == None:
            return head.next
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head