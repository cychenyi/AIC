def ling(x):
    i = 0
    while i < x:
        j = x - i
        k = 0
        while j > 0:
            print(" ", end="")
            j -= 1
        while k < i:
            print("*", end=" ")
            k += 1
        print()
        i += 1
    m = 0
    while m < x:
        j = 0
        k = x - m
        while j < m:
            print(" ", end="")
            j += 1
        while k > 0:
            print("*", end=" ")
            k -= 1
        print()
        m += 1