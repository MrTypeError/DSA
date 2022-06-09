def SumOfNaturalNumber(limit):
    num=limit
    if limit==0 or limit==1:
        return 1
    else:
        return num+SumOfNaturalNumber(limit-1)

#function call
print("The number should be (+)ve")
#checking the number is greater then zero
inp=int(input("Enter the a Number :",end=''  ))
if (inp<0):
    print("Enter a Valid number")
else:
    print(SumOfNaturalNumber(inp))
