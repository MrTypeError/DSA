previous = None

def f(root):
    if root :
        if not f(root.left):
            return False
        global previous
        if previous >= root.val:
            return False
        previous = root.val
        if not f(root.right):
            return False
        return True 
    return True


def solve(root):
    global previous
    previous = -(2**31+1)
    return 1 if f(root) else 0 


