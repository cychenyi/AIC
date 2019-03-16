def checkSex() :
    name=input("请输入姓名:")
    sex=input("请输入性别（男/女）:")
    adict={"男":"先生您好","女":"女士您好"}
    if sex in adict.keys():
        print(name+adict[sex])

if __name__ == '__main__':
    checkSex()