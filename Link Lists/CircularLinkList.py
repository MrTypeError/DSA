class Node():
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class CircularLinkList(self):
    def __init__(self):
        self.head=None
    
    def PushInLL(self,data):
        pass
    def DelInLL(self):
        pass
    def ShowInLL(self):
        temp=self.head
        if temp is not None:
            while(True):
                print(temp.data, end=" ")
                temp=temp.next
                if temp==self.head:
                    break
                

        