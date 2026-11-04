# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []

        while head:
            for node in seen:
                if node is head:
                    return True

            seen.append(head)
            head = head.next

        return False
        