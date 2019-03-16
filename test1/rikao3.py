import random
if __name__ == '__main__':
    arr=[1,2,3]
    brr=random.randint(0,5)
    for i in arr :
        if i>brr :
            print(str(i)+">"+str(brr))
            break
        else :
            print(str(brr) + ">" + str(i))
            break

