def heron(a, b, c):
    s=(a+b+c)/2
    return round(pow(s*(s-a)*(s-b)*(s-c),1/2),2)