def compare_versions(v1,v2):
    v1 = v1.split('.')
    v2 = v2.split('.')
    while(len(v1)!=len(v2)):
        if len(v1)>len(v2):
            v2.append('0')
        else: v1.append('0')
    for x in range(len(v1)):
        if int(v1[x])>int(v2[x]):
            return True
        elif v1[x]==v2[x]:
            continue
        elif int(v1[x])<int(v2[x]): return False
    return True