# args - arguments 
# kwargs- Keyword Argyments returns dict types


# def func(*args,**kwargs):
#Unamed arguments will be taken by *x
# print(args)
# #named arguments will be taken by *y
# print(kwargs)

# func(1,2,4,2,1,21,33,23,h=1,m=221,q=34)




def func(a,b,*x,**y):
    print(a)
    print(b)
    print(x)
    print(y)


func(1,2,4,2,1,21,33,23,h=1,m=221,q=34)