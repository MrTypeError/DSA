def Fibo(num):
    if num==0 or num==1:
        return num
    f1=Fibo(num-1)
    f2=Fibo(num-2)
    ans=f1+f2
    return ans

# value=Fibo(100)
value=Fibo(10)
print(value)