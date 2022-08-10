def bin2dec(bin):
    bin=str(bin)
    return sum(2**a for a in range(len(bin)) if bin[-a-1]=='1')

def  removeChars(a):
    return ''.join(a[i] for i in range(len(a)) if a[i]==' ' or a[i]=='1' or a[i]=='0')

def chuck_push_ups(st): 
    if type(st)!=str:
        return "FAIL!!"
    else:
        st = removeChars(st)
        try:
            return bin2dec(max(int(a) for a in st.split(" ") if a!=''))
        except:
            return 'CHUCK SMASH!!'