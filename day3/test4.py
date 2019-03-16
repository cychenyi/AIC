if __name__ == '__main__':

    klist = [
    "good ","good ","study",
    " good ","good","study ",
    "good "," good"," study",
    " good ","good"," study ",
    "good ","good ","study",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",]
    #创建集合
    alist=[]
    #去除空格
    for i in klist :
        a=i.strip()
        alist.append(a)
    #去重
    aset=set(alist)
    print(aset)
    #创建字典
    adict={}
    #赋值
    for i in aset :
        adict[i]=i
    print(adict)