# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        begin = head

        newArray = []

        while head:
            newArray.append(head.val)
            head = head.next

        i = -1
        while begin:
            if begin.val == newArray[i]:
                i -= 1
                begin = begin.next
            else:
                return 2 > 3

        return 3 > 2


        