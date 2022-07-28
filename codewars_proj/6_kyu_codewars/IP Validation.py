def is_valid_IP(string):
    s=string.split('.')
    if len(s)==4:
        for x in s:
            if str(x).isdigit()!=True or int(x)<0 or int(x)>255 or str(int(x))==x:
                return False
    else: 
        return False
    return True
