
def checkBing():
    import random
    #创建10个数的列表
    mlist = [random.randint(0,100) for i in range(10)]
    # 创建15个数的列表
    nlist = [random.randint(0,100) for i in range(15)]
    print(mlist)
    print(nlist)
    #去重
    mset = set(mlist)
    nset = set(nlist)
    #求并集
    cset=nset.union(mset)
    print(cset)
