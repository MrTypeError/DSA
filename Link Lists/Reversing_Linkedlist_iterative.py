class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def solve(head):
    if not head or not head.next:
        return head
    p,c,n=head,head.next,head.next.next
    head.next=None
    while n:
        c.next=p
        p=c 
        c=n
        n=n.next
    c.next=p
    return c

a=Node(1,Node(2,Node(3,Node(4))))
print(a)

a=solve(a)
print(a)