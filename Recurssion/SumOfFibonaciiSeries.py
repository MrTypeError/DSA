def fibo(num):
    #intilizing the values for the limits
    # temp=fibo(num-1)
    # temp1=fibo(num-2)
    #Base condition or the terminating condition
    if num==0 or num ==1:
        return 1
    else:
        #recursive Call For the fibo function
        return fibo(num-1)+fibo(num-2)

#call starts From Here 
#input will be given here.
Num=int(input("Enter The Limit : "))
value=fibo(Num)
