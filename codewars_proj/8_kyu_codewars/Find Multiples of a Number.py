def find_multiples(integer, limit):
    return [integer * (x+1) for x in range(0,int(limit/integer)) ]