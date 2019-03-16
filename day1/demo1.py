if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9]
    for i in arr :
        for j in arr :
            if j<=i :
                mstr=str(j*i)
                print(str(j)+"*"+str(i)+"="+mstr.rjust(2),end="  ")
            else:
                pass
        print()

