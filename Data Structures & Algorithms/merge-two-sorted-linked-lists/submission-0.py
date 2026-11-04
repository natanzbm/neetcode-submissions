# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        while list1:
            nodes.append(list1)
            list1 = list1.next

        while list2:
            nodes.append(list2)
            list2 = list2.next

        nodes.sort(key=lambda node: node.val)

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        if nodes:
            nodes[-1].next = None
            return nodes[0]

        return None
        