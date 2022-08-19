def code(strng):  
    return  ''.join("0" * (len(str(bin(int(strng[x]))))-3) + '1' + bin(int(strng[x]))[2:] for x in range(len(strng)))
       
def decode(strng):
    return str(int(strng[strng.find('1')+1:(strng.find('1'))*2+2],2)) + (decode(strng[(strng.find('1')+1)*2:]) if strng.find('1')*2+2<(len(strng)) else "")