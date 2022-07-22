def is_valid_IP(strng):
    s=strng.split(".")
    if len(s)==4: 
        for x in s:
            if int(x)>255 or int(x)<0:
                return False
    else: return False
    return True