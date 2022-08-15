def valid_ISBN10(isbn): 
    print(len(isbn))
    mul=sum(int(isbn[x]) * (x+1) for x in range(len(isbn)-1))
    return True if len(isbn)==10 and mul%11==0 else False

print(valid_ISBN10('1112223339'))