import random
if __name__ == '__main__':
    arr=[]
    for i in range(1,11) :
        arr.append(i)
    arr=[i for i in range(1,11)]
    print(arr)
    arr = [i**2 for i in range(1, 11)]
    print(arr)
    arr = [i ** 2 for i in range(1, 11) if i%2==0]
    print(arr)
    arr = [i ** 2 for i in range(1, 11) if i % 2 != 0]
    print(arr)
    arr = [i for i in range(1, 11,-1)]
    print(arr)
    arr = [i for i in range(11,1, -1)]
    print(arr)
    arr = [i for i in range(11, 1, -2)]
    print(arr)
    a=random.choice(arr)
    print(a)
    arr = [i for i in range(11, 1, -3)]
    print(arr)
    arr=random.randint(5,150)
    print(arr)
    arr=random.randrange(0,30)
    print(arr)
    arr = random.uniform(29,30)
    print(arr)

