def factroial(num):
    if num==1 or num==1:
        return 1
    else:
        # Recursive call is going on and retuning the value
        return num*factroial(num-1)


#function call
print("The number should be (+)ve")
#checking the number is greater then zero
inp=int(input("Enter the a Number :",end=''  ))
if (inp<0):
    print("Enter a Valid number")
else:
    print(factroial(inp))
