# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # create a dummy node as the head of the modified linked list
        New = ListNode()
        # set a pointer to the dummy node
        dummy = New

        # loop through the given list
        while head:
            # if the value in that node is not equal to the val
            if head.val != val:
                # create a new node for that value
                addNode = ListNode(head.val)
                # append the node to the new list
                dummy.next = addNode
                # Move to the next of the new node you appended
                dummy = dummy.next

            # go to the next node in the list
            head = head.next
            
        # return the next node of the new list sice the first on is zero
        return New.next