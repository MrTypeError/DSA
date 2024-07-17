# # Palindrome By Basic Logic 

# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")



# Palindrome Cheat Code 

def PalindromeMaker(n):
    newStr = str(n)
    revStr = newStr[::-1]

    if newStr == revStr:
        return True 
    else :
        return False 

n=int(input("Enter number:"))    
answer = PalindromeMaker(n)
if answer == True:
    print(f"The No. {n} Palindrome")
else:
   print( f"The No. {n} is not a Palindrome" )


