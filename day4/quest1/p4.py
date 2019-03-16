def checkHuiwen():
    astr=input("请输入一行字符串")
    if len(astr)%2==1:
        bstr=astr[::-1]
        if astr==bstr:
            print(astr + "是回文数")
        else:
            print(astr + "不是回文数")
    else:
        print(astr + "不是回文数")
