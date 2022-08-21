def find_lowest_int(k):
    n=1
    while 1:
        if sorted(str(k*n))==sorted(str((k+1)*n)):
            break
        n+=1
    return n