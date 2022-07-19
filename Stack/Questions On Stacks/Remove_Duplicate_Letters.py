def solve(s):
    last={}
    #map is ready
    for i , el in enumerate(s):
        last[el]=i
    #stack is created
    st=[]
    #creating a set
    peresent = set()

    #for index, element in s
    # This will traverse 
    for i,e in enumerate(s):
        if e in peresent:
            continue 
        #This will check the conditions and remove the elements from the map
        while st and st[-1]>e and last[st[-1]]>i:
            temp=st.pop()
            peresent.remove(temp)
        #append elements in the stack
        st.append(e)
        #add elements in the set       
        peresent.add(e)

    return "".join(st)


