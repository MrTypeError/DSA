class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self) -> str:
        return f"Node {self.data} {self.next}"

def Print_LL(head):
    while(head):
        print(head.data)
        head=head.next

def Count_LL(head,count=0):
    while head:
        count+=1
        head=head.next
    print(f"The Count Of Nodes in LL is {count}")


def Inseart_Node_End(head,data):
    if not head:
        return Node(data)
    ptr= head
    while ptr.next:
        ptr= ptr.next
    ptr.next= Node(data)
    return head

def Inseart_Node_First(head, data ):
    temp=Node(data)
    temp.next=head
    return temp

    # This same function can be written in One line 
    
    # return Node(data , head) 




# a=Node(1)
# print(a)

# b= Node(2)
# print(b)

# a.next = b
# print(a.data)

# c= Node(3)
# b.next= c

##############################
#          OR
##############################


# a=Node(1)
# a.next=Node(2)
# a.next.next=Node(3)
# a.next.next.next=Node(4)


##############################
#           OR
##############################

a=Node(1,Node(2,Node(3,Node(4))))

# print(a)
# Print_LL(a)
# Count_LL(a)
Inseart_Node_End(a,100)
Print_LL(a)
Count_LL(a)


