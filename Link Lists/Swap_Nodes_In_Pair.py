def solve(head):
    if not head or not head.next :
        return head
    p1 =head
    p2 = head.next
    x = p2.next
    p2.next = p1
    #or 
    #head.next.next =head
    p1.next = solve(x)
    #or 
    #head.next = solve(x)
    return p2





# Input :            

# A B C D E F 

# Output :

# B A D C F E




# Input :            

# A B C D E  

# Output :

# B A D C E