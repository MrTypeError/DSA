def CreateLPS(p):
    return [0,0,1,2,0,0,0,1,2,3,4,0,0,0]

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
