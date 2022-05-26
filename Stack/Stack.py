class stack(object):
    def __init__(self):
        self.item=[]
    
    def push(self,item=''):
        pass
        self.item.append(item)

    def New_pop(self):
        '''
        This will pop the last element 
        and also give you back the element
        and as well as the new list
        '''
        self.item.pop()
        pass

    def peek(self):
        if self.item:
            '''
            if the condition gets true only then 
            it will give back the element 
            '''
            return self.item[-1]
        else:
            ''' 
            That means that the stack was empty 
            '''
            return None

    def SizeOfStack(self):
        if self.item:
            size=len(self.item)
            return size 
        else:
            return None 

    def IsEmpty(self):
        if self.item==[]:
            return True
        else:
            return False

if __name__== "__main__":
    stack=stack()
    stack.push("10")
    stack.push("20")
    stack.push("30")
    stack.push("40")
    stack.push("50")
    print(stack.SizeOfStack())
    stack.New_pop()
    # print(Temp)
    print(stack.IsEmpty())
    print(stack.peek())
