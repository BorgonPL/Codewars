def calc(x):
    a="".join(str(ord(x[z])) for z in range(len(x)))
    return sum(int(a[z])-1 for z in range(len(a)) if a[z]=='7')
    