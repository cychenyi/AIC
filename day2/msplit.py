if __name__ == '__main__':
    arr="good good study,day day up"
    arr=arr.split(" ")
    print(arr)
    arr = arr.split(" ",1)
    print(arr)
    arr = arr.split(" ", 2)
    print(arr)
    arr = arr.split(" ", 3)
    print(arr)
    arr.sort()
    print(arr)
    arr = arr.split("o", 3)
    print(arr)
    arr.sort()
    print(arr)