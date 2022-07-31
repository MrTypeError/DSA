
def findMedianSortedArrays(nums1,nums2):
    
    if (len(nums1) < len(nums2)):
        return findMedianSortedArrays(nums2 ,nums1)

    n1 = len(nums1)
    n2 = len(nums2)
    low , high = 0, n1

    while low <high:
        cut1 = (low+high)//2
        cut2 = (n1+n2+1)//2 -1

        if cut1 == 0:
            INT_MAX = nums1[cut1 - 1]
            
        if cut2 == 0:
            INT_MAX = nums2[cut2 - 1]
            

        # left1 =
        # left2 = 

        # right1 =
        # right2 = 

        if left1<left2 and left2 <= right1 :
            
            if ( n1 + n2 )%2 == 0:
                return (max(left1, left2)+min(right1, right2))/2.0
            
            else:
                return max(left1 ,left2)
        
        elif left1>right2 :
            high = cut1 - 1 
        
        else:
            low = cut2 + 1
    
    return 0


                

