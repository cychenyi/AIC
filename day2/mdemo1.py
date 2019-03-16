if __name__ == '__main__':
    arr=input("输入字符串")
    print(arr)
    aset=set(arr)
    for l in aset :
        a=arr.count(l)
        print(str(l)+str(a))


