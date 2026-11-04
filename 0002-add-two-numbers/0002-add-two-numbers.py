# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        res = ListNode(0)
        val = res
        carry = 0
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            total = n1 + n2 + carry
            carry = total // 10
            digit = total % 10

            val.next = ListNode(digit)
            val = val.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return res.next