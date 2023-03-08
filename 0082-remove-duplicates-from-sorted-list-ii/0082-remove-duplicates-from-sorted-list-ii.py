# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):

        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode()
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.next.val == curr.val:
                while curr.next and curr.next.val == curr.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return dummy.next

        
        