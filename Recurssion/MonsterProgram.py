# f="MimiiDutta"
# m="SudipDutta"
# c="MSiumdiiipDDuuttttaa"
# Normal Implimentation :-
# female=''
# male=''
# for i in range(len(c)):
#     if i%2==0:
#         female+=c[i]
#     else:
#         male+=c[i]
# print(female)
# print(male)


#this is the Recursive Implimentation :-
c="MSiumdiiipDDuuttttaa"
# m="MimiiDutta"
# f="SudipDutta"
def traverse(c,pos,size,female='',male=''):
    if pos==size+1:
        return -1 #terminating condition for the recurssion
    else:
        if(pos%2==0): #this condtion will chech the postion is even ot not 
            male+=c[pos] #adding the female name
        else:
            female+=c[pos] #adding the male name 
    traverse(c,pos+1,size) #This is the recursive call for the traversal of the string
   



traverse(c,0,len(c)-1)