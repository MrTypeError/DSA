class Queue:
    def __init__(self) -> None:
        self.arr1=[]
        self.arr2=[]
    
def Enqueue(self,data):
    for i in range (len(self.arr1)):
        item=self.arr1.pop()
        self.arr2.append(item)
    self.arr1.append()
    for i in range (len(self.arr2)):
         item=self.arr2.pop()
         self.arr1.append(item)

def Dqueue(self): #ghgh
    if len(self.arr1) == 0:
        print("Under Flow")
    else:
        return self.arr1.pop()

def Showqueue(self):
    if len(arr1)==0:
        print("There Are No Element to show ")
    elif len(self.arr1):
        print("There is only one Element : ",self.arr1)
    else:
        return [i for in in self.arr1[::-1]]
        
        
