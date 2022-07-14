def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def solve(n, deck):
    m={}
    for x in deck:
        if x not in m:
            m[x]=1
        else:
            m[x]+=1
    g = m[deck[0]]

    for count in m.values():
        g =gcd(max(g,count), min(g,count))
    return True if g>1 else False

print(solve(8,[1,2,3,4,4,3,2,1]))