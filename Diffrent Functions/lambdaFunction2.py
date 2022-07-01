def f(p):
    return p[1]
def e(p):
    return len(p)
a=[
    [1,3],
    [4,7],
    [-1,8],
    [3,5],
    [2,1]
]
'''
    This will work in regard to first
    index of the character/intiger present
'''
x=sorted(a) # As noting is passed as comperator,
print(x)    # so it will sort on the basis of the normal index( p[0]) element


'''
    In this case we are passing a comperator,
    which will compare and give the output
    on the basis of comperission of ,
    kepping the comperission condition in mind
'''

y=sorted(a,key=f) #This sorting will be done w.r.t key=f
                  #This will go to the function and 
                  #sort the elements with respect to the index p[1] Elementk
print(y)

b=[
    "axc",
    "deff",
    "xy",
    "sdsadsad"
]

m=sorted(a)
print(m)
n=sorted(a,key=e)
print(n)