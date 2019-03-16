if __name__ == '__main__':
    print("输入两个数字，计算除法")
    print("树入Q退出")
    while True:
        print("\t")
        fnum = input("first number")
        if fnum == "q":
            break

        snum = input("second number:")
        if snum == "q":
            break
try:
    f = open("good.text", "r")

    f.close()
except Exception as e:
    print(e)
else:
    print("excetion else")
finally:
    print("finally")



# 定义一个函数 如果参数是0 则手动抛出异常
def mfun(v):
    if v == 0:
        raise Exception("good")



try:
    mfun(0)
except Exception as e:
    print("excetp->{0}".format(e))
    pass
print("good")



class myException(ValueError):
    pass



try:
    print("brfor raise exception")
    raise myException
    print("after raise exception")
except MyException as me:
    print("catch myException")
except ValueError as ve:
    print("catch ValueError")
except Exception as e:
    print("exception")
    print(e)



class MyExcept(Exception):
    pass

    def show(self):
        print("hehe")



import random

if __name__ == '__main__':
    mynum = [5, 9, 3, 4]
    # 打乱包的顺序
    random.shuffle(mynum)
    print(mynum)
    # 进行排序
    mynum.sort(reverse=False)
    print(mynum)
    # 倒着打印字符
    mynum.reverse()
    print(mynum)
    # 求他的长度
    len = len(mynum)
    print(len)