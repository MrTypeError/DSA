from ast import While


class Node():
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class CircularLinkList(self):
    def __init__(self):
        self.head=None
    
    def PushInLL(self,data):
        RealNode=Node(Data)
        temp=self.head
        if temp.next != None:
            while(temp.next != self.head):
                temp=temp.next
            temp.next=RealNode
        else:
            RealNode.next=RealNode
    def ShowInLL(self):
        temp=self.head
        if temp is not None:
            while(True):
                print(temp.data, end=" ")
                temp=temp.next
                if temp==self.head:
                    break
ObjectForLL=CircularLinkList()

ObjectForLL.PushInLL(201)
ObjectForLL.PushInLL(204)
ObjectForLL.PushInLL(112)
ObjectForLL.PushInLL(300)
ObjectForLL.PushInLL(101)
print("You Have Pushed Some Elements " )
print("Those are given below : ")
ShowingInfo=ObjectForLL.ShowInLL()
print(ShowingInfo)

