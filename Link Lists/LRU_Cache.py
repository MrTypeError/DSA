class DLL():
    def __init__(self , key = 0 ,value = 0) -> None:
        self.key=key
        self.value=value 
        self.previous=self.next=None

def delete(node):
    node.next.previous = node.previous 
    node.previous.next = node.next

def inseart_x_left_to_y(x,y):
    x.previous = y.previous 
    x.next = y
    y.previous = x.previous.next  = x

class LRUCache():
    def __init__(self , capacity) -> None:
        self.capacity = capacity
        self.m = {}
        self.previous_Dummy = DLL()
        self.next_Dummy = DLL()
        self.previous_Dummy.next = self.next_Dummy
        self.next_Dummy.previous = self.previous_Dummy

    def get(self,key):
        if key not in self.m:
            return -1
        node = self.m[key]
        delete(node)
        inseart_x_left_to_y(node ,self.next_Dummy)
        return node.value 

    def put(self,key , value ):
        if key in self.m:
            node = self.m[key]
            node.value = value
            delete(node)
        else:
            node = DLL(key , value )
            self.m[key] = node
        inseart_x_left_to_y(node , self.next_Dummy)

        if len(self.m)>len(self.capacity):
            k = self.previous_Dummy.next.key
            delete(self.previous_Dummy.next)
            del(self.m[k])
