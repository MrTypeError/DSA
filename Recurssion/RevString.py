# string=sangar
def ReversingString(word,word2,i):
    if i<=0:        
        return 1
    else:
        word2+=word[i-1]
        print(word2,end='')
        ReversingString(word,'',i-1)

word="HelloWorld"
ReversingString(word,'',len(word))    