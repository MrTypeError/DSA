a=[1,3,4,5,6,67,8,]
b=[1,3,5,5,56,78,78,768,73]
c=[3,4,5,6,7,8,9,99,65,34,5,24]
for x,y,z in zip(a,b,c):
    #this function will make pair 
    '''
    It returns corrosping elements of diffrent lists
    If no corrosponding element is found,
    it will not make pair
    returning type is tuple
    '''
    print(x,y,z) 
