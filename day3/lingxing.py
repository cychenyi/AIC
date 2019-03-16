def lingxing(num):
    for i in range(0,num):
        print(" "*(num-i),end=" ")
        print("  *"*i,sep="  ")
    for i in range(0,num):
        print("  " * i,end=" ")
        print(" ",end="")
        print("*  "*(num-i))