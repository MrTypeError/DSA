# class Solution:
#     def maxDepth(self, s: str):
#         # length=len(s)
#         stack=[]
#         counter,counter1,temp=0
#         # newList=["(",")","{","}","[","]"]
#         for i in s:
#         # for i in range(length):
#             stack+=[i]
#             for j in stack:
#                 if j=="(" or j=="{" or j=="[" :
#                     counter+=1
#                 elif j=="(" or j=="}" or j=="]" :
#                     counter1-=1
#                 else:
#                     pass
#             temp=max(counter,counter1)    
#             return temp 



# 1614. Maximum Nesting Depth of the Parentheses

# class Solution:
#     def maxDepth(self, s: str) -> int:
#         count = 0
#         maxCount = 0
#         for char in s:
#             if char == "(":
#                 count += 1
#                 if count > maxCount:
#                     maxCount = count
#             elif char == ")":
#                 count -= 1
#         return maxCount

# TestString=Solution
# TestString.maxDepth("(1)+((2))+(((3)))")

class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []
        for ch in s:
            if ch=='(':
                stack.append(ch)
            elif ch==')' and stack:
                stack.pop()
            else:
                continue
            res = max(res,len(stack))
        return res
string=Solution()
string.maxDepth("(1)+((2))+(((3)))")