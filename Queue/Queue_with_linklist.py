from itertools import count


class Node():

    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class Queue():
    def __init__(self) -> None:
        self.first=None
        self.last=None
        self.count=0

def Enqueue(self,data):
    
    New_Node=Node(data)
    if self.last==None:
        self.last=New_Node
        self.first=self.last
        self.count+=1
        return
    else:
        self.last.next=New_Node
        self.last=New_Node
        self.count+=1

def DeQueue(self):
    if self.first == self.last:
        self.last=None
        self.count-=1

    elif self.last==None:
        print("Nothing To Print")
    else:
        self.first=self.first.next
        self.count-=1
def PeekInQueue(self):
    return self.first.data


