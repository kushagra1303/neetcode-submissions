
class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev

        # Step 3: Merge the two halves alternately
        first = head

        while second is not None:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
