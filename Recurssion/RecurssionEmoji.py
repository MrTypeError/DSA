def design(num, spc=0,spc2=0):

    if num == 0:
        return
        

    if(num%2==0):
        spc += 2
        print(((" :) "*num) + " " * (spc*2-4)*2 + ":" + (str(num))))
        design(num-2, spc)
    
    if True:
        def ReverseFun(spc2):
            spc2 += 2
            print(((" :) "*spc2) + " " * (num*2-4)*2 + ":" + (str(spc2))))
            design(num-2, spc)
        











design(20)