# Leetcode :- Q26



def removeDuplicates(nums):
    empSet = set()
    for i in nums:
        if i in empSet :
            pass
        else:
            empSet.add(i)
    myList = list(empSet)
    hello = len(myList)
    return hello , myList


returnHelllo , returnList = removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])
print(returnHelllo , returnList)