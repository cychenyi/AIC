import random
if __name__ == '__main__':
    arr=[]


    for i in range(0,10) :
        num = random.randint(0, 100)
        arr.append(num)

        if len(arr)>10 :
            break
    print(arr)
    mu=random.randint(0,100)
    print(mu)
    print(mu in arr)