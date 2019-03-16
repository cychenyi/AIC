import random

if __name__ == '__main__':
    mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # 通过id来证明该列表和新列表是否相同
    olist = [o for o in mlist if o % 2 == 0]
    print("olist =", olist)
    plist = [1, 2, 3, 4]
    ilist = [100, 200, 300, 400]
    jlist = [m + n for m in plist for n in ilist]
    print("no if ->", jlist)
    jlist = [m + n for m in plist if m % 2 == 0 for n in ilist]
    print("with if ->", jlist)
    olist = [m for m in mlist if m % 2 == 0]
    print("olist=", olist)
    jlist = [m + n for m in plist for n in ilist]
    print("jlist == ", jlist)
    jlist = [m + n for m in plist if m % 2 == 0 for n in ilist]
    print("plist == ", jlist)
    mlist = [['a', 'b'], ['e', 'f'], ['g', 'h']]
    nlist = [[m, n] for m, n in mlist]
    print(mlist)
    nlist = [[m, n] for m, n in mlist]
    print(mlist)
    nlist = [[m, n] for m, n in mlist]
    print(mlist)
    # 随机生成整数 1-100  10个随机数
    mlist = [random.randint(0, 100) for i in range(0, 10)]
    print(mlist)
    mlist = [random.randint(0, 100) for i in range(0, 30)]
    print(mlist)
    mlist = [random.randint(0, 200) for i in range(0, 20)]
    print(mlist)
0
if __name__ == '__main__':
    # 创建一个非空列表使用中括号
    mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    nlist = mlist[-2:-4:-1]
    print("id -> mlist", id(mlist))
    print("id -< nlist", id(nlist))
    plist = [1, 2, 3, 4]
    olist = plist
    print("plist id is {plistid}".format(plistid=id(plist)))
    print("olist id is {olistid}".format(olistid=id(olist)))
    ulist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(id(ulist))
    del ulist[4]
    print(ulist)
    print(id(ulist))
    t = 2
    print("in ->", t in mlist)
    print("not in ->", t not in mlist)
    nist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nlist = [i for i in range(1, 10)]
    print("nlist =", nlist)
    nlist = [i for i in range(2, 5)]
    print(nlist)
    nlist = [i for i in range(3, 8)]
    print(nlist)
    # _index_()获取当前值在list中的下标
    nlist = [[7, 8, 9, ], [4, 5, 6], [1, 2, 3]]
    for sublist in nlist:
        for j in sublist:
            print("nlist[{1}] = {0}".format(j, j.__index__()))
    for sublist in nlist:
        for j in sublist:
            print("nlist[{1}] = {1}".format(j, j.__index__()))
    for sublist in nlist:
        for j in sublist:
            print("nlist[{1}] = {2}".format(j, j.__index__()))
    mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    olist = [o for o in mlist]
    print("olist = ", olist)
    print("olist id - >", id(olist))
    print("mlist id - >", id(mlist))
    klist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    olist = [o for o in klist if o % 2 == 0]
    print("olist=", olist)



