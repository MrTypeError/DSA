a=[1,0,1,0,1,1,0,0,0,1,1,0,1]
b=[bool(i) for i in a]

#making boolian list
print(b)

#It will return True if all the values are True 
print(all(a))

#It will return True if any one of the value is True
print(any(a))