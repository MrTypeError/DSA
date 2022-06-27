# string2="APPLE"
# String="REFER"
def IsPalindrome(word,r=0,l=0):
    if l>=r:
        return True
    else:
        if word[l]==word[r]:
            return IsPalindrome(word,r-1,l+1)
        else:
            return False

word="REFER"
answer=IsPalindrome(word,len(word),0)

if answer==True:
    print("Its Palindrome")
else:
    print("Its not a palindrome")


        
        

