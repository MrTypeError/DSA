
# GFG - >  question -> Balanced Tree

# self written approach  
def min_value_to_balance(arr):
    no_of_ele = len(arr)//2
    sum1 , sum2 = 0, 0
    
    for i in range(len(arr)):
        if i < no_of_ele:
            sum1+=arr[i]
        else:
            sum2+=arr[i]
            
    if(sum1 > sum2):
        return sum1-sum2
    elif(sum1 < sum2):
        return sum2-sum1
    else:
        return 0
    
    
    
    # Approach No. - > 2 ( Found from the comment section)
    no_of_ele = len(arr)//2
    left_sum = sum(arr[:no_of_ele])
    right_sum = sum(arr[-no_of_ele:])
    
    print(abs(left_sum - right_sum))



min_value_to_balance([1,2,3,5])