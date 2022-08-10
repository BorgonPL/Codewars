def modify_multiply(st, loc, num):
    st=st.split(" ")
    return (st[loc]+'-')*(num-1)+st[loc] if num>0 else ''