def infinityStone(a ,arr):
    min = arr[0]
    arr.sort()
    for x in arr:
        if min > x:
            min = x

    print(min)




print(infinityStone(8 ,
                    [42 , 4 , 26 , 39 , 20 , 46 , 20 , 40]
                    ))



# [39,40,42,46]
# [37,41,44,47,49]