class Node():
    def __init__(self , data ,next) -> None:
        self.data=data
        self.next=next

def solve(l1, l2 ):
    carry = 0 
    ans = p = Node(1234254)

    while l1 or l2 :
        l1data,l2data = l1.data if l1 else 0 , l2.data if l2 else 0
        additon = l1data+l2data+carry
        carry = additon//10
        num = additon%10
        p.next = Node(num)
        p, l1, l2 = p.next , l1.next if l1 else l1 , l2.next if l2 else l2
    if carry:
        p.next= Node(carry)
    return ans



