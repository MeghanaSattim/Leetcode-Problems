# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        before =dummy
        for _ in range(left-1):
            before=before.next
        curr=before.next
        for _ in range(right-left):
            next_node=curr.next

            curr.next=next_node.next
            next_node.next=before.next
            before.next=next_node
        return dummy.next
        