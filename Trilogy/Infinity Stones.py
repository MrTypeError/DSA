def infinityStone(a ,arr):
    # j , z  = 1 , 1 
    # arr.sort()
    # for x in arr[::-1]:
    #     sum = x*j
    #     if sum > z:
    #         z=sum
    #     j+=1

    # print(sum)

    sum = 0
    j , i , p = 1 , 0 , 1
    arr.sort() 
    b = arr[::-1] 
    for el in b: 
        p = el *j
        if p>sum:
            sum = p
        j+=1
    return sum




    

print(infinityStone(8 ,
                    [42 , 4 , 26 , 39 , 20 , 46 , 20 , 40]
                    ))
print(infinityStone(9 ,
                    [49, 41 , 2 , 14 , 13 , 44 , 47 , 37 , 34]
                    ))



# [39,40,42,46]
# [37,41,44,47,49]