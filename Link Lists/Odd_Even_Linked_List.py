def solve(head):
    if not head or not head.next or not head.next.next:
        return head 
    o = head 
    e = head.next
    while e and e.next :
        x = e.next
        e.next = e.next.next
        x.next = o.next
        o.next = x
        o = o.next
        e = e.next
    return head






# Input :
#     LinkedList : 1 2 3 4
# Output : 
#     1 3 2 4 