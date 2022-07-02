# sample list 
# list=[10,203,405,3,234,53,3,4,425,2,351,53,532,5,235,3215,32,5325]

def LinearSearch(array,input):
    for i in range(len(array)):
        if input==array[i]:
            return True,i,array[i]
        else:
            return False

arr=[10,203,405,3,234,53,3,4,425,2,351,53,532,5,235,3215,32,5325]

''' the function is called and 
    the number to searched 
    is also passed as a input'''

temp=LinearSearch(arr,10)
print("Found Or Not,Index,Element : ",temp)