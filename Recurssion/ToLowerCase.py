# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
TempStr=''
def ToLower(pos,word):
    if pos==len(word)+1:
        return -1
    else:
        if(word[pos]).isupper():
            TempStr+=word[pos].lower()    
        ToLower()

