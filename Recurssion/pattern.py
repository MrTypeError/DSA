# 1
# 22
# 333
# 4444
# 55555

def pattern(n):
    if n==0:
        return
    else:
        pattern(n-1)
        print(str(n)*n)

pattern(5)

#---------------------------------
#---------------------------------
#---------------------------------


# 55555
# 4444
# 333
# 22
# 1


