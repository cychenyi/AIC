# 4.klist = [
#     "good ","good ","study",
#     " good ","good","study ",
#     "good "," good"," study",
#     " good ","good"," study ",
#     "good ","good ","study",
#     " day ","day"," up",
#     " day ","day"," up",
#     " day ","day"," up",
#     " day ","day"," up",
#     " day ","day"," up",
#     " day ","day"," up",
#     " day ","day"," up",
#          ]
if __name__ == '__main__':

    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    qlist=[]
    for i in klist :
        qlist.append(i.strip())
    qset=set(qlist)
    for l in qset :
        a=qlist.count(l)
        print(l+str(a))
    qdict={}
    for n in qset :
        qdict[n]=n
    print(qdict)
    mdict={}
    for m in qset :
        mdict[m]=qlist.count(m)
    print(mdict)
