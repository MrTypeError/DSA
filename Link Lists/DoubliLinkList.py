class Node():
    def __init__(self,data=None,next=None,previous=None) -> None:
        self.next=next
        self.data=data
        self.previous=previous


class LinkList(self):
    def __init__(self) -> None:
        self.head=Node("Head")


def NewAdd(self,data):
    if self.head==None:
        node=Node(data)
        self.head=node
    else:
        node=Node(data)
        self.head.previous=node 
        self.next=self.head
        self.head=node

def Del(self,data):
    temp=self.head
    if temp.next==None:
        if temp.data==data:
            temp.next.previous=None
            self.head=temp.next
            temp.next=None
        else:
            while temp.next == None:
                if temp.data==data:
                    break
                temp=temp.next
                if temp.next:
                    temp.previous.next=temp.next
                    temp.next.previous=temp.previous 
                    temp.next=None
                    temp.previous=None
                else:
                    temp.previous.next=None
                    temp.previous=None
                return
        
