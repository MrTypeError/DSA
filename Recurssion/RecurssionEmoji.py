def design(num, spc=0):

    if num == 0:
        print("Another One")
        return
        

    if(num%2==0):
        spc += 2
        print(((" :) "*num) + " " * (spc*2-4)*2 + ":" + (str(num))))
        design(num-2, spc)













design(20)