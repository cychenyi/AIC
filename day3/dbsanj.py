def sanjiao(x):
    i=0
    x = int(input("输入"))
    while i<=x:
        j = x-i
        k = 0
        while j>0:
            print(" ",end="")
            j-=1
        while k<i:
            print("*",end=" ")
            k+=1
        print()
        i+=1
print(sanjiao())