# Infix TO Postfix
def infixToPostfix(string):
    ans ,operator =[] , []
    priority = {}
    for ch in string:
        if ch == "(":
            operator.append(ch)
        elif ch ==")":
            while operator[-1] != "(":
                element = operator.pop()
                ans.append(element)
            operator.pop()
        elif ch == "^" or ch == "+" or ch == "-" or ch == "/" or ch == "*" :
            if(len(operator) >0 ):
                while priority[operator[-1]] > priority[ch]:
                    element = operator.pop()
                    ans.append(element)
                    if len(operator) == 0:
                        break
            operator.append(ch)
        else:
            ans.append(ch)
    while len(operator) != 0:
        element = operator.pop()
        ans.append(element)
    return ans 


print(infixToPostfix("(A+b)"))
                    


            