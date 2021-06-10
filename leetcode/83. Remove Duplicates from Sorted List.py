# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        sorted_array = sorted(list(set(array)))

        answer = ListNode(0)
        result = answer
        for i in sorted_array:
            answer.next = ListNode(i)
            answer = answer.next
        return result.next
