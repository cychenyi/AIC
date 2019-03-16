# 1.	编写Python程序判断字符串是否重复。（50分）
# 2.	编写Python程序打印输出字符串中重复的所有字符。（50分）
# 3.	#把下面的klist作为字典的键
# #并统计每个单词的词频
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
    aset = set(klist)
    for i in aset :
        a=klist.count(i)
        if a>1 :
            print(str(i)+"重复了"+str(a)+"次")
    #创建空列表clist
    clist = []
    #去除空格，把元素放到新的列表中
    for j in klist :
        b=j.strip()
        clist.append(b)
    #创建集合，给列表去重
    zset = set(clist)
    print(zset)
    #创建空字典
    ndict=dict()
    #遍历集合，给每个键赋值
    for k in zset :
        ndict[k]=clist.count(k)
    print(ndict)