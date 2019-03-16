if __name__ == '__main__':
    mlist=[]
    print(mlist)

    mlist.append("班长")
    print(mlist)
    mlist.insert(1,"学委")
    print(mlist)
    mlist.insert(2, "生委")
    print(mlist)

    print(mlist.pop(1))
    print(mlist.remove("生委"))
    mlist.pop()
    print(mlist)
    del mlist[1]
    print(mlist)
    mlist.remove("班长")
    print(mlist)

    mlist=mlist.split("")
    print(mlist)