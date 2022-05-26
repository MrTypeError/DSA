# 20. Valid Parentheses


# class Solution:
#     def isValid(self, s: str) -> bool:
#         op1,op2,op3= 0
#         cl1,cl2,cl3=0
#         for ch in s:
#             if ch=="(":
#                 op1+=1
#             elif ch=="{":
#                 op2+=1
#             elif ch=="[":
#                 op3+=1
            
#             elif ch==")":
#                 cl1+=1
            
#             elif ch=="}":
#                 cl2+=1
#             else:
#                 cl3+=1
#         if op1+op2+op3==cl1+cl2+cl3:
#             return True
#         else:
#             return False

# Test=Solution()

# Test.isValid("{}[]{]")




class Solution:
    def isValid(self, s: str) -> bool:
        # Time: O(n), Space: O(n)
        stack = []
        for p in s:
            if stack and stack[-1] == '{' and p == '}':
                stack.pop()
            elif stack and stack[-1] == '(' and p == ')':
                stack.pop()
            elif stack and stack[-1] == '[' and p == ']':
                stack.pop()
            else:
                stack.append(p)
        return len(stack)==0


Test=Solution()
print(Test.isValid("()[][{()}]"))