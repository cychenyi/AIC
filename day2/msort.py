import random
if __name__ == '__main__':
    arr=[3,10,18,7,9]
    # 排序（升序）
    random.shuffle(arr)
    print(arr,end="")
    arr.sort()
    print(arr)
    # 排序（降序）
    random.shuffle(arr)
    print(arr, end="")
    arr.sort(reverse=True)
    print(arr)
    # 排序（临时升序）
    random.shuffle(arr)
    print(arr, end="")
    brr=sorted(arr)
    print(brr,arr)
    # 排序（临时降序）
    random.shuffle(arr)
    print(arr, end="")
    brr=sorted(arr,reverse=True)
    print(brr, arr)
    # 排序（从后往前排列）
    random.shuffle(arr)
    print(arr, end="")
    arr.reverse()
    print(arr)
    # 求列表长度
    random.shuffle(arr)
    print(arr, end="")
    a=len(arr)
    print(a)