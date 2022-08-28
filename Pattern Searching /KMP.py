def CreateLPS(p):
    # return [0,0,1,2,0,0,0,1,2,3,4,0,0,0]
    m = len(p)
    lps = [0]*m
    prefix , curr = 0 ,1
    while curr<m:
        if p[curr] == p[prefix]:
            prefix+=1
            curr+=1
        else:
            if prefix == 0:
                lps[curr] =0
            else:
                prefix = lps[prefix-1]
    return lps

def KMP(s, p):
    n, m =len(s) , len(p)
    lps = CreateLPS(p)
    sp = pp =0
    while sp <n:
        if s[sp]== p[pp]:
            sp+=1
            pp+=1
        else:
            if pp == 0:
                sp+=1
            else:
                pp = lps[pp-1]
        if pp==m:
            print(f"Pattern Found at {sp-pp} Location !")
            break
KMP("ababxyzabababxyzababyyz" , "ababxyzababyyz")
