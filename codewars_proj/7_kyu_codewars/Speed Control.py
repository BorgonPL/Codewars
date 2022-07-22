def gps(s, x):
    return (3600*(max(abs(x[y+1]-x[y]) for y in range(len(x)-1)))/s) if len(x)>2 else 0