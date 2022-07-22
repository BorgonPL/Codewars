def Vapor(x):
    return ''.join(x[y].upper() + ' ' for y in range(len(x)) if x[y] != " ")[:-2]