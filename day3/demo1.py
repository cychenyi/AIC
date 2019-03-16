def szdq(a,b):
        arr = range(a, b)
        for i in arr:
            print(str(i).rjust(3), end="")

            c=[i].count()
            if c % 10 ==0:
                print()
if __name__ == '__main__':
    a=input("dyi")
    b=input("der")
    szdq(int(a), int(b))

