
class Solution:
    def detectCycle(self, head):
        slow , fast = head ,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow :
                fast = head
                break
        if fast and fast.next:
            while fast != slow :
                fast =fast.next
                slow = slow.next
            return fast
        return None
            