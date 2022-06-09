def pow(number,power):
    if power==0:
        return 1
    temp=pow(number,power//2)
    if power%2==1:
        return temp*temp*number
    return temp*temp

x = int(input())
n = int(input())
print(pow(x,n))

