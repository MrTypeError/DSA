def solve(x, n):
      
    #cheating In Pyhton
    
    # ans = x**n
    # return ans

####################################
####################################
####################################

    #Base 
    if n == 0:
        return 1
    
    # Flags 

    is_x_negative , is_n_negative = x<0 , n<0
    x , n = abs(x) , abs(n)

    # Real Algo

    halfans = solve(x ,  n//2)
    if n%2 == 1:
        ans = halfans*halfans*x
    else :
        ans = halfans*halfans
    
    # Flags Checks 
    if is_x_negative and n%2 ==1:
        ans = -ans
    if is_n_negative:
        ans = 1/ans
    return ans 


print(solve(5,-5))