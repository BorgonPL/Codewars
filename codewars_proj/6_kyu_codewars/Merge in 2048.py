def merge(line):
    n=0
    tab=[]
    for x in range(len(line)):
        tab.append(0)
        if tab[n]==0 and line[x]!=0:
            tab[n]=line[x]
        elif line[x]!=0:
            if tab[n]== line[x]:
                tab[n]+= line[x]
                n+=1
            else: 
                n+=1
                tab[n]+= line[x]
    return tab