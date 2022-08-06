def gordon(a):
    b=''
    for i in a.upper():
        if i in 'EUIO':
            b+= '*'
        else: 
            b+= i
    a=(''.join(i.replace('A','@') + '!!!! ' for i in b.split(" ")))
    return a[:-1]