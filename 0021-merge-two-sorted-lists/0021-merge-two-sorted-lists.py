# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def mergeTwoLists(self, list1, list2):

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # create a dummy node as the head of the merged list
        dummy = ListNode()
        # create a pointer to the current node of the merged list
        curr = dummy

        while list1 and list2: 
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        # return the next node of the dummy node as the head of the merged list
        return dummy.next

            
    
        